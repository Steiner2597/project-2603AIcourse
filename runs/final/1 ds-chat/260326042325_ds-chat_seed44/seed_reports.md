# Seed实验统计报告: 260326042325_ds-chat_seed44

## 1) 运行概览

- 分组: 1 ds-chat
- seed: 44
- provider_tag: ds-chat
- 状态: completed
- 开始时间: 2026-03-26T04:23:25
- 结束时间: 2026-03-26T05:39:54
- 总耗时(秒): 4589.00
- Ours gap(%): 4.9754
- best_score(ratio): 0.049754
- best曲线首末相对改善: 10.96%

## 2) 事件统计

- total_eval_events: 569
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 147
- eval_errors: 0
- LLM请求总耗时(秒): 267.31
- LLM请求平均耗时(秒): 8.35

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 32 | 55815 | 26094 | 267.31 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000447
- cost_input_miss_usd: $0.004465
- cost_output_usd: $0.003131

### default_4p0

- cost_input_hit_usd: $0.000391
- cost_input_miss_usd: $0.003907
- cost_output_usd: $0.002740

### optimistic_4p5

- cost_input_hit_usd: $0.000347
- cost_input_miss_usd: $0.003473
- cost_output_usd: $0.002435

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 149.66 |
| refine | 16 | 117.65 |

