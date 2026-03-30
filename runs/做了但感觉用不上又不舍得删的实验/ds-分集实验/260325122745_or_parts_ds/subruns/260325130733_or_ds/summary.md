# Checkpoint Summary

- run_dir: runs\260325122745_or_parts_ds\subruns\260325130733_or_ds
- generated_at: 2026-03-25T15:14:37

## Overall

| Metric | Value |
|---|---:|
| eval_events | 616 |
| accepted | 346 |
| dedup_expr_hit | 152 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 95 | 21 | 24 | 0 | 8.217% | 0 | 0 |  |
| 0 | 1 | 78 | 21 | 23 | 0 | 8.376% | 0 | 0 |  |
| 1 | 0 | 36 | 19 | 6 | 0 | 6.784% | 2 | 0 | 9.534 |
| 1 | 1 | 29 | 19 | 7 | 0 | 5.634% | 2 | 0 | 7.630 |
| 2 | 0 | 27 | 19 | 2 | 0 | 5.521% | 2 | 0 | 8.390 |
| 2 | 1 | 30 | 19 | 9 | 0 | 6.147% | 2 | 0 | 17.364 |
| 3 | 0 | 23 | 19 | 3 | 0 | 6.286% | 2 | 0 | 11.351 |
| 3 | 1 | 25 | 19 | 6 | 0 | 5.152% | 2 | 0 | 11.690 |
| 4 | 0 | 34 | 19 | 12 | 0 | 6.008% | 2 | 0 | 14.433 |
| 4 | 1 | 28 | 19 | 9 | 0 | 5.574% | 2 | 0 | 18.208 |
| 5 | 0 | 29 | 19 | 7 | 0 | 5.070% | 2 | 0 | 9.506 |
| 5 | 1 | 26 | 19 | 6 | 0 | 4.502% | 2 | 0 | 15.168 |
| 6 | 0 | 30 | 19 | 8 | 0 | 5.846% | 2 | 0 | 23.652 |
| 6 | 1 | 26 | 19 | 7 | 0 | 4.296% | 2 | 0 | 19.253 |
| 7 | 0 | 27 | 19 | 8 | 0 | 5.183% | 2 | 0 | 9.887 |
| 7 | 1 | 23 | 19 | 3 | 0 | 4.576% | 2 | 0 | 18.054 |
| 8 | 0 | 25 | 19 | 6 | 0 | 5.084% | 2 | 0 | 26.696 |
| 8 | 1 | 25 | 19 | 6 | 0 | 5.801% | 2 | 0 | 12.206 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 415.7000 | 3.78 | 1.16 | 1.45 | 23.51 | 27.72 |
| Best-Fit (BF) | 420.3500 | 4.94 | 0.00 | 0.29 | 0.00 | 5.50 |
| First-Fit (FF) | 421.5000 | 5.23 | -0.29 | 0.00 | -5.83 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
