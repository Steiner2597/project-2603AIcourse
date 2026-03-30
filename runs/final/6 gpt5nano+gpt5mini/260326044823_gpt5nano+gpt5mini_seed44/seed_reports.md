# Seed实验统计报告: 260326044823_gpt5nano+gpt5mini_seed44

## 1) 运行概览

- 分组: 6 gpt5nano+gpt5mini
- seed: 44
- provider_tag: gpt5nano+gpt5mini
- 状态: completed
- 开始时间: 2026-03-26T04:48:23
- 结束时间: 2026-03-26T06:18:55
- 总耗时(秒): 5432.00
- Ours gap(%): 5.0244
- best_score(ratio): 0.050244
- best曲线首末相对改善: 10.13%

## 2) 事件统计

- total_eval_events: 584
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 144
- eval_errors: 0
- LLM请求总耗时(秒): 1049.84
- LLM请求平均耗时(秒): 32.81

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-mini | 16 | 32009 | 14242 | 548.27 |
| gpt-5-nano | 16 | 26863 | 10301 | 501.57 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.002670
- cost_output_usd: $0.009316

### default_4p0

- cost_input_usd: $0.002336
- cost_output_usd: $0.008151

### optimistic_4p5

- cost_input_usd: $0.002077
- cost_output_usd: $0.007245

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 501.57 |
| refine | 16 | 548.27 |

