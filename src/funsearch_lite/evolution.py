from __future__ import annotations

from dataclasses import dataclass
import math
import random
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

from .config import SearchConfig
from .dedup import FunctionalDeduplicator
from .evaluator import evaluate_candidate
from .heuristic_expr import (
    build_scorer,
    crossover_expression,
    expression_hash,
    local_perturb_expression,
    mutate_expression,
    normalize_expression,
    random_expression,
)


@dataclass(slots=True)
class Candidate:
    expr: str
    score: float
    novelty: float
    stability: float
    behavior_signature: str


@dataclass(slots=True)
class SearchHistory:
    best_per_gen: list[float]
    avg_per_gen: list[float]
    dedup_expr_hits: list[int]
    dedup_behavior_hits: list[int]


@dataclass(slots=True)
class SearchResult:
    best_expression: str
    best_score: float
    history: SearchHistory
    elite_expressions: list[str]
    elite_scores: list[float]


class IslandEvolution:
    def __init__(
        self,
        config: SearchConfig,
        instances: list[list[float]],
        capacity: float,
        llm_client=None,
        checkpoint_dir: str | Path | None = None,
        resume_generation: int = 0,
        initial_islands: list[list[Candidate]] | None = None,
        history_prefix: SearchHistory | None = None,
    ) -> None:
        self.cfg = config
        self.instances = instances
        self.capacity = capacity
        self.llm_client = llm_client
        self.rng = random.Random(config.random_seed)
        self.dedup = FunctionalDeduplicator()
        self._behavior_eval_counts: dict[tuple[int, int, str], int] = defaultdict(int)
        self._behavior_global_counts: dict[str, int] = defaultdict(int)
        self._island_best_history: dict[int, list[float]] = defaultdict(list)
        self._stability_cache: dict[str, float] = {}
        self.checkpoint_dir = Path(checkpoint_dir) if checkpoint_dir else None
        self.resume_generation = max(0, int(resume_generation or 0))
        self.initial_islands = initial_islands
        self.history_prefix = history_prefix
        if self.checkpoint_dir:
            self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        # OR-Library style scores are ratios (e.g., 0.0523), which are easier to read as percentages.
        self._score_is_ratio = all(
            getattr(inst, "optimal_bins", None) is not None and getattr(inst, "optimal_bins", 0) > 0
            for inst in self.instances
        ) if self.instances else False

    def run(self) -> SearchResult:
        if self.cfg.verbose:
            print(
                f"[search] start generations={self.cfg.generations} "
                f"population={self.cfg.population_size} islands={self.cfg.islands}",
                flush=True,
            )
        islands: list[list[Candidate]] = []
        start_gen = 0
        if self.initial_islands is not None:
            islands = self.initial_islands
            start_gen = self.resume_generation
            if self.cfg.verbose:
                print(f"[search] resumed from generation={start_gen}", flush=True)
        else:
            for island_idx in range(self.cfg.islands):
                islands.append(self._init_island(island_idx=island_idx))
            if self.cfg.verbose:
                print("[search] initial population ready", flush=True)
            self._write_population_checkpoint(generation=0, islands=islands)

        best_per_gen: list[float] = []
        avg_per_gen: list[float] = []
        expr_hits: list[int] = []
        beh_hits: list[int] = []
        if self.history_prefix is not None:
            best_per_gen.extend(self.history_prefix.best_per_gen)
            avg_per_gen.extend(self.history_prefix.avg_per_gen)
            expr_hits.extend(self.history_prefix.dedup_expr_hits)
            beh_hits.extend(self.history_prefix.dedup_behavior_hits)

        for gen in range(start_gen, self.cfg.generations):
            for i in range(self.cfg.islands):
                islands[i] = self._evolve_one_generation(islands[i], gen, island_idx=i)

            if gen > 0 and gen % self.cfg.migration_interval == 0:
                self._migrate(islands)

            all_scores = [c.score for island in islands for c in island]
            best_per_gen.append(min(all_scores))
            avg_per_gen.append(sum(all_scores) / max(1, len(all_scores)))
            expr_hits.append(self.dedup.stats.expr_hit)
            beh_hits.append(self.dedup.stats.behavior_hit)

            if self.cfg.verbose and (gen % max(1, self.cfg.log_interval) == 0):
                if self._score_is_ratio:
                    best_text = f"{best_per_gen[-1] * 100.0:.3f}%"
                    avg_text = f"{avg_per_gen[-1] * 100.0:.3f}%"
                else:
                    best_text = f"{best_per_gen[-1]:.6f}"
                    avg_text = f"{avg_per_gen[-1]:.6f}"
                print(
                    f"[gen {gen + 1}/{self.cfg.generations}] "
                    f"best={best_text} avg={avg_text} "
                    f"expr_dedup={self.dedup.stats.expr_hit} beh_dedup={self.dedup.stats.behavior_hit}",
                    flush=True,
                )
            self._write_generation_checkpoint(gen + 1, best_per_gen[-1], avg_per_gen[-1])
            self._write_population_checkpoint(generation=gen + 1, islands=islands)

        all_candidates = [c for island in islands for c in island]
        all_candidates_sorted = sorted(all_candidates, key=lambda c: c.score)
        best = all_candidates_sorted[0]
        elite = all_candidates_sorted[: max(1, min(12, len(all_candidates_sorted)))]
        return SearchResult(
            best_expression=best.expr,
            best_score=best.score,
            history=SearchHistory(
                best_per_gen=best_per_gen,
                avg_per_gen=avg_per_gen,
                dedup_expr_hits=expr_hits,
                dedup_behavior_hits=beh_hits,
            ),
            elite_expressions=[c.expr for c in elite],
            elite_scores=[c.score for c in elite],
        )

    def _init_island(self, island_idx: int) -> list[Candidate]:
        population: list[Candidate] = []
        pool: list[Candidate] = []
        target_pool = self.cfg.population_size + max(4, int(self.cfg.population_size * self.cfg.oversample_ratio))
        attempts = 0
        max_attempts = self.cfg.population_size * 80
        while len(pool) < target_pool and attempts < max_attempts:
            if self.cfg.verbose and (attempts == 0 or attempts % 5 == 0):
                print(
                    f"[init] attempts={attempts} accepted={len(pool)}/{target_pool}",
                    flush=True,
                )
            expr = random_expression(self.rng)
            slot = len(pool)
            cand = self._evaluate_expr(
                expr,
                stage="init",
                generation=0,
                island_idx=island_idx,
                population_slot=slot,
                attempt=attempts,
                source="random_init",
            )
            if cand is not None:
                pool.append(cand)
                self._write_init_checkpoint(len(pool), target_pool, attempts)
            attempts += 1

        population = self._select_diverse_population(pool, self.cfg.population_size, generation=0)

        if not population:
            raise RuntimeError("Failed to initialize population. Try reducing dedup strictness or changing seed.")

        while len(population) < self.cfg.population_size:
            base = population[self.rng.randrange(len(population))]
            fallback = Candidate(
                expr=base.expr,
                score=base.score,
                novelty=base.novelty,
                stability=base.stability,
                behavior_signature=base.behavior_signature,
            )
            population.append(fallback)
            self._write_init_checkpoint(len(population), self.cfg.population_size, attempts)
        return sorted(population, key=lambda c: c.score)

    def _evolve_one_generation(self, island: list[Candidate], gen: int, island_idx: int) -> list[Candidate]:
        generation_idx = gen + 1
        stagnated = self._is_stagnated(island, island_idx)
        effective_restart_ratio = self.cfg.restart_inject_ratio
        effective_llm_seeds = self.cfg.llm_seed_per_generation
        if stagnated:
            effective_restart_ratio = min(0.8, effective_restart_ratio * self.cfg.stagnation_restart_boost)
            effective_llm_seeds = max(0, effective_llm_seeds + self.cfg.stagnation_llm_boost)
            if self.cfg.verbose:
                print(
                    f"[stagnation] gen={generation_idx} island={island_idx} "
                    f"boost_restart={effective_restart_ratio:.2f} boost_llm_seeds={effective_llm_seeds}",
                    flush=True,
                )

        next_pop = list(island[: max(2, self.cfg.population_size // 6)])
        target_pool = self.cfg.population_size + max(4, int(self.cfg.population_size * self.cfg.oversample_ratio))

        if generation_idx % max(1, self.cfg.restart_interval) == 0 and effective_restart_ratio > 0:
            inject_n = max(1, int(self.cfg.population_size * effective_restart_ratio))
            self._inject_random_restarts(
                next_pop,
                generation=generation_idx,
                island_idx=island_idx,
                inject_n=min(inject_n, max(0, target_pool - len(next_pop))),
            )

        llm_proposals: list[str] = []
        if self.llm_client:
            if hasattr(self.llm_client, "set_feedback_context"):
                self.llm_client.set_feedback_context(self._build_llm_feedback(island))
            if hasattr(self.llm_client, "set_request_context"):
                self.llm_client.set_request_context(
                    {
                        "generation": gen + 1,
                        "anneal_progress": round(self._anneal_progress(generation_idx), 4),
                        "island": island_idx,
                        "phase": "proposal",
                        "stagnated": stagnated,
                    }
                )
            llm_proposals.extend(self.llm_client.generate_candidates(effective_llm_seeds))
            topk = [c.expr for c in island[: self.cfg.llm_refine_top_k]]
            if hasattr(self.llm_client, "set_request_context"):
                self.llm_client.set_request_context(
                    {
                        "generation": gen + 1,
                        "anneal_progress": round(self._anneal_progress(generation_idx), 4),
                        "island": island_idx,
                        "phase": "refine",
                        "stagnated": stagnated,
                    }
                )
            llm_proposals.extend(self.llm_client.refine_topk(topk, effective_llm_seeds))

        llm_ptr = 0
        attempts = 0
        max_attempts = self.cfg.population_size * 120
        while len(next_pop) < target_pool and attempts < max_attempts:
            p1 = self._tournament(island, generation=generation_idx)
            candidate_expr = p1.expr
            source = "tournament"

            if llm_ptr < len(llm_proposals):
                candidate_expr = llm_proposals[llm_ptr]
                llm_ptr += 1
                source = "llm"
            else:
                r = self.rng.random()
                if r < self.cfg.mutation_rate:
                    candidate_expr = mutate_expression(candidate_expr, self.rng)
                    source = "mutation"
                elif r < self.cfg.mutation_rate + self.cfg.crossover_rate:
                    p2 = self._tournament(island, generation=generation_idx)
                    candidate_expr = crossover_expression(p1.expr, p2.expr, self.rng)
                    source = "crossover"

            cand = self._evaluate_expr(
                candidate_expr,
                stage="evolve",
                generation=generation_idx,
                island_idx=island_idx,
                population_slot=len(next_pop),
                attempt=attempts,
                source=source,
            )
            if cand is not None:
                next_pop.append(cand)
            attempts += 1

        next_pop = self._select_diverse_population(next_pop, self.cfg.population_size, generation=generation_idx)

        while len(next_pop) < self.cfg.population_size:
            base = island[self.rng.randrange(len(island))]
            next_pop.append(
                Candidate(
                    expr=base.expr,
                    score=base.score,
                    novelty=base.novelty,
                    stability=base.stability,
                    behavior_signature=base.behavior_signature,
                )
            )

        # Keep score-first, then prefer behavior rarity and local robustness on ties.
        next_pop.sort(key=lambda c: self._ranking_key(c, generation=generation_idx))
        return next_pop[: self.cfg.population_size]

    def _is_stagnated(self, island: list[Candidate], island_idx: int) -> bool:
        if not island:
            return False
        history = self._island_best_history[island_idx]
        history.append(min(c.score for c in island))
        window = max(2, self.cfg.stagnation_window)
        if len(history) > window:
            del history[:-window]
        if len(history) < window:
            return False

        if max(history) - min(history) > 1e-9:
            return False

        plateau = self._island_plateau_ratio(island, self.cfg.stagnation_score_anchor)
        return plateau >= self.cfg.stagnation_ratio_threshold

    @staticmethod
    def _island_plateau_ratio(island: list[Candidate], anchor: float) -> float:
        if not island:
            return 0.0
        hit = sum(1 for c in island if abs(c.score - anchor) < 1e-9)
        return hit / float(len(island))

    def _inject_random_restarts(
        self,
        next_pop: list[Candidate],
        *,
        generation: int,
        island_idx: int,
        inject_n: int,
    ) -> None:
        if inject_n <= 0:
            return

        attempts = 0
        accepted = 0
        max_attempts = max(12, inject_n * 24)
        while accepted < inject_n and attempts < max_attempts:
            expr = random_expression(self.rng)
            cand = self._evaluate_expr(
                expr,
                stage="evolve",
                generation=generation,
                island_idx=island_idx,
                population_slot=len(next_pop),
                attempt=attempts,
                source="restart_random",
            )
            if cand is not None:
                next_pop.append(cand)
                accepted += 1
            attempts += 1

    def _build_llm_feedback(self, island: list[Candidate]) -> dict:
        if not island:
            return {}

        ranked = sorted(island, key=lambda c: (c.score, -c.novelty))
        top_n = max(1, min(3, len(ranked)))
        bottom_n = max(1, min(3, len(ranked)))

        behavior_counts: dict[str, int] = defaultdict(int)
        for cand in island:
            behavior_counts[cand.behavior_signature] += 1
        dominant_sig, dominant_count = max(behavior_counts.items(), key=lambda kv: kv[1])

        return {
            "best_score": round(ranked[0].score, 4),
            "worst_score": round(ranked[-1].score, 4),
            "good_examples": [c.expr for c in ranked[:top_n]],
            "bad_examples": [c.expr for c in ranked[-bottom_n:]],
            "dominant_behavior": {
                "signature": dominant_sig,
                "count": dominant_count,
                "total": len(island),
            },
        }

    def _evaluate_expr(
        self,
        expr: str,
        *,
        stage: str,
        generation: int,
        island_idx: int,
        population_slot: int,
        attempt: int,
        source: str,
    ) -> Candidate | None:
        try:
            expr = normalize_expression(expr)
            ehash = expression_hash(expr)
            if self.dedup.check_expr(ehash):
                self._append_eval_event(
                    {
                        "stage": stage,
                        "generation": generation,
                        "island": island_idx,
                        "population_slot": population_slot,
                        "attempt": attempt,
                        "source": source,
                        "status": "dedup_expr_hit",
                        "expr_hash": ehash,
                    }
                )
                return None

            scorer = build_scorer(expr)
            result = evaluate_candidate(
                self.instances,
                scorer,
                behavior_signature_points=self.cfg.behavior_signature_points,
            )
            primary_score = result.avg_gap_ratio if result.avg_gap_ratio is not None else result.avg_bins_used
            cached = self.dedup.lookup_behavior(result.behavior_signature)
            if cached is None:
                score = primary_score
                self.dedup.record_behavior(result.behavior_signature, score)
            else:
                score = cached

            behavior_seen = self._behavior_eval_counts[(generation, island_idx, result.behavior_signature)]
            behavior_cap, _ = self._effective_behavior_caps(generation)
            if behavior_seen >= behavior_cap:
                self._append_eval_event(
                    {
                        "stage": stage,
                        "generation": generation,
                        "island": island_idx,
                        "population_slot": population_slot,
                        "attempt": attempt,
                        "source": source,
                        "status": "dedup_behavior_overuse",
                        "expr_hash": ehash,
                        "behavior_signature": result.behavior_signature,
                        "score": score,
                        "behavior_seen": behavior_seen,
                        "behavior_cap": behavior_cap,
                    }
                )
                return None

            novelty = self._novelty_from_rarity(result.behavior_signature)
            stability = self._estimate_local_stability(expr, score)
            self._behavior_global_counts[result.behavior_signature] += 1
            self._behavior_eval_counts[(generation, island_idx, result.behavior_signature)] += 1
            self._append_eval_event(
                {
                    "stage": stage,
                    "generation": generation,
                    "island": island_idx,
                    "population_slot": population_slot,
                    "attempt": attempt,
                    "source": source,
                    "status": "accepted",
                    "expr_hash": ehash,
                    "behavior_signature": result.behavior_signature,
                    "score": score,
                    "novelty": novelty,
                    "stability": stability,
                    "behavior_cache_hit": cached is not None,
                }
            )
            return Candidate(
                expr=expr,
                score=score,
                novelty=novelty,
                stability=stability,
                behavior_signature=result.behavior_signature,
            )
        except Exception as exc:
            self._append_eval_event(
                {
                    "stage": stage,
                    "generation": generation,
                    "island": island_idx,
                    "population_slot": population_slot,
                    "attempt": attempt,
                    "source": source,
                    "status": "error",
                    "error": str(exc),
                }
            )
            return None

    def _novelty_from_rarity(self, sig: str) -> float:
        seen = self._behavior_global_counts[sig]
        return 1.0 / float(1 + seen)

    def _estimate_local_stability(self, expr: str, base_score: float) -> float:
        cached = self._stability_cache.get(expr)
        if cached is not None:
            return cached
        try:
            pert = local_perturb_expression(expr, self.rng)
            pert_res = evaluate_candidate(
                self.instances,
                build_scorer(pert),
                behavior_signature_points=self.cfg.behavior_signature_points,
            )
            pert_score = pert_res.avg_gap_ratio if pert_res.avg_gap_ratio is not None else pert_res.avg_bins_used
            stability = 1.0 / (1.0 + abs(pert_score - base_score))
        except Exception:
            stability = 0.0
        self._stability_cache[expr] = stability
        return stability

    def _tournament(self, island: list[Candidate], k: int = 4, generation: int | None = None) -> Candidate:
        picks = [island[self.rng.randrange(len(island))] for _ in range(k)]
        gen = generation if generation is not None else self.cfg.generations
        return min(picks, key=lambda c: self._ranking_key(c, generation=gen))

    def _migrate(self, islands: list[list[Candidate]]) -> None:
        migrants = [sorted(island, key=lambda c: c.score)[:2] for island in islands]
        for i in range(len(islands)):
            target = (i + 1) % len(islands)
            islands[target][-2:] = migrants[i]

    def _write_generation_checkpoint(self, generation: int, best_score: float, avg_score: float) -> None:
        if not self.checkpoint_dir:
            return
        payload = {
            "generation": generation,
            "best_score": best_score,
            "avg_score": avg_score,
            "dedup_expr_hits": self.dedup.stats.expr_hit,
            "dedup_behavior_hits": self.dedup.stats.behavior_hit,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }
        fp = self.checkpoint_dir / f"gen_{generation:04d}.json"
        fp.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _write_population_checkpoint(self, generation: int, islands: list[list[Candidate]]) -> None:
        if not self.checkpoint_dir:
            return
        payload = {
            "generation": generation,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "island_count": len(islands),
            "population_size": self.cfg.population_size,
            "islands": [
                {
                    "island": island_idx,
                    "size": len(population),
                    "candidates": [
                        {
                            "expr": cand.expr,
                            "score": cand.score,
                            "novelty": cand.novelty,
                            "stability": cand.stability,
                            "behavior_signature": cand.behavior_signature,
                        }
                        for cand in population
                    ],
                }
                for island_idx, population in enumerate(islands)
            ],
        }
        fp = self.checkpoint_dir / f"population_gen_{generation:04d}.json"
        fp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def _write_init_checkpoint(self, accepted: int, target: int, attempts: int) -> None:
        if not self.checkpoint_dir:
            return
        payload = {
            "stage": "init",
            "accepted": accepted,
            "target": target,
            "attempts": attempts,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }
        fp = self.checkpoint_dir / "init_progress.json"
        fp.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _append_eval_event(self, payload: dict) -> None:
        if not self.checkpoint_dir:
            return
        payload["timestamp"] = datetime.now().isoformat(timespec="seconds")
        fp = self.checkpoint_dir / "eval_events.jsonl"
        with fp.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")

    def _select_diverse_population(self, candidates: list[Candidate], target_size: int, generation: int | None = None) -> list[Candidate]:
        if not candidates:
            return []

        gen = generation if generation is not None else self.cfg.generations
        sorted_pool = sorted(candidates, key=lambda c: self._ranking_key(c, generation=gen))
        selected: list[Candidate] = []
        behavior_counts: dict[str, int] = defaultdict(int)
        _, repeat_cap = self._effective_behavior_caps(gen)

        for cand in sorted_pool:
            if len(selected) >= target_size:
                break
            if behavior_counts[cand.behavior_signature] >= repeat_cap:
                continue
            selected.append(cand)
            behavior_counts[cand.behavior_signature] += 1

        if len(selected) < target_size:
            # Round-robin by behavior to avoid refill collapse to a dominant signature.
            seen_ids = {id(c) for c in selected}
            buckets: dict[str, list[Candidate]] = defaultdict(list)
            behavior_order: list[str] = []
            for cand in sorted_pool:
                if id(cand) in seen_ids:
                    continue
                sig = cand.behavior_signature
                if sig not in buckets:
                    behavior_order.append(sig)
                buckets[sig].append(cand)

            bucket_idx: dict[str, int] = defaultdict(int)
            while len(selected) < target_size:
                appended = False
                for sig in behavior_order:
                    idx = bucket_idx[sig]
                    bucket = buckets[sig]
                    if idx >= len(bucket):
                        continue
                    selected.append(bucket[idx])
                    bucket_idx[sig] += 1
                    appended = True
                    if len(selected) >= target_size:
                        break
                if not appended:
                    break

        return selected[:target_size]

    def _anneal_progress(self, generation: int) -> float:
        if not self.cfg.anneal_enable:
            return 1.0
        den = max(1, self.cfg.generations - 1)
        return min(1.0, max(0.0, (generation - 1) / float(den)))

    def _annealed_weights(self, generation: int) -> tuple[float, float]:
        p = self._anneal_progress(generation)
        novelty_w = 1.0 + (self.cfg.novelty_weight_final - 1.0) * p
        stability_w = 1.0 + (self.cfg.stability_weight_final - 1.0) * p
        return novelty_w, stability_w

    def _effective_behavior_caps(self, generation: int) -> tuple[int, int]:
        if not self.cfg.anneal_enable:
            return max(1, self.cfg.behavior_eval_cap), max(1, self.cfg.behavior_repeat_cap)
        p = self._anneal_progress(generation)
        eval_start = max(1, self.cfg.behavior_eval_cap)
        eval_end = max(eval_start, self.cfg.behavior_eval_cap_final)
        rep_start = max(1, self.cfg.behavior_repeat_cap)
        rep_end = max(rep_start, self.cfg.behavior_repeat_cap_final)
        eval_cap = int(round(eval_start + (eval_end - eval_start) * p))
        rep_cap = int(round(rep_start + (rep_end - rep_start) * p))
        return max(1, eval_cap), max(1, rep_cap)

    def _ranking_key(self, cand: Candidate, generation: int) -> tuple[float, float, float]:
        novelty_w, stability_w = self._annealed_weights(generation)
        return (cand.score, -cand.novelty * novelty_w, -cand.stability * stability_w)
