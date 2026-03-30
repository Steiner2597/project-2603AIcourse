# Seed实验统计报告: 260326013733_ds-chat+ds-reasoner_seed42

## 1) 运行概览

- 分组: 5 ds-chat+ds-reasoner
- seed: 42
- provider_tag: ds-chat+ds-reasoner
- 状态: completed
- 开始时间: 2026-03-26T01:37:33
- 结束时间: 2026-03-26T03:32:35
- 总耗时(秒): 6902.00
- Ours gap(%): 5.5924
- best_score(ratio): 0.055924
- best曲线首末相对改善: 8.53%

## 2) 事件统计

- total_eval_events: 630
- total_llm_events: 64
- llm_request_done: 32
- llm_request_error: 0
- accepted: 346
- dedup_expr_hit: 192
- eval_errors: 0
- LLM请求总耗时(秒): 2300.61
- LLM请求平均耗时(秒): 71.89

## 3) 分模型统计

| model | requests | prompt_chars | response_chars | elapsed_sec |
|---|---:|---:|---:|---:|
| deepseek-chat | 16 | 37101 | 15423 | 177.25 |
| deepseek-reasoner | 16 | 45088 | 6264 | 2123.37 |

## 4) 成本估算

说明: token 由 chars/token 估算，给出 3.5 / 4.0 / 4.5 三种情境。

### pessimistic_3p5

- cost_input_hit_usd: $0.002100
- cost_input_miss_usd: $0.010053
- cost_output_usd: $0.005770

### default_4p0

- cost_input_hit_usd: $0.001838
- cost_input_miss_usd: $0.008797
- cost_output_usd: $0.005049

### optimistic_4p5

- cost_input_hit_usd: $0.001634
- cost_input_miss_usd: $0.007819
- cost_output_usd: $0.004488

## 5) 分阶段耗时

| phase | requests | elapsed_sec |
|---|---:|---:|
| proposal | 16 | 177.25 |
| refine | 16 | 2123.37 |

