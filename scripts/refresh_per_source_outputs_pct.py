from __future__ import annotations

import csv
import json
from pathlib import Path

from funsearch_lite.datasets import generate_synthetic_instances, load_orlib_instances
from funsearch_lite.evaluator import evaluate_candidate
from funsearch_lite.heuristic_expr import build_scorer
from funsearch_lite.summarize import write_summary_files
from funsearch_lite.visualize import save_curve

PARENTS = [
    Path("runs/260325122745_or_parts_ds"),
    Path("runs/260325122756_or_parts_ds"),
    Path("runs/260325122809_or_parts_ds"),
]


def _score(res) -> float:
    return res.avg_gap_ratio if res.avg_gap_ratio is not None else res.avg_bins_used


def _infer_orlib_source(run_dir: Path) -> str | None:
    b = run_dir / "binpacks"
    if not b.exists():
        return None
    candidates = sorted([p.name for p in b.iterdir() if p.is_dir()])
    if len(candidates) == 1:
        return candidates[0]
    return None


def _prepare_instances(metrics: dict, run_dir: Path):
    exp = metrics.get("experiment_config", {})
    cfg = metrics.get("search_config", {})
    dataset = exp.get("dataset", "synthetic")
    size = exp.get("size", "small")
    seed = int(cfg.get("random_seed", 42))
    if dataset == "orlib":
        source = exp.get("orlib_source") or _infer_orlib_source(run_dir)
        return load_orlib_instances("data/orlib", source=source)
    return generate_synthetic_instances(size=size, seed=seed)


def _refresh_subrun(run_dir: Path) -> dict:
    metrics_fp = run_dir / "metrics.json"
    if not metrics_fp.exists():
        raise FileNotFoundError(f"metrics.json not found: {run_dir}")

    metrics = json.loads(metrics_fp.read_text(encoding="utf-8"))
    best_expr = metrics.get("best_expression", "")
    instances = _prepare_instances(metrics, run_dir)

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

    # summary.md / summary.json / baseline_compare.png
    write_summary_files(run_dir)

    # curve.png
    hist = metrics.get("history", {})
    save_curve(hist.get("best_per_gen", []), hist.get("avg_per_gen", []), run_dir / "curve.png")

    ev = metrics.get("evaluation", {})
    source = _infer_orlib_source(run_dir) or (ev.get("per_source_summary") or {}).keys()
    if isinstance(source, set):
        source = sorted(source)[0] if source else "unknown"
    if not isinstance(source, str):
        source = "unknown"

    ff_pct = ff_gap
    bf_pct = bf_gap
    ours_pct = ours_gap
    return {
        "source": source,
        "run_dir": str(run_dir),
        "best_score": metrics.get("best_score"),
        "best_score_pct": (float(metrics.get("best_score")) * 100.0) if isinstance(metrics.get("best_score"), (int, float)) else None,
        "best_expression": best_expr,
        "avg_bins": ev.get("avg_bins_used"),
        "avg_gap": ev.get("avg_gap"),
        "avg_gap_ratio": ev.get("avg_gap_ratio"),
        "avg_gap_pct": ours_pct,
        "ff_avg_gap_ratio": ff_res.avg_gap_ratio,
        "bf_avg_gap_ratio": bf_res.avg_gap_ratio,
        "ff_avg_gap_pct": ff_pct,
        "bf_avg_gap_pct": bf_pct,
        "delta_vs_bf_pp": bf_pct - ours_pct,
        "delta_vs_ff_pp": ff_pct - ours_pct,
        "rel_improve_vs_bf_pct": ((bf_pct - ours_pct) / bf_pct * 100.0) if abs(bf_pct) > 1e-12 else 0.0,
        "rel_improve_vs_ff_pct": ((ff_pct - ours_pct) / ff_pct * 100.0) if abs(ff_pct) > 1e-12 else 0.0,
        "instances": (metrics.get("instances") or {}).get("count", 0),
    }


