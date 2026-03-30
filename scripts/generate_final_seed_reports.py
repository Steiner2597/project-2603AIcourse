from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Any


# 价格单位: 美元 / 百万 tokens
# DeepSeek 输入同时给出缓存未命中和缓存命中两种单价。
PRICE_TABLE_USD_PER_MTOK = {
    "deepseek-chat": {
        "input_miss": 0.28,
        "input_hit": 0.028,
        "output": 0.42,
    },
    "deepseek-reasoner": {
        "input_miss": 0.55,
        "input_hit": 0.14,
        "output": 2.19,
    },
    "gpt-5-nano": {
        "input": 0.05,
        "output": 0.40,
    },
    "gpt-5-mini": {
        "input": 0.25,
        "output": 2.00,
    },
}


@dataclass
class RequestRecord:
    request_id: int
    model: str
    provider: str
    request_type: str
    phase: str
    generation: int | None
    island: int | None
    prompt_chars: int
    response_chars: int
    elapsed_sec: float
    started_at: str | None
    finished_at: str | None


def _safe_read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_ts(ts: str | None) -> datetime | None:
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts)
    except ValueError:
        return None


def _seconds_between(started_at: str | None, finished_at: str | None) -> float | None:
    s = _parse_ts(started_at)
    f = _parse_ts(finished_at)
    if s is None or f is None:
        return None
    return max(0.0, (f - s).total_seconds())


def _iter_requests(requests_jsonl: Path) -> list[RequestRecord]:
    if not requests_jsonl.exists():
        return []

    starts: dict[int, dict[str, Any]] = {}
    records: list[RequestRecord] = []
    for line in requests_jsonl.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        event = str(obj.get("event", ""))
        request_id = int(obj.get("request_id", -1))
        if request_id < 0:
            continue

        if event == "llm_request_start":
            starts[request_id] = obj
            continue

        if event != "llm_request_done":
            continue

        st = starts.get(request_id, {})
        records.append(
            RequestRecord(
                request_id=request_id,
                model=str(obj.get("model") or st.get("model") or "unknown"),
                provider=str(obj.get("provider") or st.get("provider") or "unknown"),
                request_type=str(obj.get("request_type") or st.get("request_type") or "unknown"),
                phase=str(obj.get("phase") or st.get("phase") or "unknown"),
                generation=obj.get("generation", st.get("generation")),
                island=obj.get("island", st.get("island")),
                prompt_chars=int(st.get("prompt_chars", 0) or 0),
                response_chars=int(obj.get("response_chars", 0) or 0),
                elapsed_sec=float(obj.get("elapsed_sec", 0.0) or 0.0),
                started_at=st.get("started_at"),
                finished_at=obj.get("finished_at"),
            )
        )

    return records


def _extract_seed(run_name: str) -> int | None:
    marker = "_seed"
    if marker not in run_name:
        return None
    tail = run_name.split(marker, 1)[1]
    digits = ""
    for ch in tail:
        if ch.isdigit():
            digits += ch
        else:
            break
    return int(digits) if digits else None


def _tokens_from_chars(chars: int, chars_per_token: float) -> float:
    if chars <= 0:
        return 0.0
    return chars / chars_per_token


def _cost_for_model(model: str, input_tokens: float, output_tokens: float) -> dict[str, float]:
    price = PRICE_TABLE_USD_PER_MTOK.get(model)
    if not price:
        return {"cost_usd": 0.0}

    scale = 1_000_000.0
    if "input_miss" in price:
        return {
            "cost_input_miss_usd": input_tokens * price["input_miss"] / scale,
            "cost_input_hit_usd": input_tokens * price["input_hit"] / scale,
            "cost_output_usd": output_tokens * price["output"] / scale,
        }

    return {
        "cost_input_usd": input_tokens * price["input"] / scale,
        "cost_output_usd": output_tokens * price["output"] / scale,
    }


