# Seed实验统计报告: 260326030020_ds-chat_seed43

## 1) 运行概览

- 分组: 1 ds-chat
- seed: 43
- provider_tag: ds-chat
- 状态: completed
- 开始时间: 2026-03-26T03:00:20
- 结束时间: 2026-03-26T04:22:47
- 总耗时(秒): 4947.00
- Ours gap(%): 5.1192
- best_score(ratio): 0.051192
- best曲线首末相对改善: 17.93%

## 2) 事件统计

- total_eval_events: 677
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 191
- eval_errors: 0
- LLM请求总耗时(秒): 303.54
- LLM请求平均耗时(秒): 9.49

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 32 | 53932 | 26948 | 303.54 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000431
- cost_input_miss_usd: $0.004315
- cost_output_usd: $0.003234

### default_4p0

- cost_input_hit_usd: $0.000378
- cost_input_miss_usd: $0.003775
- cost_output_usd: $0.002830

### optimistic_4p5

- cost_input_hit_usd: $0.000336
- cost_input_miss_usd: $0.003356
- cost_output_usd: $0.002515

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 171.86 |
| refine | 16 | 131.68 |

