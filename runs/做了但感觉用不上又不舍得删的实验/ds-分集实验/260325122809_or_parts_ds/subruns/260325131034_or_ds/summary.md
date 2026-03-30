# Checkpoint Summary

- run_dir: runs\260325122809_or_parts_ds\subruns\260325131034_or_ds
- generated_at: 2026-03-25T15:16:43

## Overall

| Metric | Value |
|---|---:|
| eval_events | 632 |
| accepted | 346 |
| dedup_expr_hit | 168 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 104 | 21 | 25 | 0 | 8.151% | 0 | 0 |  |
| 0 | 1 | 81 | 21 | 27 | 0 | 8.128% | 0 | 0 |  |
| 1 | 0 | 27 | 19 | 8 | 0 | 6.121% | 2 | 0 | 6.831 |
| 1 | 1 | 27 | 19 | 3 | 0 | 5.743% | 2 | 0 | 10.393 |
| 2 | 0 | 28 | 19 | 8 | 0 | 4.496% | 2 | 0 | 9.615 |
| 2 | 1 | 35 | 19 | 11 | 0 | 6.207% | 2 | 0 | 9.753 |
| 3 | 0 | 23 | 19 | 3 | 0 | 4.588% | 2 | 0 | 12.248 |
| 3 | 1 | 23 | 19 | 4 | 0 | 4.560% | 2 | 0 | 11.491 |
| 4 | 0 | 22 | 19 | 3 | 0 | 5.347% | 2 | 0 | 16.078 |
| 4 | 1 | 26 | 19 | 7 | 0 | 6.630% | 2 | 0 | 11.670 |
| 5 | 0 | 31 | 19 | 10 | 0 | 4.413% | 2 | 0 | 23.132 |
| 5 | 1 | 29 | 19 | 8 | 0 | 4.953% | 2 | 0 | 8.739 |
| 6 | 0 | 25 | 19 | 6 | 0 | 5.870% | 2 | 0 | 20.442 |
| 6 | 1 | 40 | 19 | 13 | 0 | 5.066% | 2 | 0 | 9.733 |
| 7 | 0 | 33 | 19 | 14 | 0 | 5.455% | 2 | 0 | 12.697 |
| 7 | 1 | 26 | 19 | 7 | 0 | 5.889% | 2 | 0 | 10.977 |
| 8 | 0 | 23 | 19 | 3 | 1 | 5.335% | 2 | 0 | 15.986 |
| 8 | 1 | 29 | 19 | 8 | 0 | 6.313% | 2 | 0 | 12.034 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.0625 | 5.64 | 0.61 | 0.75 | 9.81 | 11.78 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
