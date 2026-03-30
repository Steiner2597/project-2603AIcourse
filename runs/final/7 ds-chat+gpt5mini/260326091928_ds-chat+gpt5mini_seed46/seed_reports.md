# Seed实验统计报告: 260326091928_ds-chat+gpt5mini_seed46

## 1) 运行概览

- 分组: 7 ds-chat+gpt5mini
- seed: 46
- provider_tag: ds-chat+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T09:19:28
- 结束时间: 2026-03-26T10:48:16
- 总耗时(秒): 5328.00
- Ours gap(%): 4.8600
- best_score(ratio): 0.048600
- best曲线首末相对改善: 3.72%

## 2) 事件统计

- total_eval_events: 586
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 165
- eval_errors: 0
- LLM请求总耗时(秒): 798.92
- LLM请求平均耗时(秒): 24.97

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 36827 | 15931 | 189.22 |
| gpt-5-mini | 16 | 45829 | 20127 | 609.69 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000295
- cost_input_miss_usd: $0.002946
- cost_input_usd: $0.003273
- cost_output_usd: $0.013413

### default_4p0

- cost_input_hit_usd: $0.000258
- cost_input_miss_usd: $0.002578
- cost_input_usd: $0.002864
- cost_output_usd: $0.011736

### optimistic_4p5

- cost_input_hit_usd: $0.000229
- cost_input_miss_usd: $0.002291
- cost_input_usd: $0.002546
- cost_output_usd: $0.010432

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 189.22 |
| refine | 16 | 609.69 |

