# Seed实验统计报告: 260326034536_gpt5nano+ds-reasoner_seed43

## 1) 运行概览

- 分组: 8 gpt5nano+ds-reasoner
- seed: 43
- provider_tag: gpt5nano+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T03:45:36
- 结束时间: 2026-03-26T05:38:14
- 总耗时(秒): 6758.00
- Ours gap(%): 4.9888
- best_score(ratio): 0.049888
- best曲线首末相对改善: 20.04%

## 2) 事件统计

- total_eval_events: 696
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 203
- eval_errors: 0
- LLM请求总耗时(秒): 1997.55
- LLM请求平均耗时(秒): 62.42

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 16 | 36832 | 5507 | 1432.61 |
| gpt-5-nano | 16 | 30661 | 11549 | 564.94 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.001473
- cost_input_miss_usd: $0.005788
- cost_input_usd: $0.000438
- cost_output_usd: $0.004766

### default_4p0

- cost_input_hit_usd: $0.001289
- cost_input_miss_usd: $0.005064
- cost_input_usd: $0.000383
- cost_output_usd: $0.004170

### optimistic_4p5

- cost_input_hit_usd: $0.001146
- cost_input_miss_usd: $0.004502
- cost_input_usd: $0.000341
- cost_output_usd: $0.003707

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 564.94 |
| refine | 16 | 1432.61 |

