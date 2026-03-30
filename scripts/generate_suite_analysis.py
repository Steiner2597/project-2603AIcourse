from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from statistics import mean, median, stdev
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _fmt(v: float | None, n: int = 4) -> str:
    if v is None:
        return "N/A"
    return f"{v:.{n}f}"


def _pct(v: float | None, n: int = 2) -> str:
    if v is None:
        return "N/A"
    return f"{v * 100:.{n}f}%"


def _safe_stdev(vals: list[float]) -> float:
    if len(vals) <= 1:
        return 0.0
    return stdev(vals)


def _parse_suite(suite_dir: Path) -> list[dict[str, Any]]:
    runs = []
    for run_dir in sorted(p for p in suite_dir.iterdir() if p.is_dir()):
        seed_report = run_dir / "seed_reports.json"
        metrics = run_dir / "metrics.json"
        status = run_dir / "status.json"
        if not (seed_report.exists() and metrics.exists() and status.exists()):
            continue

        sr = _read_json(seed_report)
        m = _read_json(metrics)
        st = _read_json(status)
        rows = sr.get("cost_totals", {}).get("default_4p0", {})

        in_cost_miss = float(rows.get("cost_input_miss_usd", 0.0) or 0.0)
        in_cost = float(rows.get("cost_input_usd", 0.0) or 0.0)
        out_cost = float(rows.get("cost_output_usd", 0.0) or 0.0)

        runs.append(
            {
                "run_name": sr.get("run_name", run_dir.name),
                "seed": sr.get("seed"),
                "gap_pct": float(sr.get("quality", {}).get("ours_gap_pct", 0.0) or 0.0),
                "best_score_ratio": float(sr.get("quality", {}).get("best_score_ratio", 0.0) or 0.0),
                "curve_improve_ratio": float(
                    sr.get("quality", {}).get("improve_ratio_first_to_last_best", 0.0) or 0.0
                ),
                "wall_sec": float(sr.get("wall_clock_sec", 0.0) or 0.0),
                "llm_sec": float(sr.get("llm_time", {}).get("sum_elapsed_sec", 0.0) or 0.0),
                "llm_req": int(sr.get("events", {}).get("llm_request_done", 0) or 0),
                "eval_events": int(sr.get("events", {}).get("total_eval_events", 0) or 0),
                "dedup_expr_hit": int(sr.get("events", {}).get("dedup_expr_hit", 0) or 0),
                "eval_errors": int(sr.get("events", {}).get("eval_errors", 0) or 0),
                "cost_input_usd": in_cost + in_cost_miss,
                "cost_output_usd": out_cost,
                "cost_total_usd": in_cost + in_cost_miss + out_cost,
                "history_best": [float(x) for x in m.get("history", {}).get("best_per_gen", [])],
                "history_avg": [float(x) for x in m.get("history", {}).get("avg_per_gen", [])],
                "status": st.get("status", "unknown"),
                "started_at": st.get("started_at"),
                "finished_at": st.get("finished_at"),
            }
        )
    return runs


def _gen_level_summary(runs: list[dict[str, Any]]) -> list[dict[str, float]]:
    max_len = max((len(r["history_best"]) for r in runs), default=0)
    out: list[dict[str, float]] = []
    for i in range(max_len):
        best_vals = [r["history_best"][i] for r in runs if i < len(r["history_best"])]
        avg_vals = [r["history_avg"][i] for r in runs if i < len(r["history_avg"])]
        if not best_vals:
            continue
        out.append(
            {
                "gen": i + 1,
                "best_mean_ratio": mean(best_vals),
                "best_min_ratio": min(best_vals),
                "best_max_ratio": max(best_vals),
                "best_std_ratio": _safe_stdev(best_vals),
                "avg_mean_ratio": mean(avg_vals) if avg_vals else 0.0,
            }
        )
    return out


