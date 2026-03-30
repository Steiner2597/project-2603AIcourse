# Checkpoint Summary

- run_dir: runs\260326111925_gpt5nano+gpt5mini_seed45
- generated_at: 2026-03-26T12:52:09

## Overall

| Metric | Value |
|---|---:|
| eval_events | 643 |
| accepted | 346 |
| dedup_expr_hit | 193 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 50 | 21 | 10 | 0 | 8.209% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 11 | 0 | 8.297% | 0 | 0 |  |
| 1 | 0 | 50 | 19 | 18 | 0 | 6.775% | 2 | 0 | 34.120 |
| 1 | 1 | 40 | 19 | 10 | 0 | 7.053% | 2 | 0 | 26.471 |
| 2 | 0 | 53 | 19 | 23 | 0 | 6.492% | 2 | 0 | 22.585 |
| 2 | 1 | 30 | 19 | 9 | 0 | 7.288% | 2 | 0 | 26.726 |
| 3 | 0 | 29 | 19 | 8 | 0 | 6.400% | 2 | 0 | 23.819 |
| 3 | 1 | 42 | 19 | 15 | 0 | 6.462% | 2 | 0 | 23.556 |
| 4 | 0 | 26 | 19 | 6 | 0 | 6.810% | 2 | 0 | 26.182 |
| 4 | 1 | 33 | 19 | 11 | 0 | 7.105% | 2 | 0 | 27.532 |
| 5 | 0 | 34 | 19 | 14 | 0 | 6.154% | 2 | 0 | 37.575 |
| 5 | 1 | 30 | 19 | 9 | 0 | 6.969% | 2 | 0 | 31.298 |
| 6 | 0 | 36 | 19 | 11 | 0 | 6.016% | 2 | 0 | 27.901 |
| 6 | 1 | 29 | 19 | 8 | 0 | 6.332% | 2 | 0 | 31.127 |
| 7 | 0 | 26 | 19 | 7 | 0 | 5.958% | 2 | 0 | 32.807 |
| 7 | 1 | 33 | 19 | 14 | 0 | 6.609% | 2 | 0 | 20.289 |
| 8 | 0 | 22 | 19 | 3 | 0 | 5.937% | 2 | 0 | 28.968 |
| 8 | 1 | 29 | 19 | 6 | 0 | 6.104% | 2 | 0 | 29.751 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.7625 | 5.09 | 1.16 | 1.30 | 18.51 | 20.29 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
