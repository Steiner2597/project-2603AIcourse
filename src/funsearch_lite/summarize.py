from __future__ import annotations

from collections import defaultdict
from datetime import datetime
import json
from pathlib import Path

import matplotlib.pyplot as plt
import typer

from .datasets import generate_synthetic_instances, load_orlib_instances
from .evaluator import evaluate_candidate
from .heuristic_expr import build_scorer


app = typer.Typer(help="Summarize checkpoint events for a run directory")


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def _latest_run_dir(runs_root: Path) -> Path:
    dirs = [p for p in runs_root.iterdir() if p.is_dir()]
    if not dirs:
        raise FileNotFoundError(f"No run directories found in {runs_root}")
    dirs.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return dirs[0]


def summarize_run(run_dir: Path) -> dict:
    ck = run_dir / "checkpoints"
    eval_events = _read_jsonl(ck / "eval_events.jsonl")
    req_events = _read_jsonl(ck / "requests.jsonl")

    by_gen_island: dict[tuple[int, int], dict] = defaultdict(
        lambda: {
            "total_eval_events": 0,
            "accepted": 0,
            "dedup_expr_hit": 0,
            "error": 0,
            "avg_score_accepted": None,
            "llm_requests": 0,
            "llm_errors": 0,
            "llm_avg_elapsed_sec": None,
        }
    )
    score_buckets: dict[tuple[int, int], list[float]] = defaultdict(list)
    llm_elapsed: dict[tuple[int, int], list[float]] = defaultdict(list)

    for e in eval_events:
        g = int(e.get("generation", 0))
        i = int(e.get("island", -1))
        key = (g, i)
        row = by_gen_island[key]
        row["total_eval_events"] += 1
        status = e.get("status", "")
        if status == "accepted":
            row["accepted"] += 1
            if isinstance(e.get("score"), (int, float)):
                score_buckets[key].append(float(e["score"]))
        elif status == "dedup_expr_hit":
            row["dedup_expr_hit"] += 1
        elif status == "error":
            row["error"] += 1

    for e in req_events:
        g = int(e.get("generation", 0))
        i = int(e.get("island", -1))
        key = (g, i)
        row = by_gen_island[key]
        event = e.get("event", "")
        if event == "llm_request_start":
            row["llm_requests"] += 1
        elif event == "llm_request_error":
            row["llm_errors"] += 1
        elif event == "llm_request_done" and isinstance(e.get("elapsed_sec"), (int, float)):
            llm_elapsed[key].append(float(e["elapsed_sec"]))

    table: list[dict] = []
    for key in sorted(by_gen_island.keys()):
        g, i = key
        row = by_gen_island[key]
        scores = score_buckets.get(key, [])
        if scores:
            row["avg_score_accepted"] = sum(scores) / len(scores)
        elapsed = llm_elapsed.get(key, [])
        if elapsed:
            row["llm_avg_elapsed_sec"] = sum(elapsed) / len(elapsed)
        table.append(
            {
                "generation": g,
                "island": i,
                **row,
            }
        )

    total = {
        "eval_events": len(eval_events),
        "llm_events": len(req_events),
        "accepted": sum(1 for x in eval_events if x.get("status") == "accepted"),
        "dedup_expr_hit": sum(1 for x in eval_events if x.get("status") == "dedup_expr_hit"),
        "eval_errors": sum(1 for x in eval_events if x.get("status") == "error"),
        "llm_request_start": sum(1 for x in req_events if x.get("event") == "llm_request_start"),
        "llm_request_done": sum(1 for x in req_events if x.get("event") == "llm_request_done"),
        "llm_request_error": sum(1 for x in req_events if x.get("event") == "llm_request_error"),
    }

    baseline = _baseline_comparison(run_dir)

    score_unit = "raw"
    metrics_fp = run_dir / "metrics.json"
    if metrics_fp.exists():
        try:
            metrics = json.loads(metrics_fp.read_text(encoding="utf-8"))
            if (metrics.get("evaluation") or {}).get("avg_gap_ratio") is not None:
                score_unit = "ratio"
        except Exception:
            score_unit = "raw"

    return {
        "run_dir": str(run_dir),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "score_unit": score_unit,
        "total": total,
        "by_generation_island": table,
        "baseline_comparison": baseline,
    }


