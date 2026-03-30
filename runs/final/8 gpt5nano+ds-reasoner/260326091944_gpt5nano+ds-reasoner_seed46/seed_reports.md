# Seed实验统计报告: 260326091944_gpt5nano+ds-reasoner_seed46

## 1) 运行概览

- 分组: 8 gpt5nano+ds-reasoner
- seed: 46
- provider_tag: gpt5nano+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T09:19:44
- 结束时间: 2026-03-26T11:23:23
- 总耗时(秒): 7419.00
- Ours gap(%): 4.8892
- best_score(ratio): 0.048892
- best曲线首末相对改善: 3.11%

## 2) 事件统计

- total_eval_events: 556
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 139
- eval_errors: 0
- LLM请求总耗时(秒): 2904.25
- LLM请求平均耗时(秒): 90.76

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 16 | 56700 | 5358 | 2296.25 |
| gpt-5-nano | 16 | 43110 | 10500 | 608.01 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.002268
- cost_input_miss_usd: $0.008910
- cost_input_usd: $0.000616
- cost_output_usd: $0.004553

### default_4p0

- cost_input_hit_usd: $0.001985
- cost_input_miss_usd: $0.007796
- cost_input_usd: $0.000539
- cost_output_usd: $0.003984

### optimistic_4p5

- cost_input_hit_usd: $0.001764
- cost_input_miss_usd: $0.006930
- cost_input_usd: $0.000479
- cost_output_usd: $0.003541

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 608.01 |
| refine | 16 | 2296.25 |

