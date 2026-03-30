# Seed实验统计报告: 260326091904_gpt5nano+gpt5mini_seed46

## 1) 运行概览

- 分组: 6 gpt5nano+gpt5mini
- seed: 46
- provider_tag: gpt5nano+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T09:19:04
- 结束时间: 2026-03-26T10:52:47
- 总耗时(秒): 5623.00
- Ours gap(%): 4.9163
- best_score(ratio): 0.049163
- best曲线首末相对改善: 2.57%

## 2) 事件统计

- total_eval_events: 560
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 150
- eval_errors: 0
- LLM请求总耗时(秒): 1160.07
- LLM请求平均耗时(秒): 36.25

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 16 | 49011 | 16132 | 552.65 |
| gpt-5-nano | 16 | 38018 | 10271 | 607.42 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.004044
- cost_output_usd: $0.010392

### default_4p0

- cost_input_usd: $0.003538
- cost_output_usd: $0.009093

### optimistic_4p5

- cost_input_usd: $0.003145
- cost_output_usd: $0.008083

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 607.42 |
| refine | 16 | 552.65 |

