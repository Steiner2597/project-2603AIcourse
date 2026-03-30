from funsearch_lite.dedup import FunctionalDeduplicator
from funsearch_lite.config import SearchConfig
from funsearch_lite.datasets import Instance
from funsearch_lite.evolution import Candidate, IslandEvolution
from funsearch_lite.evaluator import evaluate_candidate
from funsearch_lite.heuristic_expr import build_scorer, normalize_expression, random_expression
from funsearch_lite.llm_client import LLMHeuristicClient


def test_expression_normalization_and_compile():
    expr = "exact_fit*2 - after"
    normalized = normalize_expression(expr)
    scorer = build_scorer(normalized)
    value = scorer(
        {
            "item": 0.3,
            "remaining": 0.6,
            "after": 0.3,
            "fill": 0.4,
            "mean_remaining": 0.5,
            "stdev_remaining": 0.1,
            "exact_fit": 0.0,
        }
    )
    assert isinstance(value, float)


def test_evaluator_returns_valid_result():
    instances = [
        Instance(name="a", capacity=1.0, items=[0.6, 0.4, 0.6, 0.4], optimal_bins=2),
        Instance(name="b", capacity=1.0, items=[0.5, 0.5, 0.5], optimal_bins=2),
    ]
    scorer = build_scorer("-after")
    result = evaluate_candidate(instances, scorer)
    assert result.avg_bins_used >= 1
    assert len(result.per_instance) == 2
    assert len(result.behavior_signature) == 64


def test_dedup_behavior_cache():
    d = FunctionalDeduplicator()
    assert not d.check_expr("abc")
    assert d.check_expr("abc")
    assert d.lookup_behavior("sig") is None
    d.record_behavior("sig", 12.3)
    assert d.lookup_behavior("sig") == 12.3


def test_random_expression_compiles():
    import random

    rng = random.Random(0)
    expr = random_expression(rng)
    scorer = build_scorer(expr)
    assert isinstance(
        scorer(
            {
                "item": 0.2,
                "remaining": 0.5,
                "after": 0.3,
                "fill": 0.5,
                "mean_remaining": 0.4,
                "stdev_remaining": 0.2,
                "exact_fit": 0.0,
            }
        ),
        float,
    )


def test_diverse_refill_round_robin_across_behaviors():
    cfg = SearchConfig(population_size=6, behavior_repeat_cap=1, verbose=False)
    evo = IslandEvolution(config=cfg, instances=[Instance(name="s", capacity=1.0, items=[0.5, 0.5], optimal_bins=1)], capacity=1.0)
    pool = [
        Candidate(expr="a1", score=1.0, novelty=0.0, stability=0.0, behavior_signature="A"),
        Candidate(expr="a2", score=1.1, novelty=0.0, stability=0.0, behavior_signature="A"),
        Candidate(expr="a3", score=1.2, novelty=0.0, stability=0.0, behavior_signature="A"),
        Candidate(expr="b1", score=2.0, novelty=0.0, stability=0.0, behavior_signature="B"),
        Candidate(expr="b2", score=2.1, novelty=0.0, stability=0.0, behavior_signature="B"),
        Candidate(expr="c1", score=3.0, novelty=0.0, stability=0.0, behavior_signature="C"),
        Candidate(expr="c2", score=3.1, novelty=0.0, stability=0.0, behavior_signature="C"),
    ]

    selected = evo._select_diverse_population(pool, target_size=6)
    counts: dict[str, int] = {}
    for cand in selected:
        counts[cand.behavior_signature] = counts.get(cand.behavior_signature, 0) + 1

    assert len(selected) == 6
    assert counts.get("A", 0) == 2
    assert counts.get("B", 0) == 2
    assert counts.get("C", 0) == 2


def test_llm_feedback_block_contains_optimization_hints():
    c = LLMHeuristicClient(
        api_key="",
        base_url="",
        generator_model="g",
        refiner_model="r",
        verbose=False,
    )
    c.set_feedback_context(
        {
            "best_score": 6148.75,
            "worst_score": 6681.25,
            "good_examples": ["-after", "-after+fill"],
            "bad_examples": ["remaining", "item+remaining"],
            "dominant_behavior": {"count": 9, "total": 12},
        }
    )
    block = c._format_feedback_block()
    assert "best=6148.75" in block
    assert "9/12" in block
    assert "avoid patterns" in block
    assert "behaviorally different strategies" in block


