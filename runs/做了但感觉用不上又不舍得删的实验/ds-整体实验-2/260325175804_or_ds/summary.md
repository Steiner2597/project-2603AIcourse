# Checkpoint Summary

- run_dir: runs\260325175804_or_ds
- generated_at: 2026-03-25T19:26:16

## Overall

| Metric | Value |
|---|---:|
| eval_events | 551 |
| accepted | 346 |
| dedup_expr_hit | 127 |
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
| 1 | 0 | 34 | 19 | 6 | 0 | 8.420% | 2 | 0 | 10.033 |
| 1 | 1 | 52 | 19 | 18 | 0 | 7.013% | 2 | 0 | 10.435 |
| 2 | 0 | 46 | 19 | 19 | 0 | 7.167% | 2 | 0 | 10.197 |
| 2 | 1 | 29 | 19 | 3 | 0 | 6.788% | 2 | 0 | 9.936 |
| 3 | 0 | 25 | 19 | 6 | 0 | 6.650% | 2 | 0 | 14.504 |
| 3 | 1 | 24 | 19 | 4 | 0 | 6.540% | 2 | 0 | 12.393 |
| 4 | 0 | 22 | 19 | 3 | 0 | 6.580% | 2 | 0 | 11.102 |
| 4 | 1 | 24 | 19 | 4 | 0 | 6.268% | 2 | 0 | 10.538 |
| 5 | 0 | 23 | 19 | 4 | 0 | 6.472% | 2 | 0 | 10.838 |
| 5 | 1 | 27 | 19 | 6 | 0 | 6.234% | 2 | 0 | 24.926 |
| 6 | 0 | 26 | 19 | 7 | 0 | 5.843% | 2 | 0 | 15.728 |
| 6 | 1 | 28 | 19 | 7 | 0 | 6.745% | 2 | 0 | 21.523 |
| 7 | 0 | 22 | 19 | 3 | 0 | 6.213% | 2 | 0 | 13.705 |
| 7 | 1 | 22 | 19 | 3 | 0 | 6.622% | 2 | 0 | 14.454 |
| 8 | 0 | 28 | 19 | 9 | 0 | 6.247% | 2 | 0 | 10.672 |
| 8 | 1 | 24 | 19 | 2 | 0 | 6.411% | 2 | 0 | 57.773 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.0750 | 5.35 | 0.90 | 1.04 | 14.44 | 16.31 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