def _rebuild_parent(parent: Path) -> None:
    subruns_dir = parent / "subruns"
    if not subruns_dir.exists():
        return

    rows = []
    for sub in sorted([p for p in subruns_dir.iterdir() if p.is_dir()]):
        rows.append(_refresh_subrun(sub))

    total_instances = sum(int(r.get("instances") or 0) for r in rows)

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

    overall = {
        "instances": total_instances,
        "avg_bins": _wavg("avg_bins"),
        "avg_gap": _wavg("avg_gap"),
        "avg_gap_ratio": _wavg("avg_gap_ratio"),
        "avg_gap_pct": _wavg("avg_gap_pct"),
        "ff_avg_gap_ratio": _wavg("ff_avg_gap_ratio"),
        "bf_avg_gap_ratio": _wavg("bf_avg_gap_ratio"),
        "ff_avg_gap_pct": _wavg("ff_avg_gap_pct"),
        "bf_avg_gap_pct": _wavg("bf_avg_gap_pct"),
    }
    if overall["avg_gap_pct"] is not None and overall["bf_avg_gap_pct"] is not None and overall["ff_avg_gap_pct"] is not None:
        overall["delta_vs_bf_pp"] = overall["bf_avg_gap_pct"] - overall["avg_gap_pct"]
        overall["delta_vs_ff_pp"] = overall["ff_avg_gap_pct"] - overall["avg_gap_pct"]
        overall["rel_improve_vs_bf_pct"] = (
            overall["delta_vs_bf_pp"] / overall["bf_avg_gap_pct"] * 100.0 if abs(overall["bf_avg_gap_pct"]) > 1e-12 else 0.0
        )
        overall["rel_improve_vs_ff_pct"] = (
            overall["delta_vs_ff_pp"] / overall["ff_avg_gap_pct"] * 100.0 if abs(overall["ff_avg_gap_pct"]) > 1e-12 else 0.0
        )

    payload = {
        "mode": "orlib_per_source",
        "parent_run_dir": str(parent),
        "subrun_count": len(rows),
        "rows": rows,
        "overall": overall,
    }

    (parent / "aggregate_summary.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    with (parent / "aggregate_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "source",
                "instances",
                "avg_bins",
                "avg_gap",
                "avg_gap_ratio",
                "avg_gap_pct",
                "ff_avg_gap_pct",
                "bf_avg_gap_pct",
                "delta_vs_bf_pp",
                "delta_vs_ff_pp",
                "rel_improve_vs_bf_pct",
                "rel_improve_vs_ff_pct",
                "best_score",
                "best_score_pct",
                "run_dir",
            ]
        )
        for r in sorted(rows, key=lambda x: x.get("source", "")):
            writer.writerow(
                [
                    r.get("source", ""),
                    r.get("instances", 0),
                    r.get("avg_bins", ""),
                    r.get("avg_gap", ""),
                    r.get("avg_gap_ratio", ""),
                    r.get("avg_gap_pct", ""),
                    r.get("ff_avg_gap_pct", ""),
                    r.get("bf_avg_gap_pct", ""),
                    r.get("delta_vs_bf_pp", ""),
                    r.get("delta_vs_ff_pp", ""),
                    r.get("rel_improve_vs_bf_pct", ""),
                    r.get("rel_improve_vs_ff_pct", ""),
                    r.get("best_score", ""),
                    r.get("best_score_pct", ""),
                    r.get("run_dir", ""),
                ]
            )

    md_lines = [
        "# OR-Library Per-Source Aggregate Summary",
        "",
        f"- parent_run_dir: {parent}",
        f"- subrun_count: {len(rows)}",
        "",
        "## Per Source",
        "",
        "| source | instances | avg_gap(%) | vs BF(pp) | vs FF(pp) | improve vs BF(%) | improve vs FF(%) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in sorted(rows, key=lambda x: x.get("source", "")):
        md_lines.append(
            f"| {r.get('source','')} | {int(r.get('instances') or 0)} | {float(r.get('avg_gap_pct') or 0.0):.2f} | {float(r.get('delta_vs_bf_pp') or 0.0):.2f} | {float(r.get('delta_vs_ff_pp') or 0.0):.2f} | {float(r.get('rel_improve_vs_bf_pct') or 0.0):.2f} | {float(r.get('rel_improve_vs_ff_pct') or 0.0):.2f} |"
        )

    md_lines.extend(
        [
            "",
            "## Overall (instance-weighted)",
            "",
            "| metric | value |",
            "|---|---:|",
        ]
    )
    for key in [
        "instances",
        "avg_bins",
        "avg_gap",
        "avg_gap_ratio",
        "avg_gap_pct",
        "ff_avg_gap_pct",
        "bf_avg_gap_pct",
        "delta_vs_bf_pp",
        "delta_vs_ff_pp",
        "rel_improve_vs_bf_pct",
        "rel_improve_vs_ff_pct",
    ]:
        val = overall.get(key)
        if isinstance(val, float):
            txt = f"{val:.6f}"
        else:
            txt = str(val)
        md_lines.append(f"| {key} | {txt} |")

    (parent / "aggregate_summary.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for p in PARENTS:
        _rebuild_parent(p)
        print(f"updated parent: {p}")
