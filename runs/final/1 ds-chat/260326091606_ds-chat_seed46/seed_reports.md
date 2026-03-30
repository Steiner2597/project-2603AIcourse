# Seed实验统计报告: 260326091606_ds-chat_seed46

## 1) 运行概览

- 分组: 1 ds-chat
- seed: 46
- provider_tag: ds-chat
- 状态: completed
- 开始时间: 2026-03-26T09:16:06
- 结束时间: 2026-03-26T10:40:05
- 总耗时(秒): 5039.00
- Ours gap(%): 4.8515
- best_score(ratio): 0.048515
- best曲线首末相对改善: 3.85%

## 2) 事件统计

- total_eval_events: 579
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 150
- eval_errors: 0
- LLM请求总耗时(秒): 483.13
- LLM请求平均耗时(秒): 15.10

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 32 | 86513 | 41468 | 483.13 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000692
- cost_input_miss_usd: $0.006921
- cost_output_usd: $0.004976

### default_4p0

- cost_input_hit_usd: $0.000606
- cost_input_miss_usd: $0.006056
- cost_output_usd: $0.004354

### optimistic_4p5

- cost_input_hit_usd: $0.000538
- cost_input_miss_usd: $0.005383
- cost_output_usd: $0.003870

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 287.27 |
| refine | 16 | 195.86 |

