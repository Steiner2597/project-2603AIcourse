# Seed实验统计报告: 260326045229_gpt5mini_seed44

## 1) 运行概览

- 分组: 4 gpt5mini
- seed: 44
- provider_tag: gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T04:52:29
- 结束时间: 2026-03-26T06:22:03
- 总耗时(秒): 5374.00
- Ours gap(%): 5.1611
- best_score(ratio): 0.051611
- best曲线首末相对改善: 3.52%

## 2) 事件统计

- total_eval_events: 578
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 143
- eval_errors: 0
- LLM请求总耗时(秒): 950.98
- LLM请求平均耗时(秒): 29.72

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 32 | 83900 | 32748 | 950.98 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.005993
- cost_output_usd: $0.018713

### default_4p0

- cost_input_usd: $0.005244
- cost_output_usd: $0.016374

### optimistic_4p5

- cost_input_usd: $0.004661
- cost_output_usd: $0.014555

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 438.23 |
| refine | 16 | 512.75 |

