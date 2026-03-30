# Seed实验统计报告: 260326013713_gpt5mini_seed42

## 1) 运行概览

- 分组: 4 gpt5mini
- seed: 42
- provider_tag: gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T01:37:13
- 结束时间: 2026-03-26T03:11:33
- 总耗时(秒): 5660.00
- Ours gap(%): 4.9572
- best_score(ratio): 0.049572
- best曲线首末相对改善: 18.45%

## 2) 事件统计

- total_eval_events: 595
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 172
- eval_errors: 0
- LLM请求总耗时(秒): 1189.39
- LLM请求平均耗时(秒): 37.17

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 32 | 65740 | 35699 | 1189.39 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.004696
- cost_output_usd: $0.020399

### default_4p0

- cost_input_usd: $0.004109
- cost_output_usd: $0.017850

### optimistic_4p5

- cost_input_usd: $0.003652
- cost_output_usd: $0.015866

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 563.70 |
| refine | 16 | 625.70 |