def build_report(suite_dir: Path) -> str:
    runs = _parse_suite(suite_dir)
    if not runs:
        raise RuntimeError("该目录下未发现可分析实验")

    group_name = suite_dir.name
    run_count = len(runs)

    gaps = [r["gap_pct"] for r in runs]
    costs = [r["cost_total_usd"] for r in runs]
    walls = [r["wall_sec"] for r in runs]
    llm_secs = [r["llm_sec"] for r in runs]
    improv = [r["curve_improve_ratio"] for r in runs]
    eval_events = [r["eval_events"] for r in runs]
    dedup_hits = [r["dedup_expr_hit"] for r in runs]
    err_count = sum(r["eval_errors"] for r in runs)

    best_run = min(runs, key=lambda x: x["gap_pct"])
    worst_run = max(runs, key=lambda x: x["gap_pct"])

    gen_stats = _gen_level_summary(runs)
    if gen_stats:
        g1 = gen_stats[0]["best_mean_ratio"]
        g4 = gen_stats[min(3, len(gen_stats) - 1)]["best_mean_ratio"]
        g8 = gen_stats[-1]["best_mean_ratio"]
        early_drop = (g1 - g4) / g1 if abs(g1) > 1e-12 else 0.0
        late_drop = (g4 - g8) / g4 if abs(g4) > 1e-12 else 0.0
    else:
        early_drop = 0.0
        late_drop = 0.0

    # 成本效率：每1美元可减少多少gap百分点（相对BF固定6.2496）
    bf_gap = 6.249559388376383
    eff = []
    for r in runs:
        gain_pp = bf_gap - r["gap_pct"]
        if r["cost_total_usd"] > 1e-12:
            eff.append(gain_pp / r["cost_total_usd"])

    lines: list[str] = []
    lines.append(f"# 第1套实验（{group_name}）详细分析报告")
    lines.append("")
    lines.append(f"- 生成时间: {datetime.now().isoformat(timespec='seconds')}")
    lines.append(f"- 套件目录: {suite_dir.as_posix()}")
    lines.append(f"- 样本数: {run_count} (seed {', '.join(str(r['seed']) for r in runs)})")
    lines.append("")

    lines.append("## 1) 核心结论")
    lines.append("")
    lines.append(f"- 平均性能（Ours gap%）: {_fmt(mean(gaps), 4)}，中位数: {_fmt(median(gaps), 4)}，标准差: {_fmt(_safe_stdev(gaps), 4)}。")
    lines.append(f"- 最优seed: {best_run['seed']}（{_fmt(best_run['gap_pct'], 4)}%），最差seed: {worst_run['seed']}（{_fmt(worst_run['gap_pct'], 4)}%），区间跨度: {_fmt(max(gaps)-min(gaps), 4)}pp。")
    lines.append(f"- 平均总耗时: {_fmt(mean(walls), 2)}秒（约{_fmt(mean(walls)/60.0, 2)}分钟）；其中LLM累计耗时均值: {_fmt(mean(llm_secs), 2)}秒。")
    lines.append(f"- 平均总成本（默认4.0 chars/token估算）: ${_fmt(mean(costs), 6)}；范围: ${_fmt(min(costs), 6)} ~ ${_fmt(max(costs), 6)}。")
    lines.append(f"- 收敛节奏: 前半程(g1→g4)平均改善 {_pct(early_drop)}，后半程(g4→末代)平均改善 {_pct(late_drop)}。")
    lines.append(f"- 质量提升一致性: 首末代best相对改善均值 {_pct(mean(improv))}，标准差 {_pct(_safe_stdev(improv))}。")
    lines.append("")

    lines.append("## 2) Seed级明细")
    lines.append("")
    lines.append("| seed | gap_pct | wall_sec | llm_sec | llm_req | eval_events | dedup_expr_hit | eval_errors | cost_total_usd |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for r in sorted(runs, key=lambda x: x["seed"]):
        lines.append(
            f"| {r['seed']} | {_fmt(r['gap_pct'], 4)} | {_fmt(r['wall_sec'], 2)} | {_fmt(r['llm_sec'], 2)} | {r['llm_req']} | {r['eval_events']} | {r['dedup_expr_hit']} | {r['eval_errors']} | {_fmt(r['cost_total_usd'], 6)} |"
        )
    lines.append("")

    lines.append("## 3) 进化轨迹汇总（跨seed）")
    lines.append("")
    lines.append("| gen | mean(best_ratio) | min(best_ratio) | max(best_ratio) | std(best_ratio) | mean(avg_ratio) |")
    lines.append("|---:|---:|---:|---:|---:|---:|")
    for g in gen_stats:
        lines.append(
            f"| {int(g['gen'])} | {_fmt(g['best_mean_ratio'], 6)} | {_fmt(g['best_min_ratio'], 6)} | {_fmt(g['best_max_ratio'], 6)} | {_fmt(g['best_std_ratio'], 6)} | {_fmt(g['avg_mean_ratio'], 6)} |"
        )
    lines.append("")

    lines.append("## 4) 成本-性能效率")
    lines.append("")
    lines.append(f"- 相对BF基线(6.2496%)的平均提升: {_fmt(bf_gap - mean(gaps), 4)}pp。")
    lines.append(f"- 每1美元可带来的gap改进（pp/$）均值: {_fmt(mean(eff), 2)}，范围: {_fmt(min(eff), 2)} ~ {_fmt(max(eff), 2)}。")
    lines.append(f"- LLM时间占比（LLM累计耗时/总墙钟）均值: {_pct(mean([r['llm_sec']/r['wall_sec'] for r in runs if r['wall_sec']>0]))}。")
    lines.append("")

    lines.append("## 5) 稳定性与风险")
    lines.append("")
    lines.append(f"- gap标准差 {_fmt(_safe_stdev(gaps), 4)}，说明该套配置有一定seed敏感性，但未出现失控离散。")
    lines.append(f"- eval error 总数: {err_count}，占总评估事件比例约 {_pct(err_count / max(1, sum(eval_events)), 4)}。")
    lines.append(f"- dedup命中均值: {_fmt(mean(dedup_hits), 2)}，建议继续监控表达式空间多样性，避免后期同质化。")
    lines.append("")

    lines.append("## 6) 结论与建议")
    lines.append("")
    lines.append("- 若目标是最优质量：优先 seed44/45/46 同等配置复现实验，再做多次重跑取最优。")
    lines.append("- 若目标是稳定+性价比：保持当前ds-chat配置，建议追加3-5个seed并采用中位数汇报，降低偶然波动影响。")
    lines.append("- 若目标是缩短总耗时：优先优化非LLM阶段（评估/演化循环），因为当前LLM累计耗时只占总墙钟的一小部分。")
    lines.append("- 若目标是进一步降成本：可在不降质量前提下先试减少refine token长度（压缩提示模板），成本下降会更直接。")
    lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="按套件目录生成详细分析报告")
    parser.add_argument("--suite-dir", required=True, help="例如 runs/final/1 ds-chat")
    parser.add_argument("--output", default="suite_detailed_analysis.md", help="输出文件名")
    args = parser.parse_args()

    suite_dir = Path(args.suite_dir)
    if not suite_dir.exists():
        raise FileNotFoundError(f"目录不存在: {suite_dir}")

    report_text = build_report(suite_dir)
    out_path = suite_dir / args.output
    out_path.write_text(report_text, encoding="utf-8")
    print(f"Generated: {out_path}")


if __name__ == "__main__":
    main()
