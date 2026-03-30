# Seed实验统计报告: 260326033313_ds-chat+ds-reasoner_seed43

## 1) 运行概览

- 分组: 5 ds-chat+ds-reasoner
- seed: 43
- provider_tag: ds-chat+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T03:33:13
- 结束时间: 2026-03-26T05:20:56
- 总耗时(秒): 6463.00
- Ours gap(%): 4.8724
- best_score(ratio): 0.048724
- best曲线首末相对改善: 21.91%

## 2) 事件统计

- total_eval_events: 671
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 181
- eval_errors: 0
- LLM请求总耗时(秒): 1726.61
- LLM请求平均耗时(秒): 53.96

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 27574 | 13027 | 136.58 |
| deepseek-reasoner | 16 | 31513 | 4902 | 1590.03 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.001481
- cost_input_miss_usd: $0.007158
- cost_output_usd: $0.004630

### default_4p0

- cost_input_hit_usd: $0.001296
- cost_input_miss_usd: $0.006263
- cost_output_usd: $0.004052

### optimistic_4p5

- cost_input_hit_usd: $0.001152
- cost_input_miss_usd: $0.005567
- cost_output_usd: $0.003601

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 136.58 |
| refine | 16 | 1590.03 |

