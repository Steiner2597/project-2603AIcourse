# Checkpoint Summary

- run_dir: runs\260326111915_gpt5mini_seed45
- generated_at: 2026-03-26T12:53:19

## Overall

| Metric | Value |
|---|---:|
| eval_events | 658 |
| accepted | 346 |
| dedup_expr_hit | 194 |
| eval_errors | 2 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 50 | 21 | 10 | 0 | 8.209% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 11 | 0 | 8.297% | 0 | 0 |  |
| 1 | 0 | 50 | 19 | 18 | 0 | 6.775% | 2 | 0 | 27.910 |
| 1 | 1 | 39 | 19 | 10 | 0 | 7.074% | 2 | 0 | 27.831 |
| 2 | 0 | 47 | 19 | 14 | 0 | 6.952% | 2 | 0 | 21.439 |
| 2 | 1 | 30 | 19 | 5 | 0 | 7.034% | 2 | 0 | 26.875 |
| 3 | 0 | 23 | 19 | 3 | 0 | 6.049% | 2 | 0 | 36.827 |
| 3 | 1 | 30 | 19 | 7 | 0 | 6.706% | 2 | 0 | 27.340 |
| 4 | 0 | 29 | 19 | 9 | 0 | 6.118% | 2 | 0 | 32.364 |
| 4 | 1 | 56 | 19 | 24 | 0 | 6.904% | 2 | 0 | 30.430 |
| 5 | 0 | 25 | 19 | 5 | 1 | 5.915% | 2 | 0 | 30.140 |
| 5 | 1 | 34 | 19 | 12 | 0 | 6.761% | 2 | 0 | 33.907 |
| 6 | 0 | 30 | 19 | 9 | 1 | 5.656% | 2 | 0 | 22.886 |
| 6 | 1 | 31 | 19 | 8 | 0 | 7.007% | 2 | 0 | 29.218 |
| 7 | 0 | 34 | 19 | 12 | 0 | 5.700% | 2 | 0 | 28.963 |
| 7 | 1 | 32 | 19 | 13 | 0 | 6.765% | 2 | 0 | 25.093 |
| 8 | 0 | 24 | 19 | 5 | 0 | 6.071% | 2 | 0 | 41.246 |
| 8 | 1 | 43 | 19 | 19 | 0 | 6.481% | 2 | 0 | 31.922 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.2250 | 5.34 | 0.91 | 1.05 | 14.61 | 16.48 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
