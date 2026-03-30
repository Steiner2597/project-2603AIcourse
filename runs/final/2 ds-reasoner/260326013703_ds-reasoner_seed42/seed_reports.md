# Seed实验统计报告: 260326013703_ds-reasoner_seed42

## 1) 运行概览

- 分组: 2 ds-reasoner
- seed: 42
- provider_tag: ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T01:37:03
- 结束时间: 2026-03-26T03:51:44
- 总耗时(秒): 8081.00
- Ours gap(%): 5.2720
- best_score(ratio): 0.052720
- best曲线首末相对改善: 13.84%

## 2) 事件统计

- total_eval_events: 596
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 170
- eval_errors: 0
- LLM请求总耗时(秒): 3539.38
- LLM请求平均耗时(秒): 110.61

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 32 | 59369 | 11242 | 3539.38 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.002375
- cost_input_miss_usd: $0.009329
- cost_output_usd: $0.007034

### default_4p0

- cost_input_hit_usd: $0.002078
- cost_input_miss_usd: $0.008163
- cost_output_usd: $0.006155

### optimistic_4p5

- cost_input_hit_usd: $0.001847
- cost_input_miss_usd: $0.007256
- cost_output_usd: $0.005471

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 1700.93 |
| refine | 16 | 1838.45 |

