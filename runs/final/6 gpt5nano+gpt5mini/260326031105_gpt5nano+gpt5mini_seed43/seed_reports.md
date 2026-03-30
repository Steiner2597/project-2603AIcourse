# Seed实验统计报告: 260326031105_gpt5nano+gpt5mini_seed43

## 1) 运行概览

- 分组: 6 gpt5nano+gpt5mini
- seed: 43
- provider_tag: gpt5nano+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T03:11:05
- 结束时间: 2026-03-26T04:47:45
- 总耗时(秒): 5800.00
- Ours gap(%): 4.8350
- best_score(ratio): 0.048350
- best曲线首末相对改善: 22.51%

## 2) 事件统计

- total_eval_events: 689
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 210
- eval_errors: 0
- LLM请求总耗时(秒): 1177.44
- LLM请求平均耗时(秒): 36.80

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 16 | 27105 | 13837 | 573.18 |
| gpt-5-nano | 16 | 24077 | 10610 | 604.26 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.002280
- cost_output_usd: $0.009119

### default_4p0

- cost_input_usd: $0.001995
- cost_output_usd: $0.007980

### optimistic_4p5

- cost_input_usd: $0.001773
- cost_output_usd: $0.007093

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 604.26 |
| refine | 16 | 573.18 |

