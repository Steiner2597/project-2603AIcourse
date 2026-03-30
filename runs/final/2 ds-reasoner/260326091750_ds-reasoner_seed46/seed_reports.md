# Seed实验统计报告: 260326091750_ds-reasoner_seed46

## 1) 运行概览

- 分组: 2 ds-reasoner
- seed: 46
- provider_tag: ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T09:17:50
- 结束时间: 2026-03-26T11:49:57
- 总耗时(秒): 9127.00
- Ours gap(%): 4.8829
- best_score(ratio): 0.048829
- best曲线首末相对改善: 3.27%

## 2) 事件统计

- total_eval_events: 588
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 163
- eval_errors: 0
- LLM请求总耗时(秒): 4476.30
- LLM请求平均耗时(秒): 139.88

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-reasoner | 32 | 82739 | 12746 | 4476.30 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.003310
- cost_input_miss_usd: $0.013002
- cost_output_usd: $0.007975

### default_4p0

- cost_input_hit_usd: $0.002896
- cost_input_miss_usd: $0.011377
- cost_output_usd: $0.006978

### optimistic_4p5

- cost_input_hit_usd: $0.002574
- cost_input_miss_usd: $0.010113
- cost_output_usd: $0.006203

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 2405.04 |
| refine | 16 | 2071.26 |

