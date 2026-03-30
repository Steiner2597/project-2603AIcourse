# Checkpoint Summary

- run_dir: runs\260325120014_or_ds
- generated_at: 2026-03-25T13:59:23

## Overall

| Metric | Value |
|---|---:|
| eval_events | 582 |
| accepted | 346 |
| dedup_expr_hit | 155 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 59 | 21 | 11 | 0 | 8.320% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 18 | 0 | 8.076% | 0 | 0 |  |
| 1 | 0 | 33 | 19 | 4 | 0 | 7.548% | 2 | 0 | 7.800 |
| 1 | 1 | 34 | 19 | 6 | 0 | 6.509% | 2 | 0 | 7.856 |
| 2 | 0 | 38 | 19 | 11 | 0 | 6.897% | 2 | 0 | 10.270 |
| 2 | 1 | 34 | 19 | 9 | 0 | 6.259% | 2 | 0 | 12.167 |
| 3 | 0 | 31 | 19 | 12 | 0 | 6.571% | 2 | 0 | 10.700 |
| 3 | 1 | 32 | 19 | 10 | 0 | 7.030% | 2 | 0 | 15.078 |
| 4 | 0 | 26 | 19 | 7 | 0 | 6.545% | 2 | 0 | 11.584 |
| 4 | 1 | 30 | 19 | 10 | 0 | 6.810% | 2 | 0 | 17.421 |
| 5 | 0 | 23 | 19 | 4 | 0 | 6.069% | 2 | 0 | 11.869 |
| 5 | 1 | 22 | 19 | 2 | 0 | 6.396% | 2 | 0 | 13.541 |
| 6 | 0 | 32 | 19 | 13 | 0 | 5.741% | 2 | 0 | 74.957 |
| 6 | 1 | 31 | 19 | 8 | 0 | 6.866% | 2 | 0 | 20.643 |
| 7 | 0 | 30 | 19 | 11 | 0 | 6.000% | 2 | 0 | 39.287 |
| 7 | 1 | 27 | 19 | 8 | 0 | 7.114% | 2 | 0 | 13.024 |
| 8 | 0 | 24 | 19 | 5 | 0 | 5.951% | 2 | 0 | 25.502 |
| 8 | 1 | 25 | 19 | 6 | 0 | 6.590% | 2 | 0 | 27.730 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.1875 | 5.18 | 1.07 | 1.21 | 17.06 | 18.87 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