def _summarize_run(run_dir: Path) -> dict[str, Any]:
    summary = _safe_read_json(run_dir / "summary.json")
    metrics = _safe_read_json(run_dir / "metrics.json")
    status = _safe_read_json(run_dir / "status.json")
    reqs = _iter_requests(run_dir / "checkpoints" / "requests.jsonl")

    run_name = run_dir.name
    group_name = run_dir.parent.name
    provider_tag = metrics.get("experiment_config", {}).get("provider_tag", "")

    started_at = status.get("started_at")
    finished_at = status.get("finished_at")
    wall_clock_sec = _seconds_between(started_at, finished_at)

    llm_elapsed_sum = sum(r.elapsed_sec for r in reqs)
    llm_elapsed_avg = (llm_elapsed_sum / len(reqs)) if reqs else 0.0

    by_model: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    by_phase: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    by_generation: dict[int, dict[str, float]] = defaultdict(lambda: defaultdict(float))

    for r in reqs:
        by_model[r.model]["requests"] += 1
        by_model[r.model]["prompt_chars"] += r.prompt_chars
        by_model[r.model]["response_chars"] += r.response_chars
        by_model[r.model]["elapsed_sec"] += r.elapsed_sec

        by_phase[r.phase]["requests"] += 1
        by_phase[r.phase]["elapsed_sec"] += r.elapsed_sec

        if isinstance(r.generation, int):
            by_generation[r.generation]["requests"] += 1
            by_generation[r.generation]["elapsed_sec"] += r.elapsed_sec

    # token 估算采用字符转 token，默认 4 chars/token，并提供 3.5~4.5 灵敏度范围
    token_scenarios = {
        "pessimistic_3p5": 3.5,
        "default_4p0": 4.0,
        "optimistic_4p5": 4.5,
    }

    by_model_with_cost: dict[str, Any] = {}
    total_cost = {
        "pessimistic_3p5": defaultdict(float),
        "default_4p0": defaultdict(float),
        "optimistic_4p5": defaultdict(float),
    }

    for model, bucket in sorted(by_model.items()):
        prompt_chars = int(bucket["prompt_chars"])
        response_chars = int(bucket["response_chars"])
        model_info: dict[str, Any] = {
            "requests": int(bucket["requests"]),
            "prompt_chars": prompt_chars,
            "response_chars": response_chars,
            "elapsed_sec": bucket["elapsed_sec"],
            "scenarios": {},
        }

        for scenario_name, cpt in token_scenarios.items():
            input_tokens = _tokens_from_chars(prompt_chars, cpt)
            output_tokens = _tokens_from_chars(response_chars, cpt)
            costs = _cost_for_model(model, input_tokens, output_tokens)
            model_info["scenarios"][scenario_name] = {
                "chars_per_token": cpt,
                "input_tokens_est": input_tokens,
                "output_tokens_est": output_tokens,
                **costs,
            }

            for key, val in costs.items():
                total_cost[scenario_name][key] += float(val)

        by_model_with_cost[model] = model_info

    def _get_gap_pct() -> float | None:
        rows = summary.get("baseline_comparison", {}).get("rows", [])
        for r in rows:
            if r.get("method") == "FunSearch-Lite (Ours)":
                return float(r.get("gap_pct", 0.0))
        score = metrics.get("best_score")
        if score is not None:
            return float(score) * 100.0
        return None

    # 质量指标
    gap_pct = _get_gap_pct()
    best_score = metrics.get("best_score")
    history_best = metrics.get("history", {}).get("best_per_gen", [])
    improvement_ratio = None
    if isinstance(history_best, list) and len(history_best) >= 2:
        first = float(history_best[0])
        last = float(history_best[-1])
        if abs(first) > 1e-12:
            improvement_ratio = (first - last) / first

    run_report = {
        "run_dir": str(run_dir.as_posix()),
        "group": group_name,
        "run_name": run_name,
        "seed": _extract_seed(run_name),
        "provider_tag": provider_tag,
        "status": status.get("status", "unknown"),
        "started_at": started_at,
        "finished_at": finished_at,
        "wall_clock_sec": wall_clock_sec,
        "quality": {
            "best_score_ratio": best_score,
            "ours_gap_pct": gap_pct,
            "improve_ratio_first_to_last_best": improvement_ratio,
        },
        "events": {
            "total_eval_events": summary.get("total", {}).get("eval_events"),
            "total_llm_events": summary.get("total", {}).get("llm_events"),
            "llm_request_done": summary.get("total", {}).get("llm_request_done"),
            "llm_request_error": summary.get("total", {}).get("llm_request_error"),
            "accepted": summary.get("total", {}).get("accepted"),
            "dedup_expr_hit": summary.get("total", {}).get("dedup_expr_hit"),
            "eval_errors": summary.get("total", {}).get("eval_errors"),
        },
        "llm_time": {
            "sum_elapsed_sec": llm_elapsed_sum,
            "avg_elapsed_sec": llm_elapsed_avg,
        },
        "by_model": by_model_with_cost,
        "by_phase": {
            k: {
                "requests": int(v["requests"]),
                "elapsed_sec": float(v["elapsed_sec"]),
            }
            for k, v in sorted(by_phase.items())
        },
        "by_generation": {
            str(k): {
                "requests": int(v["requests"]),
                "elapsed_sec": float(v["elapsed_sec"]),
            }
            for k, v in sorted(by_generation.items())
        },
        "cost_totals": {
            name: dict(vals)
            for name, vals in total_cost.items()
        },
    }
    return run_report


