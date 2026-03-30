# Seed实验统计报告: 260326111931_ds-chat+ds-reasoner_seed45

## 1) 运行概览

- 分组: 5 ds-chat+ds-reasoner
- seed: 45
- provider_tag: ds-chat+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T11:19:31
- 结束时间: 2026-03-26T13:16:31
- 总耗时(秒): 7020.00
- Ours gap(%): 5.4064
- best_score(ratio): 0.054064
- best曲线首末相对改善: 12.84%

## 2) 事件统计

- total_eval_events: 630
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 185
- eval_errors: 0
- LLM请求总耗时(秒): 2507.89
- LLM请求平均耗时(秒): 78.37

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 30514 | 14168 | 193.25 |
| deepseek-reasoner | 16 | 35869 | 6730 | 2314.65 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.001679
- cost_input_miss_usd: $0.008078
- cost_output_usd: $0.005911

### default_4p0

- cost_input_hit_usd: $0.001469
- cost_input_miss_usd: $0.007068
- cost_output_usd: $0.005172

### optimistic_4p5

- cost_input_hit_usd: $0.001306
- cost_input_miss_usd: $0.006283
- cost_output_usd: $0.004598

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 193.25 |
| refine | 16 | 2314.65 |