def write_summary_files(run_dir: Path) -> dict:
    summary = summarize_run(run_dir)
    out_json = run_dir / "summary.json"
    out_md = run_dir / "summary.md"
    out_chart = run_dir / "baseline_compare.png"
    out_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md.write_text(_to_markdown(summary), encoding="utf-8")
    _save_baseline_chart(summary["baseline_comparison"], out_chart)
    return {
        "summary": summary,
        "summary_json": str(out_json),
        "summary_md": str(out_md),
        "baseline_chart": str(out_chart),
    }


def _to_markdown(summary: dict) -> str:
    lines: list[str] = []
    lines.append("# Checkpoint Summary")
    lines.append("")
    lines.append(f"- run_dir: {summary['run_dir']}")
    lines.append(f"- generated_at: {summary['generated_at']}")
    lines.append("")

    total = summary["total"]
    lines.append("## Overall")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---:|")
    for k in [
        "eval_events",
        "accepted",
        "dedup_expr_hit",
        "eval_errors",
        "llm_events",
        "llm_request_start",
        "llm_request_done",
        "llm_request_error",
    ]:
        lines.append(f"| {k} | {total.get(k, 0)} |")

    lines.append("")
    lines.append("## By Generation/Island")
    lines.append("")
    is_ratio = summary.get("score_unit") == "ratio"
    lines.append(
        "| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |"
    )
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for r in summary["by_generation_island"]:
        if r["avg_score_accepted"] is None:
            score = ""
        elif is_ratio:
            score = f"{r['avg_score_accepted'] * 100.0:.3f}%"
        else:
            score = f"{r['avg_score_accepted']:.6f}"
        ltm = "" if r["llm_avg_elapsed_sec"] is None else f"{r['llm_avg_elapsed_sec']:.3f}"
        lines.append(
            "| {generation} | {island} | {total_eval_events} | {accepted} | {dedup_expr_hit} | {error} | {score} | {llm_requests} | {llm_errors} | {ltm} |".format(
                generation=r["generation"],
                island=r["island"],
                total_eval_events=r["total_eval_events"],
                accepted=r["accepted"],
                dedup_expr_hit=r["dedup_expr_hit"],
                error=r["error"],
                score=score,
                llm_requests=r["llm_requests"],
                llm_errors=r["llm_errors"],
                ltm=ltm,
            )
        )
    lines.append("")

    base = summary.get("baseline_comparison") or {}
    rows = base.get("rows") or []
    if rows:
        lines.append("## Baseline Comparison")
        lines.append("")
        lines.append("| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|")
        for r in rows:
            lines.append(
                "| {method} | {avg_bins:.4f} | {gap_pct:.2f} | {delta_bf:.2f} | {delta_ff:.2f} | {imp_bf:.2f} | {imp_ff:.2f} |".format(
                    method=r["method"],
                    avg_bins=r["avg_bins"],
                    gap_pct=r["gap_pct"],
                    delta_bf=r.get("delta_vs_bf_pp", 0.0),
                    delta_ff=r.get("delta_vs_ff_pp", 0.0),
                    imp_bf=r.get("rel_improve_vs_bf_pct", 0.0),
                    imp_ff=r.get("rel_improve_vs_ff_pct", 0.0),
                )
            )
        lines.append("")
        lines.append(f"- winner: {base.get('winner', 'N/A')}")
        lines.append(f"- chart: baseline_compare.png")
        lines.append("")

    return "\n".join(lines)


