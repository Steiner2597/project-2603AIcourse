# Seed实验统计报告: 260326112027_gpt5nano+ds-reasoner_seed45

## 1) 运行概览

- 分组: 8 gpt5nano+ds-reasoner
- seed: 45
- provider_tag: gpt5nano+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T11:20:27
- 结束时间: 2026-03-26T13:14:48
- 总耗时(秒): 6861.00
- Ours gap(%): 5.1152
- best_score(ratio): 0.051152
- best曲线首末相对改善: 14.38%

## 2) 事件统计

- total_eval_events: 613
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 171
- eval_errors: 0
- LLM请求总耗时(秒): 2394.03
- LLM请求平均耗时(秒): 74.81

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 16 | 30349 | 5482 | 1939.26 |
| gpt-5-nano | 16 | 26217 | 8983 | 454.77 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.001214
- cost_input_miss_usd: $0.004769
- cost_input_usd: $0.000375
- cost_output_usd: $0.004457

### default_4p0

- cost_input_hit_usd: $0.001062
- cost_input_miss_usd: $0.004173
- cost_input_usd: $0.000328
- cost_output_usd: $0.003900

### optimistic_4p5

- cost_input_hit_usd: $0.000944
- cost_input_miss_usd: $0.003709
- cost_input_usd: $0.000291
- cost_output_usd: $0.003466

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 454.77 |
| refine | 16 | 1939.26 |

