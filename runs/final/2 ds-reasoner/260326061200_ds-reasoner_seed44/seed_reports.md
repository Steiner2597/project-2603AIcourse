# Seed实验统计报告: 260326061200_ds-reasoner_seed44

## 1) 运行概览

- 分组: 2 ds-reasoner
- seed: 44
- provider_tag: ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T06:12:00
- 结束时间: 2026-03-26T09:42:05
- 总耗时(秒): 12605.00
- Ours gap(%): 4.9493
- best_score(ratio): 0.049493
- best曲线首末相对改善: 7.86%

## 2) 事件统计

- total_eval_events: 586
- total_llm_events: 68
- llm_request_done: 32
- llm_request_error: 1
- accepted: 348
- dedup_expr_hit: 155
- eval_errors: 0
- LLM请求总耗时(秒): 3454.95
- LLM请求平均耗时(秒): 107.97

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 32 | 68455 | 12096 | 3454.95 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.002738
- cost_input_miss_usd: $0.010757
- cost_output_usd: $0.007569

### default_4p0

- cost_input_hit_usd: $0.002396
- cost_input_miss_usd: $0.009413
- cost_output_usd: $0.006623

### optimistic_4p5

- cost_input_hit_usd: $0.002130
- cost_input_miss_usd: $0.008367
- cost_output_usd: $0.005887

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 1787.66 |
| refine | 16 | 1667.29 |

