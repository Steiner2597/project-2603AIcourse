# Seed实验统计报告: 260326013725_gpt5nano+gpt5mini_seed42

## 1) 运行概览

- 分组: 6 gpt5nano+gpt5mini
- seed: 42
- provider_tag: gpt5nano+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T01:37:25
- 结束时间: 2026-03-26T03:10:26
- 总耗时(秒): 5581.00
- Ours gap(%): 4.9918
- best_score(ratio): 0.049918
- best曲线首末相对改善: 11.80%

## 2) 事件统计

- total_eval_events: 615
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 179
- eval_errors: 0
- LLM请求总耗时(秒): 1050.68
- LLM请求平均耗时(秒): 32.83

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 16 | 34477 | 12574 | 519.22 |
| gpt-5-nano | 16 | 29431 | 7655 | 531.46 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.002883
- cost_output_usd: $0.008060

### default_4p0

- cost_input_usd: $0.002523
- cost_output_usd: $0.007052

### optimistic_4p5

- cost_input_usd: $0.002242
- cost_output_usd: $0.006269

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 531.46 |
| refine | 16 | 519.22 |

