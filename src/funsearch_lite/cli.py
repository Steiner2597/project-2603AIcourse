from __future__ import annotations

import csv
from dataclasses import replace
from datetime import datetime
import json
from pathlib import Path
import typer

from .config import ExperimentConfig, SearchConfig
from .compare import generate_comparison
from .datasets import list_orlib_sources
from .experiment import run_experiment
from .llm_client import LLMHeuristicClient, load_model_env


def _model_slug(model: str) -> str:
    raw = (model or "model").strip().lower()
    aliases = {
        "deepseek-chat": "ds-chat",
        "deepseek-reasoner": "ds-reasoner",
        "gpt-5-nano": "gpt5nano",
        "gpt-5-mini": "gpt5mini",
    }
    if raw in aliases:
        return aliases[raw]
    cleaned = "".join(ch for ch in raw if ch.isalnum())
    return cleaned or "model"


def main(
    api: str = typer.Option("none", "--api", "-a", help="none|gpt|ds"),
    gen_provider: str = typer.Option("", "--gen-provider", help="Provider for generation stage: gpt|ds (default follows --api)"),
    ref_provider: str = typer.Option("", "--ref-provider", help="Provider for refinement stage: gpt|ds (default follows --api)"),
    ds_dual_model: bool = typer.Option(False, "--ds-dual-model", help="Use DeepSeek dual-model collaboration: deepseek-chat for generate + deepseek-reasoner for refine"),
    demo: bool = typer.Option(False, "--demo", help="Run without API usage"),
    dataset: str = typer.Option("synthetic", "--dataset", "-d", help="synthetic|orlib"),
        size: str = typer.Option("small", "--size", "-s", help="small/medium/large (ignored for orlib; all binpack1-8 will run)"),
    generations: int = typer.Option(30, "--generations", "-g", min=1),
    population: int = typer.Option(48, "--population", "-p", min=1),
    islands: int = typer.Option(4, "--islands", "-i", min=1),
    seed: int = typer.Option(42, "--seed"),
    compare: bool = typer.Option(False, "--compare", help="Generate FF/BF/Ours comparison table"),
    host_url: str = typer.Option("", "--host-url", help="Model gateway host or base URL, supports HOST_URL style"),
    gen_model_override: str = typer.Option("", "--gen-model", help="Override generator model"),
    ref_model_override: str = typer.Option("", "--ref-model", help="Override refiner model"),
    llm_seeds: int = typer.Option(4, "--llm-seeds", min=0, help="LLM proposals per generation stage"),
    llm_topk: int = typer.Option(3, "--llm-topk", min=1, help="Top-K elites sent to refiner"),
    log_interval: int = typer.Option(1, "--log-interval", min=1, help="Print progress every N generations"),
    quiet: bool = typer.Option(False, "--quiet", help="Disable generation progress logs"),
    behavior_repeat_cap: int = typer.Option(2, "--behavior-repeat-cap", min=1, help="Max repeated behavior signatures per island"),
    behavior_eval_cap: int = typer.Option(3, "--behavior-eval-cap", min=1, help="Max accepted repeats of same behavior per generation and island"),
    behavior_signature_points: int = typer.Option(120, "--behavior-signature-points", min=20, max=400, help="Sample points used to build behavior signature from full trajectory"),
    oversample_ratio: float = typer.Option(0.35, "--oversample-ratio", min=0.0, max=1.0, help="Extra candidate pool ratio before diversity selection"),
    restart_interval: int = typer.Option(1, "--restart-interval", min=1, help="Inject fresh random candidates every N generations per island"),
    restart_ratio: float = typer.Option(0.15, "--restart-ratio", min=0.0, max=0.8, help="Fraction of population replaced by fresh random candidates at restart"),
    stagnation_window: int = typer.Option(2, "--stagnation-window", min=2, help="Generations to detect unchanged best score"),
    stagnation_score_anchor: float = typer.Option(1567.0, "--stagnation-score-anchor", help="Anchor score used to detect plateau zone"),
    stagnation_ratio_threshold: float = typer.Option(0.35, "--stagnation-ratio-threshold", min=0.1, max=0.95, help="Plateau score ratio threshold to trigger exploration boost"),
    stagnation_restart_boost: float = typer.Option(1.8, "--stagnation-restart-boost", min=1.0, max=4.0, help="Multiplier for restart ratio during stagnation"),
    stagnation_llm_boost: int = typer.Option(1, "--stagnation-llm-boost", min=0, max=4, help="Additional LLM seeds during stagnation"),
    anneal: bool = typer.Option(True, "--anneal/--no-anneal", help="Enable annealing schedule for ranking and dedup caps"),
    novelty_weight_final: float = typer.Option(0.2, "--novelty-weight-final", min=0.0, max=1.0, help="Final novelty weight at late generations"),
    stability_weight_final: float = typer.Option(1.0, "--stability-weight-final", min=0.0, max=2.0, help="Final stability weight at late generations"),
    behavior_eval_cap_final: int = typer.Option(3, "--behavior-eval-cap-final", min=1, help="Final eval-stage behavior cap at late generations"),
    behavior_repeat_cap_final: int = typer.Option(2, "--behavior-repeat-cap-final", min=1, help="Final selection-stage behavior cap at late generations"),
    local_topk: int = typer.Option(2, "--local-topk", min=1, help="Top-K elites for local-search post refinement"),
    local_steps: int = typer.Option(2, "--local-steps", min=1, help="Perturbation steps per elite in local search"),
    orlib_mode: str = typer.Option("combined", "--orlib-mode", help="OR-Library mode: combined|per-source"),
    resume_run_dir: str = typer.Option("", "--resume-run-dir", help="Resume from an existing run directory that contains checkpoints"),
) -> None:
    provider = "none" if demo else api.lower()
    gen_provider_norm = (gen_provider or "").strip().lower()
    ref_provider_norm = (ref_provider or "").strip().lower()
    if gen_provider_norm and gen_provider_norm not in {"gpt", "ds"}:
        raise typer.BadParameter("--gen-provider must be one of: gpt, ds")
    if ref_provider_norm and ref_provider_norm not in {"gpt", "ds"}:
        raise typer.BadParameter("--ref-provider must be one of: gpt, ds")

    # Default role providers follow --api unless explicitly overridden.
    role_gen_provider = gen_provider_norm or provider
    role_ref_provider = ref_provider_norm or provider

    # Optional shortcut for DeepSeek dual-model collaboration.
    if ds_dual_model:
        role_gen_provider = "ds"
        role_ref_provider = "ds"

    run_provider_tag = provider if provider in {"gpt", "ds", "none"} else "none"

    search_cfg = SearchConfig(
        generations=generations,
        population_size=population,
        islands=islands,
        random_seed=seed,
        llm_seed_per_generation=llm_seeds,
        llm_refine_top_k=llm_topk,
        verbose=not quiet,
        log_interval=log_interval,
        behavior_repeat_cap=behavior_repeat_cap,
        behavior_eval_cap=behavior_eval_cap,
        behavior_signature_points=behavior_signature_points,
        oversample_ratio=oversample_ratio,
        restart_interval=restart_interval,
        restart_inject_ratio=restart_ratio,
        stagnation_window=stagnation_window,
        stagnation_score_anchor=stagnation_score_anchor,
        stagnation_ratio_threshold=stagnation_ratio_threshold,
        stagnation_restart_boost=stagnation_restart_boost,
        stagnation_llm_boost=stagnation_llm_boost,
        anneal_enable=anneal,
        novelty_weight_final=novelty_weight_final,
        stability_weight_final=stability_weight_final,
        behavior_eval_cap_final=behavior_eval_cap_final,
        behavior_repeat_cap_final=behavior_repeat_cap_final,
        local_search_top_k=local_topk,
        local_search_steps=local_steps,
    )

    llm_client = None
    role_gen_model = ""
    role_ref_model = ""
    use_llm = role_gen_provider in {"gpt", "ds"} or role_ref_provider in {"gpt", "ds"}
    if use_llm:
        # Pull env per role so exploration/refinement can use different providers.
        key, base, gen_model, ref_model = load_model_env(provider if provider in {"gpt", "ds"} else "gpt")

        gen_key = ""
        gen_base = ""
        role_gen_model = gen_model
        if role_gen_provider in {"gpt", "ds"}:
            gen_key, gen_base, role_gen_model, _ = load_model_env(role_gen_provider)

        ref_key = ""
        ref_base = ""
        role_ref_model = ref_model
        if role_ref_provider in {"gpt", "ds"}:
            ref_key, ref_base, _, role_ref_model = load_model_env(role_ref_provider)

        if ds_dual_model:
            role_gen_model = "deepseek-chat"
            role_ref_model = "deepseek-reasoner"

        if host_url:
            base = host_url
            if not base.rstrip("/").endswith("/v1"):
                base = base.rstrip("/") + "/v1"
            # Keep explicit host override behavior for both roles.
            gen_base = base
            ref_base = base
        if gen_model_override:
            role_gen_model = gen_model_override
        if ref_model_override:
            role_ref_model = ref_model_override
        if role_gen_provider in {"gpt", "ds"} and not gen_key:
            raise typer.BadParameter(
                f"Missing API key for generation provider '{role_gen_provider}'. Please set corresponding env key in .env / 作业要求/.env"
            )
        if role_ref_provider in {"gpt", "ds"} and not ref_key:
            raise typer.BadParameter(
                f"Missing API key for refinement provider '{role_ref_provider}'. Please set corresponding env key in .env / 作业要求/.env"
            )
        # Backward compatibility: if role-specific providers are not used, keep single-provider message.
        if provider in {"gpt", "ds"} and not key and not (gen_key or ref_key):
            raise typer.BadParameter(
                "Missing API key. Please set OPENAI_API_KEY or DEEPSEEK_API_KEY in .env / 作业要求/.env"
            )
        llm_client = LLMHeuristicClient(
            api_key=key or gen_key or ref_key,
            base_url=base or gen_base or ref_base,
            generator_model=role_gen_model,
            refiner_model=role_ref_model,
            generator_provider=role_gen_provider if role_gen_provider in {"gpt", "ds"} else None,
            refiner_provider=role_ref_provider if role_ref_provider in {"gpt", "ds"} else None,
            generator_api_key=gen_key or None,
            generator_base_url=gen_base or None,
            refiner_api_key=ref_key or None,
            refiner_base_url=ref_base or None,
            verbose=not quiet,
        )

    # Always reflect concrete model names in run naming for easier experiment traceability.
    if use_llm:
        gen_tag = _model_slug(role_gen_model)
        ref_tag = _model_slug(role_ref_model)
        run_provider_tag = gen_tag if gen_tag == ref_tag else f"{gen_tag}+{ref_tag}"

    exp_cfg = ExperimentConfig(dataset=dataset, size=size, provider_tag=run_provider_tag)
    resume_dir = (resume_run_dir or "").strip()
    mode = (orlib_mode or "combined").strip().lower()
    if resume_dir and mode == "per-source":
        raise typer.BadParameter("--resume-run-dir is not supported with --orlib-mode per-source")

    if exp_cfg.dataset == "orlib" and mode == "per-source":
        result = _run_orlib_per_source(
            exp_cfg=exp_cfg,
            search_cfg=search_cfg,
            llm_client=llm_client,
            with_compare=compare,
        )
        payload = {
            "run_dir": result["run_dir"],
            "mode": "per-source",
            "subrun_count": result["subrun_count"],
            "aggregate_json": result["aggregate_json"],
            "aggregate_md": result["aggregate_md"],
            "aggregate_csv": result["aggregate_csv"],
        }
    elif compare:
        result = generate_comparison(exp_cfg, search_cfg, llm_client=llm_client, resume_run_dir=resume_dir or None)
        payload = {
            "run_dir": result["run_dir"],
            "best_score": result["best_score"],
            "best_expression": result["best_expression"],
            "comparison_markdown": result["comparison_markdown"],
            "comparison_csv": result["comparison_csv"],
            "comparison_rows": result["comparison_rows"],
        }
    else:
        result = run_experiment(exp_cfg, search_cfg, llm_client=llm_client, resume_run_dir=resume_dir or None)
        payload = {
            "run_dir": result["run_dir"],
            "best_score": result["best_score"],
            "best_expression": result["best_expression"],
        }

    typer.echo(json.dumps(payload, ensure_ascii=False, indent=2))


