# Seed实验统计报告: 260326111944_ds-chat+gpt5mini_seed45

## 1) 运行概览

- 分组: 7 ds-chat+gpt5mini
- seed: 45
- provider_tag: ds-chat+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T11:19:44
- 结束时间: 2026-03-26T12:49:22
- 总耗时(秒): 5378.00
- Ours gap(%): 5.4705
- best_score(ratio): 0.054705
- best曲线首末相对改善: 11.72%

## 2) 事件统计

- total_eval_events: 667
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 202
- eval_errors: 0
- LLM请求总耗时(秒): 697.33
- LLM请求平均耗时(秒): 21.79

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 27007 | 12901 | 181.51 |
| gpt-5-mini | 16 | 30993 | 12810 | 515.82 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000216
- cost_input_miss_usd: $0.002161
- cost_input_usd: $0.002214
- cost_output_usd: $0.008868

### default_4p0

- cost_input_hit_usd: $0.000189
- cost_input_miss_usd: $0.001890
- cost_input_usd: $0.001937
- cost_output_usd: $0.007760

### optimistic_4p5

- cost_input_hit_usd: $0.000168
- cost_input_miss_usd: $0.001680
- cost_input_usd: $0.001722
- cost_output_usd: $0.006897

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 181.51 |
| refine | 16 | 515.82 |

