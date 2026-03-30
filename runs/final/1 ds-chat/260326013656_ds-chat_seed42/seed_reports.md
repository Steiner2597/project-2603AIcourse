# Seed实验统计报告: 260326013656_ds-chat_seed42

## 1) 运行概览

- 分组: 1 ds-chat
- seed: 42
- provider_tag: ds-chat
- 状态: completed
- 开始时间: 2026-03-26T01:36:56
- 结束时间: 2026-03-26T02:59:41
- 总耗时(秒): 4965.00
- Ours gap(%): 5.1080
- best_score(ratio): 0.051080
- best曲线首末相对改善: 16.63%

## 2) 事件统计

- total_eval_events: 611
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 176
- eval_errors: 1
- LLM请求总耗时(秒): 428.13
- LLM请求平均耗时(秒): 13.38

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 32 | 63020 | 37316 | 428.13 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000504
- cost_input_miss_usd: $0.005042
- cost_output_usd: $0.004478

### default_4p0

- cost_input_hit_usd: $0.000441
- cost_input_miss_usd: $0.004411
- cost_output_usd: $0.003918

### optimistic_4p5

- cost_input_hit_usd: $0.000392
- cost_input_miss_usd: $0.003921
- cost_output_usd: $0.003483

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 215.93 |
| refine | 16 | 212.20 |

