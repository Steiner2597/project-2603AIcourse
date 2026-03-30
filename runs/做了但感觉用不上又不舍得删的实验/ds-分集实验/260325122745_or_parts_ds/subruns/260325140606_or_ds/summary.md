# Checkpoint Summary

- run_dir: runs\260325122745_or_parts_ds\subruns\260325140606_or_ds
- generated_at: 2026-03-25T15:14:42

## Overall

| Metric | Value |
|---|---:|
| eval_events | 605 |
| accepted | 346 |
| dedup_expr_hit | 169 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 52 | 21 | 11 | 0 | 6.256% | 0 | 0 |  |
| 0 | 1 | 58 | 21 | 20 | 0 | 6.437% | 0 | 0 |  |
| 1 | 0 | 43 | 19 | 13 | 0 | 6.084% | 2 | 0 | 8.036 |
| 1 | 1 | 39 | 19 | 8 | 0 | 6.103% | 2 | 0 | 10.763 |
| 2 | 0 | 32 | 19 | 8 | 0 | 5.986% | 2 | 0 | 10.960 |
| 2 | 1 | 31 | 19 | 5 | 0 | 5.602% | 2 | 0 | 14.155 |
| 3 | 0 | 23 | 19 | 4 | 0 | 5.805% | 2 | 0 | 10.097 |
| 3 | 1 | 30 | 19 | 9 | 0 | 5.095% | 2 | 0 | 10.753 |
| 4 | 0 | 29 | 19 | 10 | 0 | 5.450% | 2 | 0 | 14.645 |
| 4 | 1 | 29 | 19 | 5 | 0 | 4.746% | 2 | 0 | 11.154 |
| 5 | 0 | 30 | 19 | 8 | 0 | 5.276% | 2 | 0 | 17.976 |
| 5 | 1 | 34 | 19 | 11 | 0 | 4.807% | 2 | 0 | 12.441 |
| 6 | 0 | 27 | 19 | 8 | 0 | 5.507% | 2 | 0 | 12.372 |
| 6 | 1 | 33 | 19 | 11 | 0 | 4.902% | 2 | 0 | 16.252 |
| 7 | 0 | 35 | 19 | 15 | 0 | 5.178% | 2 | 0 | 9.556 |
| 7 | 1 | 28 | 19 | 9 | 0 | 4.899% | 2 | 0 | 13.530 |
| 8 | 0 | 25 | 19 | 6 | 0 | 5.330% | 2 | 0 | 22.148 |
| 8 | 1 | 27 | 19 | 8 | 0 | 4.734% | 2 | 0 | 17.692 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 86.4500 | 4.16 | 2.23 | 2.23 | 34.91 | 34.91 |
| First-Fit (FF) | 88.3000 | 6.39 | 0.00 | 0.00 | 0.00 | 0.00 |
| Best-Fit (BF) | 88.3000 | 6.39 | 0.00 | 0.00 | 0.00 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
