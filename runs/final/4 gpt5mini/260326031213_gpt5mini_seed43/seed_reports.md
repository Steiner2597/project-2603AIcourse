# Seed实验统计报告: 260326031213_gpt5mini_seed43

## 1) 运行概览

- 分组: 4 gpt5mini
- seed: 43
- provider_tag: gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T03:12:13
- 结束时间: 2026-03-26T04:51:50
- 总耗时(秒): 5977.00
- Ours gap(%): 6.2458
- best_score(ratio): 0.062458
- best曲线首末相对改善: 0.06%

## 2) 事件统计

- total_eval_events: 745
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 224
- eval_errors: 0
- LLM请求总耗时(秒): 1115.96
- LLM请求平均耗时(秒): 34.87

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 32 | 76538 | 25250 | 1115.96 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.005467
- cost_output_usd: $0.014429

### default_4p0

- cost_input_usd: $0.004784
- cost_output_usd: $0.012625

### optimistic_4p5

- cost_input_usd: $0.004252
- cost_output_usd: $0.011222

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 530.08 |
| refine | 16 | 585.88 |

