# Seed实验统计报告: 260326013708_gpt5nano_seed42

## 1) 运行概览

- 分组: 3 gpt5nano
- seed: 42
- provider_tag: gpt5nano
- 状态: completed
- 开始时间: 2026-03-26T01:37:08
- 结束时间: 2026-03-26T03:09:59
- 总耗时(秒): 5571.00
- Ours gap(%): 5.0230
- best_score(ratio): 0.050230
- best曲线首末相对改善: 18.05%

## 2) 事件统计

- total_eval_events: 599
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 178
- eval_errors: 0
- LLM请求总耗时(秒): 1113.54
- LLM请求平均耗时(秒): 34.80

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-nano | 32 | 65508 | 19166 | 1113.54 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.000936
- cost_output_usd: $0.002190

### default_4p0

- cost_input_usd: $0.000819
- cost_output_usd: $0.001917

### optimistic_4p5

- cost_input_usd: $0.000728
- cost_output_usd: $0.001704

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 541.31 |
| refine | 16 | 572.23 |