def _render_run_markdown(run_report: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# Seed实验统计报告: {run_report['run_name']}")
    lines.append("")
    lines.append("## 1) 运行概览")
    lines.append("")
    lines.append(f"- 分组: {run_report['group']}")
    lines.append(f"- seed: {run_report.get('seed')}")
    lines.append(f"- provider_tag: {run_report.get('provider_tag')}")
    lines.append(f"- 状态: {run_report.get('status')}")
    lines.append(f"- 开始时间: {run_report.get('started_at')}")
    lines.append(f"- 结束时间: {run_report.get('finished_at')}")
    wc = run_report.get("wall_clock_sec")
    lines.append(f"- 总耗时(秒): {wc:.2f}" if isinstance(wc, (int, float)) else "- 总耗时(秒): N/A")
    q = run_report.get("quality", {})
    gap = q.get("ours_gap_pct")
    if isinstance(gap, (int, float)):
        lines.append(f"- Ours gap(%): {gap:.4f}")
    best_score = q.get("best_score_ratio")
    if isinstance(best_score, (int, float)):
        lines.append(f"- best_score(ratio): {best_score:.6f}")
    improve = q.get("improve_ratio_first_to_last_best")
    if isinstance(improve, (int, float)):
        lines.append(f"- best曲线首末相对改善: {improve * 100:.2f}%")

    lines.append("")
    lines.append("## 2) 事件统计")
    lines.append("")
    ev = run_report.get("events", {})
    for k in [
        "total_eval_events",
        "total_llm_events",
        "llm_request_done",
        "llm_request_error",
        "accepted",
        "dedup_expr_hit",
        "eval_errors",
    ]:
        lines.append(f"- {k}: {ev.get(k)}")

    llm_time = run_report.get("llm_time", {})
    lines.append(f"- LLM请求总耗时(秒): {llm_time.get('sum_elapsed_sec', 0.0):.2f}")
    lines.append(f"- LLM请求平均耗时(秒): {llm_time.get('avg_elapsed_sec', 0.0):.2f}")

    lines.append("")
    lines.append("## 3) 分模型统计")
    lines.append("")
    lines.append("| model | requests | prompt_chars | response_chars | elapsed_sec |")
    lines.append("|---|---:|---:|---:|---:|")
    for model, m in run_report.get("by_model", {}).items():
        lines.append(
            f"| {model} | {m['requests']} | {m['prompt_chars']} | {m['response_chars']} | {m['elapsed_sec']:.2f} |"
        )

    lines.append("")
    lines.append("## 4) 成本估算")
    lines.append("")
    lines.append("说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。")
    lines.append("")
    for scenario, vals in run_report.get("cost_totals", {}).items():
        lines.append(f"### {scenario}")
        lines.append("")
        for k, v in sorted(vals.items()):
            lines.append(f"- {k}: ${v:.6f}")
        lines.append("")

    lines.append("## 5) 分阶段耗时")
    lines.append("")
    lines.append("| phase | requests | elapsed_sec |")
    lines.append("|---|---:|---:|")
    for phase, v in run_report.get("by_phase", {}).items():
        lines.append(f"| {phase} | {v['requests']} | {v['elapsed_sec']:.2f} |")
    lines.append("")

    return "\n".join(lines) + "\n"


def _fmt_float(v: float | None, ndigits: int = 6) -> str:
    if v is None:
        return ""
    return f"{v:.{ndigits}f}"


def generate_reports(final_root: Path, out_name: str = "seed_reports") -> None:
    run_dirs = sorted(
        p
        for p in final_root.glob("*/*")
        if p.is_dir() and (p / "summary.json").exists() and (p / "metrics.json").exists()
    )

    all_reports: list[dict[str, Any]] = []
    for run_dir in run_dirs:
        report = _summarize_run(run_dir)
        all_reports.append(report)

        json_path = run_dir / f"{out_name}.json"
        md_path = run_dir / f"{out_name}.md"
        json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        md_path.write_text(_render_run_markdown(report), encoding="utf-8")

    # 全局汇总
    aggregate_json = final_root / f"{out_name}_aggregate.json"
    aggregate_md = final_root / f"{out_name}_aggregate.md"
    aggregate_csv = final_root / f"{out_name}_aggregate.csv"

    aggregate = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "final_root": str(final_root.as_posix()),
        "run_count": len(all_reports),
        "runs": all_reports,
    }
    aggregate_json.write_text(json.dumps(aggregate, ensure_ascii=False, indent=2), encoding="utf-8")

    # CSV平铺，便于后续筛选
    csv_rows: list[dict[str, Any]] = []
    for r in all_reports:
        default_cost = r.get("cost_totals", {}).get("default_4p0", {})
        csv_rows.append(
            {
                "group": r.get("group"),
                "run_name": r.get("run_name"),
                "seed": r.get("seed"),
                "status": r.get("status"),
                "provider_tag": r.get("provider_tag"),
                "ours_gap_pct": r.get("quality", {}).get("ours_gap_pct"),
                "wall_clock_sec": r.get("wall_clock_sec"),
                "llm_elapsed_sum_sec": r.get("llm_time", {}).get("sum_elapsed_sec"),
                "llm_requests_done": r.get("events", {}).get("llm_request_done"),
                "eval_events": r.get("events", {}).get("total_eval_events"),
                "eval_errors": r.get("events", {}).get("eval_errors"),
                "cost_default_input_miss_usd": default_cost.get("cost_input_miss_usd"),
                "cost_default_input_hit_usd": default_cost.get("cost_input_hit_usd"),
                "cost_default_input_usd": default_cost.get("cost_input_usd"),
                "cost_default_output_usd": default_cost.get("cost_output_usd"),
            }
        )

    with aggregate_csv.open("w", newline="", encoding="utf-8") as f:
        fieldnames = list(csv_rows[0].keys()) if csv_rows else ["run_name"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_rows)

    # Markdown总览
    group_buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in all_reports:
        group_buckets[r.get("group", "unknown")].append(r)

    md_lines: list[str] = []
    md_lines.append("# Final Seed实验汇总报告")
    md_lines.append("")
    md_lines.append(f"- 生成时间: {aggregate['generated_at']}")
    md_lines.append(f"- 实验数量: {aggregate['run_count']}")
    md_lines.append("")

    md_lines.append("## 1) 全量实验明细(默认4.0 chars/token成本)")
    md_lines.append("")
    md_lines.append(
        "| group | run_name | seed | ours_gap_pct | wall_clock_sec | llm_elapsed_sum_sec | cost_input_usd | cost_output_usd |"
    )
    md_lines.append("|---|---|---:|---:|---:|---:|---:|---:|")

    for r in sorted(all_reports, key=lambda x: (str(x.get("group")), int(x.get("seed") or -1))):
        c = r.get("cost_totals", {}).get("default_4p0", {})
        input_cost = c.get("cost_input_usd", 0.0) + c.get("cost_input_miss_usd", 0.0)
        output_cost = c.get("cost_output_usd", 0.0)
        md_lines.append(
            "| {group} | {run_name} | {seed} | {gap} | {wall} | {llm} | {ic} | {oc} |".format(
                group=r.get("group"),
                run_name=r.get("run_name"),
                seed=r.get("seed"),
                gap=_fmt_float(r.get("quality", {}).get("ours_gap_pct"), 4),
                wall=_fmt_float(r.get("wall_clock_sec"), 2),
                llm=_fmt_float(r.get("llm_time", {}).get("sum_elapsed_sec"), 2),
                ic=_fmt_float(input_cost, 6),
                oc=_fmt_float(output_cost, 6),
            )
        )

    md_lines.append("")
    md_lines.append("## 2) 按分组统计")
    md_lines.append("")
    md_lines.append(
        "| group | runs | avg_gap_pct | std_hint(min~max) | avg_wall_clock_sec | avg_cost_input_usd | avg_cost_output_usd |"
    )
    md_lines.append("|---|---:|---:|---:|---:|---:|---:|")

    for group, rows in sorted(group_buckets.items()):
        gaps = [float(r.get("quality", {}).get("ours_gap_pct")) for r in rows if r.get("quality", {}).get("ours_gap_pct") is not None]
        walls = [float(r.get("wall_clock_sec")) for r in rows if r.get("wall_clock_sec") is not None]
        in_costs = []
        out_costs = []
        for r in rows:
            c = r.get("cost_totals", {}).get("default_4p0", {})
            in_costs.append(float(c.get("cost_input_usd", 0.0) + c.get("cost_input_miss_usd", 0.0)))
            out_costs.append(float(c.get("cost_output_usd", 0.0)))

        gap_range = ""
        if gaps:
            gap_range = f"{min(gaps):.4f}~{max(gaps):.4f}"

        md_lines.append(
            "| {group} | {runs} | {avg_gap} | {gap_range} | {avg_wall} | {avg_in} | {avg_out} |".format(
                group=group,
                runs=len(rows),
                avg_gap=_fmt_float(mean(gaps), 4) if gaps else "",
                gap_range=gap_range,
                avg_wall=_fmt_float(mean(walls), 2) if walls else "",
                avg_in=_fmt_float(mean(in_costs), 6) if in_costs else "",
                avg_out=_fmt_float(mean(out_costs), 6) if out_costs else "",
            )
        )

    aggregate_md.write_text("\n".join(md_lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="为runs/final实验批量生成seed统计报告")
    parser.add_argument(
        "--final-root",
        default="runs/final",
        help="final实验根目录，默认 runs/final",
    )
    parser.add_argument(
        "--out-name",
        default="seed_reports",
        help="单实验输出文件名前缀，默认 seed_reports",
    )
    args = parser.parse_args()

    final_root = Path(args.final_root)
    if not final_root.exists():
        raise FileNotFoundError(f"目录不存在: {final_root}")

    generate_reports(final_root=final_root, out_name=args.out_name)
    print(f"Done. reports generated under: {final_root}")


if __name__ == "__main__":
    main()
