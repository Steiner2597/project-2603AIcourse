# Seed实验统计报告: 260326111925_gpt5nano+gpt5mini_seed45

## 1) 运行概览

- 分组: 6 gpt5nano+gpt5mini
- seed: 45
- provider_tag: gpt5nano+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T11:19:25
- 结束时间: 2026-03-26T12:51:53
- 总耗时(秒): 5548.00
- Ours gap(%): 5.0925
- best_score(ratio): 0.050925
- best曲线首末相对改善: 17.90%

## 2) 事件统计

- total_eval_events: 643
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 193
- eval_errors: 0
- LLM请求总耗时(秒): 901.41
- LLM请求平均耗时(秒): 28.17

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 16 | 39252 | 14325 | 414.97 |
| gpt-5-nano | 16 | 32194 | 8890 | 486.44 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.003264
- cost_output_usd: $0.009202

### default_4p0

- cost_input_usd: $0.002856
- cost_output_usd: $0.008051

### optimistic_4p5

- cost_input_usd: $0.002538
- cost_output_usd: $0.007157

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 486.44 |
| refine | 16 | 414.97 |

