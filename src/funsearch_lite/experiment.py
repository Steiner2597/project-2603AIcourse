from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
import json
from pathlib import Path
import random
import traceback

from .config import ExperimentConfig, SearchConfig
from .datasets import generate_synthetic_instances, load_orlib_instances
from .evaluator import evaluate_candidate
from .evolution import Candidate, IslandEvolution, SearchHistory
from .heuristic_expr import build_scorer, local_perturb_expression
from .summarize import write_summary_files
from .visualize import save_curve


def run_experiment(exp_cfg: ExperimentConfig, search_cfg: SearchConfig, llm_client=None, resume_run_dir: str | Path | None = None) -> dict:
    if resume_run_dir:
        run_dir = Path(resume_run_dir)
    else:
        ts = datetime.now().strftime("%y%m%d%H%M%S")
        provider_tag = _normalize_provider_tag(exp_cfg.provider_tag)
        seed_tag = f"seed{search_cfg.random_seed}"
        if exp_cfg.dataset == "orlib":
            run_name = f"{ts}_{provider_tag}_{seed_tag}"
        else:
            size_tag = {"small": "s", "large": "l", "medium": "m"}.get(exp_cfg.size, "s")
            run_name = f"{ts}_syn_{size_tag}_{provider_tag}_{seed_tag}"
        run_dir = Path(exp_cfg.output_dir) / run_name
    run_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_dir = run_dir / "checkpoints"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    if llm_client is not None and hasattr(llm_client, "set_checkpoint_dir"):
        llm_client.set_checkpoint_dir(checkpoint_dir)

    started_at = datetime.now().isoformat(timespec="seconds")
    prev_status_fp = run_dir / "status.json"
    if resume_run_dir and prev_status_fp.exists():
        try:
            prev_status = json.loads(prev_status_fp.read_text(encoding="utf-8"))
            started_at = str(prev_status.get("started_at") or started_at)
        except Exception:
            pass

    status = {
        "status": "running",
        "phase": "preparing_data",
        "started_at": started_at,
    }
    (run_dir / "status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")

    if exp_cfg.dataset == "orlib":
        instances = load_orlib_instances("data/orlib", source=exp_cfg.orlib_source or None)
        if not instances:
            if exp_cfg.orlib_source:
                raise RuntimeError(f"No OR-Library instances found for source={exp_cfg.orlib_source} under data/orlib")
            raise RuntimeError("No OR-Library instances found under data/orlib")
    else:
        instances = generate_synthetic_instances(exp_cfg.size, seed=search_cfg.random_seed)

    status["phase"] = "searching"
    (run_dir / "status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")

    resume_generation = 0
    initial_islands = None
    history_prefix = None
    if resume_run_dir:
        resume_generation, initial_islands, history_prefix = _load_resume_state(
            checkpoint_dir=checkpoint_dir,
            islands=search_cfg.islands,
            population_size=search_cfg.population_size,
        )
        status["resumed_from_generation"] = resume_generation
        (run_dir / "status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")

    engine = IslandEvolution(
        config=search_cfg,
        instances=instances,
        capacity=exp_cfg.bin_capacity,
        llm_client=llm_client,
        checkpoint_dir=checkpoint_dir,
        resume_generation=resume_generation,
        initial_islands=initial_islands,
        history_prefix=history_prefix,
    )
    try:
        result = engine.run()
    except Exception as exc:
        status = {
            "status": "failed",
            "started_at": status["started_at"],
            "finished_at": datetime.now().isoformat(timespec="seconds"),
            "error": str(exc),
            "traceback": traceback.format_exc(),
        }
        (run_dir / "status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")
        # Even on failure, write a partial summary from whatever checkpoints exist.
        try:
            write_summary_files(run_dir)
        except Exception:
            pass
        raise

    best_expr = result.best_expression
    best_score = result.best_score
    local_search_trace = {
        "enabled": True,
        "top_k": search_cfg.local_search_top_k,
        "steps": search_cfg.local_search_steps,
        "improved": False,
        "start_best_score": best_score,
        "end_best_score": best_score,
        "records": [],
    }
    ls_expr, ls_score, ls_records = _run_local_search(
        instances=instances,
        initial_best_expr=best_expr,
        initial_best_score=best_score,
        elite_expressions=result.elite_expressions,
        capacity=exp_cfg.bin_capacity,
        top_k=search_cfg.local_search_top_k,
        steps_per_expr=search_cfg.local_search_steps,
        seed=search_cfg.random_seed,
    )
    if ls_score < best_score:
        best_expr, best_score = ls_expr, ls_score
        local_search_trace["improved"] = True
    local_search_trace["end_best_score"] = best_score
    local_search_trace["records"] = ls_records
    (checkpoint_dir / "local_search.json").write_text(
        json.dumps(local_search_trace, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    final_eval = evaluate_candidate(
        instances,
        build_scorer(best_expr),
        behavior_signature_points=search_cfg.behavior_signature_points,
    )

    # Baselines: First-Fit (FF) and Best-Fit (BF) for comparison.
    ff_eval = evaluate_candidate(instances, lambda _: 0.0, behavior_signature_points=search_cfg.behavior_signature_points)
    bf_eval = evaluate_candidate(instances, build_scorer("-after"), behavior_signature_points=search_cfg.behavior_signature_points)

    per_source: dict[str, dict] = {}
    for pi in final_eval.per_instance:
        key = pi.source or "unknown"
        bucket = per_source.setdefault(key, {"count": 0, "avg_bins_sum": 0.0, "gap_sum": 0.0, "gap_ratio_sum": 0.0, "gap_count": 0})
        bucket["count"] += 1
        bucket["avg_bins_sum"] += pi.bins_used
        if pi.gap is not None:
            bucket["gap_sum"] += pi.gap
            bucket["gap_count"] += 1
        if pi.gap_ratio is not None:
            bucket["gap_ratio_sum"] += pi.gap_ratio

    per_source_summary = {}
    for key, bucket in per_source.items():
        c = max(1, bucket["count"])
        gap_c = max(1, bucket.get("gap_count", 0)) if bucket.get("gap_count", 0) > 0 else None
        per_source_summary[key] = {
            "instances": bucket["count"],
            "avg_bins": bucket["avg_bins_sum"] / c,
            "avg_gap": (bucket["gap_sum"] / gap_c) if gap_c else None,
            "avg_gap_ratio": (bucket["gap_ratio_sum"] / gap_c) if gap_c else None,
        }

    metrics = {
        "best_score": best_score,
        "best_expression": best_expr,
        "history": asdict(result.history),
        "search_config": asdict(search_cfg),
        "experiment_config": asdict(exp_cfg),
        "local_search": {
            "improved": local_search_trace["improved"],
            "start_best_score": local_search_trace["start_best_score"],
            "end_best_score": local_search_trace["end_best_score"],
            "top_k": search_cfg.local_search_top_k,
            "steps": search_cfg.local_search_steps,
        },
        "instances": {
            "count": len(instances),
            "avg_items": sum(len(x.items) for x in instances) / max(1, len(instances)),
        },
        "evaluation": {
            "avg_bins_used": final_eval.avg_bins_used,
            "avg_gap": final_eval.avg_gap,
            "avg_gap_ratio": final_eval.avg_gap_ratio,
            "per_instance": [
                {
                    "name": pi.name,
                    "source": pi.source,
                    "capacity": pi.capacity,
                    "bins_used": pi.bins_used,
                    "optimal_bins": pi.optimal_bins,
                    "gap": pi.gap,
                    "gap_ratio": pi.gap_ratio,
                }
                for pi in final_eval.per_instance
            ],
            "per_source_summary": per_source_summary,
            "baselines": {
                "ff": {
                    "avg_bins": ff_eval.avg_bins_used,
                    "avg_gap": ff_eval.avg_gap,
                    "avg_gap_ratio": ff_eval.avg_gap_ratio,
                },
                "bf": {
                    "avg_bins": bf_eval.avg_bins_used,
                    "avg_gap": bf_eval.avg_gap,
                    "avg_gap_ratio": bf_eval.avg_gap_ratio,
                },
            },
        },
    }
    (run_dir / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    (run_dir / "best_expression.txt").write_text(best_expr + "\n", encoding="utf-8")

    binpack_root = run_dir / "binpacks"
    binpack_root.mkdir(parents=True, exist_ok=True)
    # Precompute per-source baseline rollups.
    ff_by_source: dict[str, list[tuple[int | None, float | None]]] = {}
    bf_by_source: dict[str, list[tuple[int | None, float | None]]] = {}
    for res, bucket in ((ff_eval, ff_by_source), (bf_eval, bf_by_source)):
        for pi in res.per_instance:
            key = pi.source or "unknown"
            bucket.setdefault(key, []).append((pi.optimal_bins, pi.gap_ratio))

    def _avg_gap_ratio(bucket: dict[str, list[tuple[int | None, float | None]]], key: str) -> float | None:
        vals = [gr for opt, gr in bucket.get(key, []) if gr is not None]
        return sum(vals) / len(vals) if vals else None

    for source, summary in per_source_summary.items():
        sub = binpack_root / source
        sub.mkdir(parents=True, exist_ok=True)
        per_inst = [pi for pi in metrics["evaluation"]["per_instance"] if (pi.get("source") or "unknown") == source]
        payload = {
            "source": source,
            "summary": summary,
            "instances": per_inst,
            "baselines": {
                "ff_gap_ratio": _avg_gap_ratio(ff_by_source, source),
                "bf_gap_ratio": _avg_gap_ratio(bf_by_source, source),
            },
        }
        (sub / "report.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        checkpoint_payload = {
            "source": source,
            "summary": summary,
            "instances": per_inst,
            "baselines": payload["baselines"],
        }
        (checkpoint_dir / f"{source}.json").write_text(
            json.dumps(checkpoint_payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    save_curve(result.history.best_per_gen, result.history.avg_per_gen, run_dir / "curve.png")

    status = {
        "status": "completed",
        "started_at": status["started_at"],
        "finished_at": datetime.now().isoformat(timespec="seconds"),
    }
    (run_dir / "status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")

    # Auto-generate summary for every completed experiment run.
    write_summary_files(run_dir)

    return {"run_dir": str(run_dir), **metrics}


def _load_resume_state(
    checkpoint_dir: Path,
    islands: int,
    population_size: int,
) -> tuple[int, list[list[Candidate]], SearchHistory]:
    pop_files = sorted(checkpoint_dir.glob("population_gen_*.json"))
    if not pop_files:
        raise RuntimeError(f"No population checkpoints found under {checkpoint_dir}")

    latest_fp = pop_files[-1]
    try:
        pop_payload = json.loads(latest_fp.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"Failed to read checkpoint file: {latest_fp}") from exc

    generation = int(pop_payload.get("generation") or 0)
    islands_payload = pop_payload.get("islands") or []
    if len(islands_payload) != islands:
        raise RuntimeError(
            f"Checkpoint island count mismatch: checkpoint={len(islands_payload)} expected={islands}"
        )

    restored_islands: list[list[Candidate]] = []
    for island_payload in islands_payload:
        candidates_payload = island_payload.get("candidates") or []
        if len(candidates_payload) < population_size:
            raise RuntimeError(
                f"Checkpoint population too small: island={island_payload.get('island')} "
                f"size={len(candidates_payload)} expected>={population_size}"
            )
        restored = [
            Candidate(
                expr=str(c.get("expr", "")),
                score=float(c.get("score", 0.0)),
                novelty=float(c.get("novelty", 0.0)),
                stability=float(c.get("stability", 0.0)),
                behavior_signature=str(c.get("behavior_signature", "")),
            )
            for c in candidates_payload[:population_size]
        ]
        restored.sort(key=lambda x: x.score)
        restored_islands.append(restored)

    gen_files = sorted(checkpoint_dir.glob("gen_*.json"))
    best_per_gen: list[float] = []
    avg_per_gen: list[float] = []
    expr_hits: list[int] = []
    behavior_hits: list[int] = []
    for fp in gen_files:
        try:
            payload = json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            continue
        g = int(payload.get("generation") or 0)
        if g <= 0 or g > generation:
            continue
        best_per_gen.append(float(payload.get("best_score", 0.0)))
        avg_per_gen.append(float(payload.get("avg_score", 0.0)))
        expr_hits.append(int(payload.get("dedup_expr_hits", 0)))
        behavior_hits.append(int(payload.get("dedup_behavior_hits", 0)))

    history = SearchHistory(
        best_per_gen=best_per_gen,
        avg_per_gen=avg_per_gen,
        dedup_expr_hits=expr_hits,
        dedup_behavior_hits=behavior_hits,
    )
    return generation, restored_islands, history


def _normalize_provider_tag(provider_tag: str | None) -> str:
    raw = (provider_tag or "none").strip().lower()
    if not raw:
        return "none"
    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789+-_")
    if all(ch in allowed for ch in raw):
        return raw[:80]
    return "none"


def _run_local_search(
    *,
    instances: list[list[float]],
    initial_best_expr: str,
    initial_best_score: float,
    elite_expressions: list[str],
    capacity: float,
    top_k: int,
    steps_per_expr: int,
    seed: int,
) -> tuple[str, float, list[dict]]:
    rng = random.Random(seed + 7919)
    cache: dict[str, float] = {}

    def eval_expr(expr: str) -> float | None:
        if expr in cache:
            return cache[expr]
        try:
            res = evaluate_candidate(instances, build_scorer(expr))
            score = res.avg_gap_ratio if res.avg_gap_ratio is not None else res.avg_bins_used
            cache[expr] = score
            return score
        except Exception:
            return None

    best_expr = initial_best_expr
    best_score = initial_best_score
    records: list[dict] = []

    for rank, base_expr in enumerate(elite_expressions[: max(1, top_k)]):
        current_expr = base_expr
        current_score = eval_expr(base_expr)
        if current_score is None:
            continue

        for step in range(1, max(1, steps_per_expr) + 1):
            cand_expr = local_perturb_expression(current_expr, rng)
            cand_score = eval_expr(cand_expr)
            status = "invalid" if cand_score is None else "evaluated"

            if cand_score is not None and cand_score <= current_score:
                current_expr = cand_expr
                current_score = cand_score
                status = "accepted_local"

            if cand_score is not None and cand_score < best_score:
                best_expr = cand_expr
                best_score = cand_score
                status = "new_global_best"

            records.append(
                {
                    "elite_rank": rank,
                    "step": step,
                    "status": status,
                    "candidate_score": cand_score,
                }
            )

    return best_expr, best_score, records
