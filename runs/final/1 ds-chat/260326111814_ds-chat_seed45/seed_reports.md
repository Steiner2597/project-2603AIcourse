# Seed实验统计报告: 260326111814_ds-chat_seed45

## 1) 运行概览

- 分组: 1 ds-chat
- seed: 45
- provider_tag: ds-chat
- 状态: completed
- 开始时间: 2026-03-26T11:18:14
- 结束时间: 2026-03-26T12:41:55
- 总耗时(秒): 5021.00
- Ours gap(%): 4.8832
- best_score(ratio): 0.048832
- best曲线首末相对改善: 12.98%

## 2) 事件统计

- total_eval_events: 610
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 162
- eval_errors: 0
- LLM请求总耗时(秒): 357.58
- LLM请求平均耗时(秒): 11.17

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 32 | 60547 | 26379 | 357.58 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000484
- cost_input_miss_usd: $0.004844
- cost_output_usd: $0.003165

### default_4p0

- cost_input_hit_usd: $0.000424
- cost_input_miss_usd: $0.004238
- cost_output_usd: $0.002770

### optimistic_4p5

- cost_input_hit_usd: $0.000377
- cost_input_miss_usd: $0.003767
- cost_output_usd: $0.002462

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 175.77 |
| refine | 16 | 181.82 |

