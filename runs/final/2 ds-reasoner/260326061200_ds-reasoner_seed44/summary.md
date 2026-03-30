# Checkpoint Summary

- run_dir: runs\final\2 ds-reasoner\260326061200_ds-reasoner_seed44
- generated_at: 2026-03-26T09:42:22

## Overall

| Metric | Value |
|---|---:|
| eval_events | 586 |
| accepted | 348 |
| dedup_expr_hit | 155 |
| eval_errors | 0 |
| llm_events | 68 |
| llm_request_start | 33 |
| llm_request_done | 32 |
| llm_request_error | 1 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 59 | 21 | 11 | 0 | 8.320% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 18 | 0 | 8.076% | 0 | 0 |  |
| 1 | 0 | 34 | 19 | 10 | 0 | 7.163% | 2 | 0 | 55.127 |
| 1 | 1 | 35 | 19 | 7 | 0 | 6.356% | 2 | 0 | 96.867 |
| 2 | 0 | 34 | 19 | 8 | 0 | 6.604% | 2 | 0 | 69.630 |
| 2 | 1 | 30 | 19 | 9 | 0 | 6.339% | 2 | 0 | 98.615 |
| 3 | 0 | 31 | 19 | 9 | 0 | 6.503% | 2 | 0 | 129.093 |
| 3 | 1 | 28 | 19 | 6 | 0 | 6.790% | 2 | 0 | 150.559 |
| 4 | 0 | 27 | 19 | 8 | 0 | 5.776% | 2 | 0 | 112.081 |
| 4 | 1 | 32 | 19 | 11 | 0 | 6.343% | 2 | 0 | 125.434 |
| 5 | 0 | 21 | 19 | 2 | 0 | 5.843% | 2 | 0 | 109.064 |
| 5 | 1 | 29 | 19 | 6 | 0 | 7.097% | 2 | 0 | 114.543 |
| 6 | 0 | 31 | 19 | 9 | 0 | 6.014% | 2 | 0 | 86.739 |
| 6 | 1 | 34 | 19 | 15 | 0 | 6.774% | 2 | 0 | 113.177 |
| 7 | 0 | 24 | 21 | 2 | 0 | 6.378% | 3 | 1 | 110.614 |
| 7 | 1 | 29 | 19 | 10 | 0 | 6.636% | 2 | 0 | 106.488 |
| 8 | 0 | 27 | 19 | 6 | 0 | 6.237% | 2 | 0 | 118.683 |
| 8 | 1 | 30 | 19 | 8 | 0 | 5.800% | 2 | 0 | 130.763 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.6375 | 4.95 | 1.30 | 1.44 | 20.81 | 22.54 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
