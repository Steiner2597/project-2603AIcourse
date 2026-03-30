# Checkpoint Summary

- run_dir: runs\260325115953_or_ds
- generated_at: 2026-03-25T13:58:25

## Overall

| Metric | Value |
|---|---:|
| eval_events | 571 |
| accepted | 346 |
| dedup_expr_hit | 147 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 46 | 21 | 8 | 0 | 8.310% | 0 | 0 |  |
| 0 | 1 | 49 | 21 | 15 | 0 | 7.938% | 0 | 0 |  |
| 1 | 0 | 46 | 19 | 17 | 0 | 8.426% | 2 | 0 | 10.839 |
| 1 | 1 | 50 | 19 | 18 | 0 | 6.353% | 2 | 0 | 8.329 |
| 2 | 0 | 38 | 19 | 10 | 0 | 7.957% | 2 | 0 | 13.643 |
| 2 | 1 | 27 | 19 | 7 | 0 | 6.823% | 2 | 0 | 10.150 |
| 3 | 0 | 27 | 19 | 8 | 0 | 7.245% | 2 | 0 | 15.852 |
| 3 | 1 | 22 | 19 | 3 | 0 | 6.524% | 2 | 0 | 8.001 |
| 4 | 0 | 25 | 19 | 6 | 0 | 7.130% | 2 | 0 | 11.427 |
| 4 | 1 | 30 | 19 | 7 | 0 | 6.250% | 2 | 0 | 6.247 |
| 5 | 0 | 23 | 19 | 3 | 0 | 6.655% | 2 | 0 | 10.744 |
| 5 | 1 | 30 | 19 | 9 | 0 | 6.512% | 2 | 0 | 11.575 |
| 6 | 0 | 23 | 19 | 3 | 0 | 5.898% | 2 | 0 | 10.893 |
| 6 | 1 | 26 | 19 | 4 | 0 | 6.714% | 2 | 0 | 12.008 |
| 7 | 0 | 25 | 19 | 6 | 0 | 5.865% | 2 | 0 | 15.856 |
| 7 | 1 | 25 | 19 | 6 | 0 | 6.304% | 2 | 0 | 12.899 |
| 8 | 0 | 28 | 19 | 7 | 0 | 6.369% | 2 | 0 | 13.484 |
| 8 | 1 | 31 | 19 | 10 | 0 | 6.377% | 2 | 0 | 23.523 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.1188 | 5.55 | 0.70 | 0.84 | 11.15 | 13.09 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
