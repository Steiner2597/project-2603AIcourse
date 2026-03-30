# Seed实验统计报告: 260326111915_gpt5mini_seed45

## 1) 运行概览

- 分组: 4 gpt5mini
- seed: 45
- provider_tag: gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T11:19:15
- 结束时间: 2026-03-26T12:53:04
- 总耗时(秒): 5629.00
- Ours gap(%): 5.3363
- best_score(ratio): 0.053363
- best曲线首末相对改善: 13.97%

## 2) 事件统计

- total_eval_events: 658
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 194
- eval_errors: 2
- LLM请求总耗时(秒): 948.78
- LLM请求平均耗时(秒): 29.65

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 32 | 45519 | 25285 | 948.78 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.003251
- cost_output_usd: $0.014449

### default_4p0

- cost_input_usd: $0.002845
- cost_output_usd: $0.012642

### optimistic_4p5

- cost_input_usd: $0.002529
- cost_output_usd: $0.011238

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 469.66 |
| refine | 16 | 479.12 |

