# Seed实验统计报告: 260326031035_gpt5nano_seed43

## 1) 运行概览

- 分组: 3 gpt5nano
- seed: 43
- provider_tag: gpt5nano
- 状态: completed
- 开始时间: 2026-03-26T03:10:35
- 结束时间: 2026-03-26T04:50:09
- 总耗时(秒): 5974.00
- Ours gap(%): 6.2002
- best_score(ratio): 0.062002
- best曲线首末相对改善: 0.69%

## 2) 事件统计

- total_eval_events: 693
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 194
- eval_errors: 1
- LLM请求总耗时(秒): 1197.87
- LLM请求平均耗时(秒): 37.43

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-nano | 32 | 57464 | 24376 | 1197.87 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.000821
- cost_output_usd: $0.002786

### default_4p0

- cost_input_usd: $0.000718
- cost_output_usd: $0.002438

### optimistic_4p5

- cost_input_usd: $0.000638
- cost_output_usd: $0.002167

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 569.45 |
| refine | 16 | 628.42 |

