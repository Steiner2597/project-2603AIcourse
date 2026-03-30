from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ModelConfig:
    provider: str = "none"
    generator_model: str = "gpt-5-nano"
    refiner_model: str = "gpt-5-mini"
    api_key: str = ""
    base_url: str = ""


@dataclass(slots=True)
class SearchConfig:
    generations: int = 30
    population_size: int = 48
    islands: int = 4
    migration_interval: int = 5
    mutation_rate: float = 0.7
    crossover_rate: float = 0.2
    llm_seed_per_generation: int = 4
    llm_refine_top_k: int = 3
    random_seed: int = 42
    verbose: bool = True
    log_interval: int = 1
    behavior_repeat_cap: int = 2
    behavior_eval_cap: int = 3
    behavior_signature_points: int = 120
    oversample_ratio: float = 0.35
    restart_interval: int = 1
    restart_inject_ratio: float = 0.15
    stagnation_window: int = 2
    stagnation_score_anchor: float = 1567.0
    stagnation_ratio_threshold: float = 0.35
    stagnation_restart_boost: float = 1.8
    stagnation_llm_boost: int = 1
    anneal_enable: bool = True
    novelty_weight_final: float = 0.2
    stability_weight_final: float = 1.0
    behavior_eval_cap_final: int = 3
    behavior_repeat_cap_final: int = 2
    local_search_top_k: int = 2
    local_search_steps: int = 2


@dataclass(slots=True)
class ExperimentConfig:
    dataset: str = "synthetic"
    size: str = "small"
    bin_capacity: float = 1.0
    output_dir: str = "runs"
    provider_tag: str = "none"
    orlib_source: str = ""