def _baseline_comparison(run_dir: Path) -> dict:
    metrics_fp = run_dir / "metrics.json"
    if not metrics_fp.exists():
        return {"rows": [], "winner": "N/A"}

    metrics = json.loads(metrics_fp.read_text(encoding="utf-8"))
    exp = metrics.get("experiment_config", {})
    cfg = metrics.get("search_config", {})
    best_expr = metrics.get("best_expression", "")

    dataset = exp.get("dataset", "synthetic")
    size = exp.get("size", "small")
    seed = int(cfg.get("random_seed", 42))

    if dataset == "orlib":
            source = exp.get("orlib_source")
            if not source:
                binpacks_dir = run_dir / "binpacks"
                if binpacks_dir.exists():
                    sources = sorted([p.name for p in binpacks_dir.iterdir() if p.is_dir()])
                    if len(sources) == 1:
                        source = sources[0]
            instances = load_orlib_instances("data/orlib", source=source)
    else:
        instances = generate_synthetic_instances(size=size, seed=seed)

    ff_res = evaluate_candidate(instances, lambda _: 0.0)
    bf_res = evaluate_candidate(instances, build_scorer("-after"))
    ours_res = evaluate_candidate(instances, build_scorer(best_expr))

    def _score(res):
        return res.avg_gap_ratio if res.avg_gap_ratio is not None else res.avg_bins_used

    rows = [
        {"method": "First-Fit (FF)", "avg_bins": ff_res.avg_bins_used, "gap_ratio": ff_res.avg_gap_ratio, "score": _score(ff_res)},
        {"method": "Best-Fit (BF)", "avg_bins": bf_res.avg_bins_used, "gap_ratio": bf_res.avg_gap_ratio, "score": _score(bf_res)},
        {"method": "FunSearch-Lite (Ours)", "avg_bins": ours_res.avg_bins_used, "gap_ratio": ours_res.avg_gap_ratio, "score": _score(ours_res)},
    ]
    rows.sort(key=lambda x: x["score"])
    for r in rows:
        gap_pct = r["gap_ratio"] * 100.0 if r.get("gap_ratio") is not None else None
        r["gap_pct"] = gap_pct

    ff_gap = next((r["gap_pct"] for r in rows if r["method"] == "First-Fit (FF)"), None)
    bf_gap = next((r["gap_pct"] for r in rows if r["method"] == "Best-Fit (BF)"), None)
    if ff_gap is not None and bf_gap is not None:
        for r in rows:
            g = r.get("gap_pct")
            if g is None:
                r["delta_vs_bf_pp"] = 0.0
                r["delta_vs_ff_pp"] = 0.0
                r["rel_improve_vs_bf_pct"] = 0.0
                r["rel_improve_vs_ff_pct"] = 0.0
                continue
            delta_bf = bf_gap - g
            delta_ff = ff_gap - g
            r["delta_vs_bf_pp"] = delta_bf
            r["delta_vs_ff_pp"] = delta_ff
            r["rel_improve_vs_bf_pct"] = (delta_bf / bf_gap * 100.0) if abs(bf_gap) > 1e-12 else 0.0
            r["rel_improve_vs_ff_pct"] = (delta_ff / ff_gap * 100.0) if abs(ff_gap) > 1e-12 else 0.0
    winner = rows[0]["method"]
    return {"rows": rows, "winner": winner}


def _save_baseline_chart(baseline: dict, out_path: Path) -> None:
    rows = baseline.get("rows") or []
    if not rows:
        return
    methods = [r["method"] for r in rows]
    values = [r.get("gap_pct") if r.get("gap_pct") is not None else r["avg_bins"] for r in rows]

    plt.figure(figsize=(8, 4.5))
    bars = plt.bar(methods, values)
    plt.title("Baseline Comparison (Lower is Better)")
    ylabel = "Gap to optimum (%)" if any(r.get("gap_pct") is not None for r in rows) else "Average bins used"
    plt.ylabel(ylabel)
    plt.grid(axis="y", alpha=0.25)
    min_v = min(values)
    max_v = max(values)
    margin = max(1.0, (max_v - min_v) * 0.25)
    plt.ylim(min_v - margin, max_v + margin)
    for b, v in zip(bars, values):
        plt.text(b.get_x() + b.get_width() / 2.0, v, f"{v:.2f}", ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig(out_path, dpi=140)
    plt.close()


@app.command()
def main(
    run_dir: str = typer.Option("", "--run-dir", help="Path to run directory; default is latest under runs/"),
    runs_root: str = typer.Option("runs", "--runs-root", help="Runs root directory"),
) -> None:
    root = Path(runs_root)
    target = Path(run_dir) if run_dir else _latest_run_dir(root)
    result = write_summary_files(target)
    summary = result["summary"]

    typer.echo(
        json.dumps(
            {
                "run_dir": str(target),
                "summary_json": result["summary_json"],
                "summary_md": result["summary_md"],
                "baseline_chart": result["baseline_chart"],
                "overall": summary["total"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def run() -> None:
    app()


if __name__ == "__main__":
    run()
