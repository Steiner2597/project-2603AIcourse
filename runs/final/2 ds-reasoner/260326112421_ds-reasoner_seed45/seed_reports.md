# Seed实验统计报告: 260326112421_ds-reasoner_seed45

## 1) 运行概览

- 分组: 2 ds-reasoner
- seed: 45
- provider_tag: ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T11:24:21
- 结束时间: 2026-03-26T14:01:22
- 总耗时(秒): 9421.00
- Ours gap(%): 4.9410
- best_score(ratio): 0.049410
- best曲线首末相对改善: 20.19%

## 2) 事件统计

- total_eval_events: 631
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 175
- eval_errors: 0
- LLM请求总耗时(秒): 5049.10
- LLM请求平均耗时(秒): 157.78

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 32 | 54761 | 10181 | 5049.10 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.002190
- cost_input_miss_usd: $0.008605
- cost_output_usd: $0.006370

### default_4p0

- cost_input_hit_usd: $0.001917
- cost_input_miss_usd: $0.007530
- cost_output_usd: $0.005574

### optimistic_4p5

- cost_input_hit_usd: $0.001704
- cost_input_miss_usd: $0.006693
- cost_output_usd: $0.004955

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 2660.78 |
| refine | 16 | 2388.32 |

