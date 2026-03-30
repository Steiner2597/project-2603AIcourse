from __future__ import annotations

from dataclasses import dataclass
from dataclasses import asdict
import csv
from pathlib import Path

from .config import ExperimentConfig, SearchConfig
from .datasets import generate_synthetic_instances, load_orlib_instances
from .evaluator import evaluate_candidate
from .experiment import run_experiment
from .heuristic_expr import build_scorer


@dataclass(slots=True)
class CompareRow:
    method: str
    avg_bins: float
    gap_pct: float
    delta_vs_bf_pp: float
    delta_vs_ff_pp: float
    rel_improve_vs_bf_pct: float
    rel_improve_vs_ff_pct: float


def generate_comparison(
    exp_cfg: ExperimentConfig,
    search_cfg: SearchConfig,
    llm_client=None,
    resume_run_dir: str | Path | None = None,
) -> dict:
    run_result = run_experiment(exp_cfg=exp_cfg, search_cfg=search_cfg, llm_client=llm_client, resume_run_dir=resume_run_dir)
    run_dir = Path(run_result["run_dir"])

    instances = _prepare_instances(exp_cfg=exp_cfg, search_cfg=search_cfg)
    ff_res = evaluate_candidate(instances, _ff_scorer)
    bf_res = evaluate_candidate(instances, build_scorer("-after"))
    ours_res = evaluate_candidate(instances, build_scorer(run_result["best_expression"]))

    def _score(res):
        return res.avg_gap_ratio if res.avg_gap_ratio is not None else res.avg_bins_used

    ff_score = _score(ff_res)
    bf_score = _score(bf_res)
    ours_score = _score(ours_res)

    ff_gap = _gap_to_opt(ff_score)
    bf_gap = _gap_to_opt(bf_score)
    ours_gap = _gap_to_opt(ours_score)

    def _enrich(method: str, avg_bins: float, gap: float) -> CompareRow:
        delta_vs_bf = bf_gap - gap
        delta_vs_ff = ff_gap - gap
        rel_vs_bf = (delta_vs_bf / bf_gap * 100.0) if abs(bf_gap) > 1e-12 else 0.0
        rel_vs_ff = (delta_vs_ff / ff_gap * 100.0) if abs(ff_gap) > 1e-12 else 0.0
        return CompareRow(
            method=method,
            avg_bins=avg_bins,
            gap_pct=gap,
            delta_vs_bf_pp=delta_vs_bf,
            delta_vs_ff_pp=delta_vs_ff,
            rel_improve_vs_bf_pct=rel_vs_bf,
            rel_improve_vs_ff_pct=rel_vs_ff,
        )

    rows = [
        _enrich(method="First-Fit (FF)", avg_bins=ff_res.avg_bins_used, gap=ff_gap),
        _enrich(method="Best-Fit (BF)", avg_bins=bf_res.avg_bins_used, gap=bf_gap),
        _enrich(method="FunSearch-Lite (Ours)", avg_bins=ours_res.avg_bins_used, gap=ours_gap),
    ]
    rows.sort(key=lambda r: r.gap_pct)

    md_path = run_dir / "comparison_table.md"
    csv_path = run_dir / "comparison_table.csv"
    _write_markdown(rows, md_path)
    _write_csv(rows, csv_path)

    return {
        **run_result,
        "comparison_markdown": str(md_path),
        "comparison_csv": str(csv_path),
        "comparison_rows": [asdict(r) for r in rows],
    }


def _prepare_instances(exp_cfg: ExperimentConfig, search_cfg: SearchConfig) -> list[list[float]]:
    if exp_cfg.dataset == "orlib":
        instances = load_orlib_instances("data/orlib", source=exp_cfg.orlib_source or None)
        if instances:
            return instances
    return generate_synthetic_instances(exp_cfg.size, seed=search_cfg.random_seed)


def _ff_scorer(_: dict[str, float]) -> float:
    # All feasible bins have equal score, evaluator keeps the first feasible one.
    return 0.0


def _gap_to_opt(score: float) -> float:
    """Convert gap ratio (relative to optimum) to percentage."""
    return score * 100.0


def _write_markdown(rows: list[CompareRow], out_path: Path) -> None:
    lines = [
           "| Method | Avg Bins (Lower Better) | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r.method} | {r.avg_bins:.4f} | {r.gap_pct:.2f} | {r.delta_vs_bf_pp:.2f} | {r.delta_vs_ff_pp:.2f} | {r.rel_improve_vs_bf_pct:.2f} | {r.rel_improve_vs_ff_pct:.2f} |"
        )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_csv(rows: list[CompareRow], out_path: Path) -> None:
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "method",
                "avg_bins",
                "gap_to_opt_pct",
                "delta_vs_bf_pp",
                "delta_vs_ff_pp",
                "rel_improve_vs_bf_pct",
                "rel_improve_vs_ff_pct",
            ]
        )
        for r in rows:
            writer.writerow(
                [
                    r.method,
                    f"{r.avg_bins:.6f}",
                    f"{r.gap_pct:.4f}",
                    f"{r.delta_vs_bf_pp:.4f}",
                    f"{r.delta_vs_ff_pp:.4f}",
                    f"{r.rel_improve_vs_bf_pct:.4f}",
                    f"{r.rel_improve_vs_ff_pct:.4f}",
                ]
            )
