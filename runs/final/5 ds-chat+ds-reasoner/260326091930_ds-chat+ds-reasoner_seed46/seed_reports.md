# Seed实验统计报告: 260326091930_ds-chat+ds-reasoner_seed46

## 1) 运行概览

- 分组: 5 ds-chat+ds-reasoner
- seed: 46
- provider_tag: ds-chat+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T09:19:30
- 结束时间: 2026-03-26T11:11:09
- 总耗时(秒): 6699.00
- Ours gap(%): 4.8952
- best_score(ratio): 0.048952
- best曲线首末相对改善: 3.02%

## 2) 事件统计

- total_eval_events: 563
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 133
- eval_errors: 1
- LLM请求总耗时(秒): 2196.52
- LLM请求平均耗时(秒): 68.64

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 31277 | 15628 | 193.34 |
| deepseek-reasoner | 16 | 37436 | 7709 | 2003.17 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.001748
- cost_input_miss_usd: $0.008385
- cost_output_usd: $0.006699

### default_4p0

- cost_input_hit_usd: $0.001529
- cost_input_miss_usd: $0.007337
- cost_output_usd: $0.005862

### optimistic_4p5

- cost_input_hit_usd: $0.001359
- cost_input_miss_usd: $0.006522
- cost_output_usd: $0.005210

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 193.34 |
| refine | 16 | 2003.17 |

