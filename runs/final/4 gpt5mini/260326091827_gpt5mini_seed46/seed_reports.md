# Seed实验统计报告: 260326091827_gpt5mini_seed46

## 1) 运行概览

- 分组: 4 gpt5mini
- seed: 46
- provider_tag: gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T09:18:27
- 结束时间: 2026-03-26T10:50:22
- 总耗时(秒): 5515.00
- Ours gap(%): 4.9185
- best_score(ratio): 0.049185
- best曲线首末相对改善: 2.56%

## 2) 事件统计

- total_eval_events: 585
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 157
- eval_errors: 0
- LLM请求总耗时(秒): 972.83
- LLM请求平均耗时(秒): 30.40

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 32 | 76186 | 27308 | 972.83 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.005442
- cost_output_usd: $0.015605

### default_4p0

- cost_input_usd: $0.004762
- cost_output_usd: $0.013654

### optimistic_4p5

- cost_input_usd: $0.004233
- cost_output_usd: $0.012137

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 479.71 |
| refine | 16 | 493.12 |

