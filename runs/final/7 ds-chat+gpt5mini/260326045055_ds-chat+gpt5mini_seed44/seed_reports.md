# Seed实验统计报告: 260326045055_ds-chat+gpt5mini_seed44

## 1) 运行概览

- 分组: 7 ds-chat+gpt5mini
- seed: 44
- provider_tag: ds-chat+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T04:50:55
- 结束时间: 2026-03-26T06:15:22
- 总耗时(秒): 5067.00
- Ours gap(%): 5.2839
- best_score(ratio): 0.052839
- best曲线首末相对改善: 5.49%

## 2) 事件统计

- total_eval_events: 557
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 134
- eval_errors: 1
- LLM请求总耗时(秒): 728.43
- LLM请求平均耗时(秒): 22.76

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 30681 | 13549 | 138.13 |
| gpt-5-mini | 16 | 36635 | 19112 | 590.30 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000245
- cost_input_miss_usd: $0.002454
- cost_input_usd: $0.002617
- cost_output_usd: $0.012547

### default_4p0

- cost_input_hit_usd: $0.000215
- cost_input_miss_usd: $0.002148
- cost_input_usd: $0.002290
- cost_output_usd: $0.010979

### optimistic_4p5

- cost_input_hit_usd: $0.000191
- cost_input_miss_usd: $0.001909
- cost_input_usd: $0.002035
- cost_output_usd: $0.009759

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 138.13 |
| refine | 16 | 590.30 |

