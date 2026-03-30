from __future__ import annotations

import csv
import json
from pathlib import Path

from funsearch_lite.datasets import generate_synthetic_instances, load_orlib_instances
from funsearch_lite.evaluator import evaluate_candidate
from funsearch_lite.heuristic_expr import build_scorer
from funsearch_lite.summarize import write_summary_files
from funsearch_lite.visualize import save_curve

RUNS = [
    Path("runs/260325115953_or_ds"),
    Path("runs/260325120006_or_ds"),
    Path("runs/260325120014_or_ds"),
]


def _score(res) -> float:
    return res.avg_gap_ratio if res.avg_gap_ratio is not None else res.avg_bins_used


def _prepare_instances(metrics: dict):
    exp = metrics.get("experiment_config", {})
    cfg = metrics.get("search_config", {})
    dataset = exp.get("dataset", "synthetic")
    size = exp.get("size", "small")
    seed = int(cfg.get("random_seed", 42))
    if dataset == "orlib":
        return load_orlib_instances("data/orlib")
    return generate_synthetic_instances(size=size, seed=seed)


def refresh_run(run_dir: Path) -> None:
    metrics = json.loads((run_dir / "metrics.json").read_text(encoding="utf-8"))
    best_expr = metrics.get("best_expression", "")
    instances = _prepare_instances(metrics)

    ff_res = evaluate_candidate(instances, lambda _: 0.0)
    bf_res = evaluate_candidate(instances, build_scorer("-after"))
    ours_res = evaluate_candidate(instances, build_scorer(best_expr))

    ff_gap = _score(ff_res) * 100.0
    bf_gap = _score(bf_res) * 100.0
    ours_gap = _score(ours_res) * 100.0

    rows = [
        ("First-Fit (FF)", ff_res.avg_bins_used, ff_gap),
        ("Best-Fit (BF)", bf_res.avg_bins_used, bf_gap),
        ("FunSearch-Lite (Ours)", ours_res.avg_bins_used, ours_gap),
    ]

    enriched = []
    for method, avg_bins, gap in rows:
        delta_vs_bf = bf_gap - gap
        delta_vs_ff = ff_gap - gap
        rel_vs_bf = (delta_vs_bf / bf_gap * 100.0) if abs(bf_gap) > 1e-12 else 0.0
        rel_vs_ff = (delta_vs_ff / ff_gap * 100.0) if abs(ff_gap) > 1e-12 else 0.0
        enriched.append((method, avg_bins, gap, delta_vs_bf, delta_vs_ff, rel_vs_bf, rel_vs_ff))

    enriched.sort(key=lambda x: x[2])

    md_fp = run_dir / "comparison_table.md"
    csv_fp = run_dir / "comparison_table.csv"

    md_lines = [
        "| Method | Avg Bins (Lower Better) | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in enriched:
        md_lines.append(
            f"| {r[0]} | {r[1]:.4f} | {r[2]:.2f} | {r[3]:.2f} | {r[4]:.2f} | {r[5]:.2f} | {r[6]:.2f} |"
        )
    md_fp.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    with csv_fp.open("w", newline="", encoding="utf-8") as f:
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
        for r in enriched:
            writer.writerow(
                [
                    r[0],
                    f"{r[1]:.6f}",
                    f"{r[2]:.4f}",
                    f"{r[3]:.4f}",
                    f"{r[4]:.4f}",
                    f"{r[5]:.4f}",
                    f"{r[6]:.4f}",
                ]
            )

    write_summary_files(run_dir)

    hist = metrics.get("history", {})
    save_curve(hist.get("best_per_gen", []), hist.get("avg_per_gen", []), run_dir / "curve.png")


if __name__ == "__main__":
    for run in RUNS:
        refresh_run(run)
        print(f"updated: {run}")
