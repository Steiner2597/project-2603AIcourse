# Seed实验统计报告: 260326035225_ds-reasoner_seed43

## 1) 运行概览

- 分组: 2 ds-reasoner
- seed: 43
- provider_tag: ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T03:52:25
- 结束时间: 2026-03-26T06:11:23
- 总耗时(秒): 8338.00
- Ours gap(%): 6.2209
- best_score(ratio): 0.062209
- best曲线首末相对改善: 0.30%

## 2) 事件统计

- total_eval_events: 687
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 200
- eval_errors: 0
- LLM请求总耗时(秒): 3654.35
- LLM请求平均耗时(秒): 114.20

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 32 | 48538 | 9906 | 3654.35 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.001942
- cost_input_miss_usd: $0.007627
- cost_output_usd: $0.006198

### default_4p0

- cost_input_hit_usd: $0.001699
- cost_input_miss_usd: $0.006674
- cost_output_usd: $0.005424

### optimistic_4p5

- cost_input_hit_usd: $0.001510
- cost_input_miss_usd: $0.005932
- cost_output_usd: $0.004821

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 2084.03 |
| refine | 16 | 1570.32 |

