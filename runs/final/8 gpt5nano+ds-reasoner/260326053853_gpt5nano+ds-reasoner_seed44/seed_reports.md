# Seed实验统计报告: 260326053853_gpt5nano+ds-reasoner_seed44

## 1) 运行概览

- 分组: 8 gpt5nano+ds-reasoner
- seed: 44
- provider_tag: gpt5nano+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T05:38:53
- 结束时间: 2026-03-26T07:19:24
- 总耗时(秒): 6031.00
- Ours gap(%): 4.7926
- best_score(ratio): 0.047926
- best曲线首末相对改善: 10.78%

## 2) 事件统计

- total_eval_events: 573
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 155
- eval_errors: 0
- LLM请求总耗时(秒): 1971.17
- LLM请求平均耗时(秒): 61.60

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 16 | 55010 | 6153 | 1500.09 |
| gpt-5-nano | 16 | 42942 | 12171 | 471.08 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.002200
- cost_input_miss_usd: $0.008644
- cost_input_usd: $0.000613
- cost_output_usd: $0.005241

### default_4p0

- cost_input_hit_usd: $0.001925
- cost_input_miss_usd: $0.007564
- cost_input_usd: $0.000537
- cost_output_usd: $0.004586

### optimistic_4p5

- cost_input_hit_usd: $0.001711
- cost_input_miss_usd: $0.006723
- cost_input_usd: $0.000477
- cost_output_usd: $0.004076

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 471.08 |
| refine | 16 | 1500.09 |

