# Seed实验统计报告: 260326052134_ds-chat+ds-reasoner_seed44

## 1) 运行概览

- 分组: 5 ds-chat+ds-reasoner
- seed: 44
- provider_tag: ds-chat+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T05:21:34
- 结束时间: 2026-03-26T06:57:49
- 总耗时(秒): 5775.00
- Ours gap(%): 4.9313
- best_score(ratio): 0.049313
- best曲线首末相对改善: 8.20%

## 2) 事件统计

- total_eval_events: 583
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 166
- eval_errors: 0
- LLM请求总耗时(秒): 1661.57
- LLM请求平均耗时(秒): 51.92

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 33050 | 15693 | 157.64 |
| deepseek-reasoner | 16 | 39363 | 8018 | 1503.93 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.001839
- cost_input_miss_usd: $0.008830
- cost_output_usd: $0.006900

### default_4p0

- cost_input_hit_usd: $0.001609
- cost_input_miss_usd: $0.007726
- cost_output_usd: $0.006038

### optimistic_4p5

- cost_input_hit_usd: $0.001430
- cost_input_miss_usd: $0.006867
- cost_output_usd: $0.005367

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 157.64 |
| refine | 16 | 1503.93 |