def _run_orlib_per_source(
    exp_cfg: ExperimentConfig,
    search_cfg: SearchConfig,
    llm_client,
    with_compare: bool,
) -> dict:
    provider_tag = (exp_cfg.provider_tag or "none").lower()
    ts = datetime.now().strftime("%y%m%d%H%M%S")
    parent_dir = Path(exp_cfg.output_dir) / f"{ts}_parts_{provider_tag}_seed{search_cfg.random_seed}"
    subruns_root = parent_dir / "subruns"
    subruns_root.mkdir(parents=True, exist_ok=True)

    sources = list_orlib_sources("data/orlib")
    if not sources:
        raise typer.BadParameter("No OR-Library sources found under data/orlib")

    rows: list[dict] = []
    for source in sources:
        typer.echo(f"[per-source] running {source} ...")
        child_exp = replace(
            exp_cfg,
            dataset="orlib",
            orlib_source=source,
            output_dir=str(subruns_root),
        )
        child_result = generate_comparison(child_exp, search_cfg, llm_client=llm_client) if with_compare else run_experiment(child_exp, search_cfg, llm_client=llm_client)
        metrics_fp = Path(child_result["run_dir"]) / "metrics.json"
        metrics = json.loads(metrics_fp.read_text(encoding="utf-8"))
        eval_block = metrics.get("evaluation", {})
        base = eval_block.get("baselines", {})
        rows.append(
            {
                "source": source,
                "run_dir": child_result["run_dir"],
                "best_score": child_result.get("best_score", metrics.get("best_score")),
                "best_expression": child_result.get("best_expression", metrics.get("best_expression", "")),
                "avg_bins": eval_block.get("avg_bins_used"),
                "avg_gap": eval_block.get("avg_gap"),
                "avg_gap_ratio": eval_block.get("avg_gap_ratio"),
                "ff_avg_gap_ratio": (base.get("ff") or {}).get("avg_gap_ratio"),
                "bf_avg_gap_ratio": (base.get("bf") or {}).get("avg_gap_ratio"),
                "instances": (metrics.get("instances") or {}).get("count", 0),
            }
        )

    agg = _build_aggregate(rows)
    agg_payload = {
        "mode": "orlib_per_source",
        "parent_run_dir": str(parent_dir),
        "subrun_count": len(rows),
        "rows": rows,
        "overall": agg,
    }

    agg_json = parent_dir / "aggregate_summary.json"
    agg_md = parent_dir / "aggregate_summary.md"
    agg_csv = parent_dir / "aggregate_summary.csv"
    agg_json.write_text(json.dumps(agg_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_aggregate_markdown(agg_payload, agg_md)
    _write_aggregate_csv(rows, agg_csv)

    return {
        "run_dir": str(parent_dir),
        "subrun_count": len(rows),
        "aggregate_json": str(agg_json),
        "aggregate_md": str(agg_md),
        "aggregate_csv": str(agg_csv),
    }


def _build_aggregate(rows: list[dict]) -> dict:
    if not rows:
        return {}
    total_n = sum(int(r.get("instances") or 0) for r in rows)
    weight_sum = float(total_n) if total_n > 0 else float(len(rows))

    def _wavg(key: str) -> float | None:
        num = 0.0
        den = 0.0
        for r in rows:
            v = r.get(key)
            if not isinstance(v, (int, float)):
                continue
            w = float(r.get("instances") or 1)
            num += float(v) * w
            den += w
        if den <= 0:
            return None
        return num / den

    return {
        "instances": total_n,
        "avg_bins": _wavg("avg_bins"),
        "avg_gap": _wavg("avg_gap"),
        "avg_gap_ratio": _wavg("avg_gap_ratio"),
        "ff_avg_gap_ratio": _wavg("ff_avg_gap_ratio"),
        "bf_avg_gap_ratio": _wavg("bf_avg_gap_ratio"),
        "weight_sum": weight_sum,
    }


def _write_aggregate_csv(rows: list[dict], out_path: Path) -> None:
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "source",
            "instances",
            "avg_bins",
            "avg_gap",
            "avg_gap_ratio",
            "ff_avg_gap_ratio",
            "bf_avg_gap_ratio",
            "best_score",
            "run_dir",
        ])
        for r in sorted(rows, key=lambda x: x.get("source", "")):
            writer.writerow(
                [
                    r.get("source", ""),
                    r.get("instances", 0),
                    r.get("avg_bins", ""),
                    r.get("avg_gap", ""),
                    r.get("avg_gap_ratio", ""),
                    r.get("ff_avg_gap_ratio", ""),
                    r.get("bf_avg_gap_ratio", ""),
                    r.get("best_score", ""),
                    r.get("run_dir", ""),
                ]
            )


