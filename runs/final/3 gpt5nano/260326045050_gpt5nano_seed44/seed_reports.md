# Seed实验统计报告: 260326045050_gpt5nano_seed44

## 1) 运行概览

- 分组: 3 gpt5nano
- seed: 44
- provider_tag: gpt5nano
- 状态: completed
- 开始时间: 2026-03-26T04:50:50
- 结束时间: 2026-03-26T06:23:16
- 总耗时(秒): 5546.00
- Ours gap(%): 5.2725
- best_score(ratio): 0.052725
- best曲线首末相对改善: 1.85%

## 2) 事件统计

- total_eval_events: 577
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 161
- eval_errors: 3
- LLM请求总耗时(秒): 1182.06
- LLM请求平均耗时(秒): 36.94

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| gpt-5-nano | 32 | 108259 | 25552 | 1182.06 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_usd: $0.001547
- cost_output_usd: $0.002920

### default_4p0

- cost_input_usd: $0.001353
- cost_output_usd: $0.002555

### optimistic_4p5

- cost_input_usd: $0.001203
- cost_output_usd: $0.002271

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 450.86 |
| refine | 16 | 731.20 |

