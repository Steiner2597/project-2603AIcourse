# Seed实验统计报告: 260326015346_gpt5nano+ds-reasoner_seed42

## 1) 运行概览

- 分组: 8 gpt5nano+ds-reasoner
- seed: 42
- provider_tag: gpt5nano+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T01:53:46
- 结束时间: 2026-03-26T03:44:57
- 总耗时(秒): 6671.00
- Ours gap(%): 4.9672
- best_score(ratio): 0.049672
- best曲线首末相对改善: 17.38%

## 2) 事件统计

- total_eval_events: 568
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 139
- eval_errors: 2
- LLM请求总耗时(秒): 2245.52
- LLM请求平均耗时(秒): 70.17

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 16 | 27581 | 6065 | 1766.37 |
| gpt-5-nano | 16 | 24336 | 9585 | 479.15 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.001103
- cost_input_miss_usd: $0.004334
- cost_input_usd: $0.000348
- cost_output_usd: $0.004890

### default_4p0

- cost_input_hit_usd: $0.000965
- cost_input_miss_usd: $0.003792
- cost_input_usd: $0.000304
- cost_output_usd: $0.004279

### optimistic_4p5

- cost_input_hit_usd: $0.000858
- cost_input_miss_usd: $0.003371
- cost_input_usd: $0.000270
- cost_output_usd: $0.003804

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 479.15 |
| refine | 16 | 1766.37 |