def _write_aggregate_markdown(payload: dict, out_path: Path) -> None:
    rows = sorted(payload.get("rows", []), key=lambda x: x.get("source", ""))
    overall = payload.get("overall", {})
    lines: list[str] = []
    lines.append("# OR-Library Per-Source Aggregate Summary")
    lines.append("")
    lines.append(f"- parent_run_dir: {payload.get('parent_run_dir', '')}")
    lines.append(f"- subrun_count: {payload.get('subrun_count', 0)}")
    lines.append("")
    lines.append("## Per Source")
    lines.append("")
    lines.append("| source | instances | avg_gap_ratio | FF gap_ratio | BF gap_ratio | best_score |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for r in rows:
        lines.append(
            "| {source} | {instances} | {avg_gap_ratio:.6f} | {ff:.6f} | {bf:.6f} | {best:.6f} |".format(
                source=r.get("source", ""),
                instances=int(r.get("instances") or 0),
                avg_gap_ratio=float(r.get("avg_gap_ratio") or 0.0),
                ff=float(r.get("ff_avg_gap_ratio") or 0.0),
                bf=float(r.get("bf_avg_gap_ratio") or 0.0),
                best=float(r.get("best_score") or 0.0),
            )
        )
    lines.append("")
    lines.append("## Overall (instance-weighted)")
    lines.append("")
    lines.append("| metric | value |")
    lines.append("|---|---:|")
    for key in ["instances", "avg_bins", "avg_gap", "avg_gap_ratio", "ff_avg_gap_ratio", "bf_avg_gap_ratio"]:
        val = overall.get(key)
        if isinstance(val, float):
            text = f"{val:.6f}"
        else:
            text = str(val)
        lines.append(f"| {key} | {text} |")
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


app = typer.Typer(help="FunSearch-Lite CLI")
app.command(name="run")(main)


def run() -> None:
    typer.run(main)


if __name__ == "__main__":
    run()
