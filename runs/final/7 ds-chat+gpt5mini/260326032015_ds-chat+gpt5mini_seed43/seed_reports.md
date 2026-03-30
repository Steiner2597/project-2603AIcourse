# Seed实验统计报告: 260326032015_ds-chat+gpt5mini_seed43

## 1) 运行概览

- 分组: 7 ds-chat+gpt5mini
- seed: 43
- provider_tag: ds-chat+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T03:20:15
- 结束时间: 2026-03-26T04:50:15
- 总耗时(秒): 5400.00
- Ours gap(%): 6.1357
- best_score(ratio): 0.061357
- best曲线首末相对改善: 1.80%

## 2) 事件统计

- total_eval_events: 701
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 208
- eval_errors: 0
- LLM请求总耗时(秒): 704.86
- LLM请求平均耗时(秒): 22.03

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 23364 | 13350 | 141.99 |
| gpt-5-mini | 16 | 25983 | 15650 | 562.87 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.000187
- cost_input_miss_usd: $0.001869
- cost_input_usd: $0.001856
- cost_output_usd: $0.010545

### default_4p0

- cost_input_hit_usd: $0.000164
- cost_input_miss_usd: $0.001635
- cost_input_usd: $0.001624
- cost_output_usd: $0.009227

### optimistic_4p5

- cost_input_hit_usd: $0.000145
- cost_input_miss_usd: $0.001454
- cost_input_usd: $0.001443
- cost_output_usd: $0.008202

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 141.99 |
| refine | 16 | 562.87 |

