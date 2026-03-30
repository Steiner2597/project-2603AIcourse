# Seed实验统计报告: 260326111835_gpt5nano_seed45

## 1) 运行概览

- 分组: 3 gpt5nano
- seed: 45
- provider_tag: gpt5nano
- 状态: completed
- 开始时间: 2026-03-26T11:18:35
- 结束时间: 2026-03-26T12:53:42
- 总耗时(秒): 5707.00
- Ours gap(%): 5.0094
- best_score(ratio): 0.050094
- best曲线首末相对改善: 13.52%

## 2) 事件统计

- total_eval_events: 607
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 160
- eval_errors: 2
- LLM请求总耗时(秒): 1100.44
- LLM请求平均耗时(秒): 34.39

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-nano | 32 | 52965 | 19327 | 1100.44 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.000757
- cost_output_usd: $0.002209

### default_4p0

- cost_input_usd: $0.000662
- cost_output_usd: $0.001933

### optimistic_4p5

- cost_input_usd: $0.000589
- cost_output_usd: $0.001718

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 464.16 |
| refine | 16 | 636.28 |