def test_restart_random_injection_adds_candidates():
    cfg = SearchConfig(population_size=10, restart_inject_ratio=0.2, restart_interval=1, verbose=False)
    evo = IslandEvolution(config=cfg, instances=[Instance(name="s", capacity=1.0, items=[0.5, 0.5], optimal_bins=1)], capacity=1.0)

    next_pop = [Candidate(expr="seed", score=1.0, novelty=0.0, stability=0.0, behavior_signature="S")]

    def fake_eval(expr: str, **kwargs):
        idx = len(next_pop)
        return Candidate(expr=expr, score=10.0 + idx, novelty=0.0, stability=0.0, behavior_signature=f"R{idx}")

    evo._evaluate_expr = fake_eval  # type: ignore[method-assign]
    evo._inject_random_restarts(next_pop, generation=1, island_idx=0, inject_n=2)

    assert len(next_pop) == 3
    assert all(c.behavior_signature.startswith(("S", "R")) for c in next_pop)


def test_behavior_eval_cap_filters_repeated_behavior():
    cfg = SearchConfig(population_size=8, behavior_eval_cap=1, verbose=False)
    evo = IslandEvolution(config=cfg, instances=[Instance(name="s", capacity=1.0, items=[0.5, 0.5], optimal_bins=1)], capacity=1.0)

    sig = "a" * 64
    first = Candidate(expr="e1", score=1.0, novelty=0.0, stability=0.0, behavior_signature=sig)
    second = Candidate(expr="e2", score=1.0, novelty=0.0, stability=0.0, behavior_signature=sig)
    queue = [first, second]

    def fake_eval(*args, **kwargs):
        if not queue:
            return Candidate(expr="fallback", score=2.0, novelty=0.0, stability=0.0, behavior_signature="b" * 64)
        out = queue.pop(0)
        return type("R", (), {"avg_bins_used": out.score, "avg_gap_ratio": 0.0, "behavior_signature": out.behavior_signature, "per_instance": []})

    import funsearch_lite.evolution as evolution_module

    original_eval = evolution_module.evaluate_candidate
    evolution_module.evaluate_candidate = fake_eval
    evo._estimate_local_stability = lambda expr, score: 0.0  # type: ignore[method-assign]
    try:
        c1 = evo._evaluate_expr("item", stage="evolve", generation=1, island_idx=0, population_slot=0, attempt=0, source="mutation")
        c2 = evo._evaluate_expr("after", stage="evolve", generation=1, island_idx=0, population_slot=1, attempt=1, source="mutation")
    finally:
        evolution_module.evaluate_candidate = original_eval

    assert c1 is not None
    assert c2 is None


def test_anneal_caps_increase_towards_late_generations():
    cfg = SearchConfig(
        generations=10,
        behavior_eval_cap=1,
        behavior_eval_cap_final=3,
        behavior_repeat_cap=1,
        behavior_repeat_cap_final=2,
        anneal_enable=True,
        verbose=False,
    )
    evo = IslandEvolution(config=cfg, instances=[Instance(name="s", capacity=1.0, items=[0.5, 0.5], optimal_bins=1)], capacity=1.0)

    early_eval, early_rep = evo._effective_behavior_caps(1)
    late_eval, late_rep = evo._effective_behavior_caps(10)

    assert early_eval == 1
    assert early_rep == 1
    assert late_eval == 3
    assert late_rep == 2


def test_anneal_reduces_novelty_weight_late():
    cfg = SearchConfig(generations=10, novelty_weight_final=0.2, stability_weight_final=1.0, anneal_enable=True, verbose=False)
    evo = IslandEvolution(config=cfg, instances=[Instance(name="s", capacity=1.0, items=[0.5, 0.5], optimal_bins=1)], capacity=1.0)
    c = Candidate(expr="x", score=1.0, novelty=0.5, stability=0.5, behavior_signature="sig")

    early = evo._ranking_key(c, generation=1)
    late = evo._ranking_key(c, generation=10)

    # Later generations should weaken novelty tie-break influence.
    assert late[1] > early[1]
