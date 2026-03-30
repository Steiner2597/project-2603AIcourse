# Checkpoint Summary

- run_dir: runs\260325122756_or_parts_ds\subruns\260325141618_or_ds
- generated_at: 2026-03-25T15:15:33

## Overall

| Metric | Value |
|---|---:|
| eval_events | 562 |
| accepted | 346 |
| dedup_expr_hit | 135 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 71 | 21 | 20 | 0 | 6.024% | 0 | 0 |  |
| 0 | 1 | 65 | 21 | 20 | 0 | 6.032% | 0 | 0 |  |
| 1 | 0 | 26 | 19 | 2 | 0 | 5.506% | 2 | 0 | 8.537 |
| 1 | 1 | 24 | 19 | 3 | 0 | 5.742% | 2 | 0 | 8.979 |
| 2 | 0 | 29 | 19 | 5 | 0 | 5.243% | 2 | 0 | 9.224 |
| 2 | 1 | 30 | 19 | 8 | 0 | 5.424% | 2 | 0 | 10.060 |
| 3 | 0 | 25 | 19 | 6 | 0 | 4.984% | 2 | 0 | 10.730 |
| 3 | 1 | 26 | 19 | 4 | 0 | 5.370% | 2 | 0 | 10.185 |
| 4 | 0 | 28 | 19 | 7 | 0 | 4.830% | 2 | 0 | 16.139 |
| 4 | 1 | 27 | 19 | 6 | 0 | 5.080% | 2 | 0 | 11.340 |
| 5 | 0 | 24 | 19 | 5 | 0 | 5.263% | 2 | 0 | 15.200 |
| 5 | 1 | 26 | 19 | 6 | 0 | 5.224% | 2 | 0 | 12.605 |
| 6 | 0 | 26 | 19 | 7 | 0 | 5.025% | 2 | 0 | 14.471 |
| 6 | 1 | 28 | 19 | 5 | 0 | 5.205% | 2 | 0 | 14.697 |
| 7 | 0 | 27 | 19 | 8 | 0 | 4.902% | 2 | 0 | 19.486 |
| 7 | 1 | 24 | 19 | 5 | 0 | 5.186% | 2 | 0 | 14.941 |
| 8 | 0 | 32 | 19 | 13 | 0 | 5.134% | 2 | 0 | 25.736 |
| 8 | 1 | 24 | 19 | 5 | 0 | 5.158% | 2 | 0 | 14.224 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |
| FunSearch-Lite (Ours) | 143.4062 | 7.75 | -1.50 | -1.36 | -23.95 | -21.24 |

- winner: Best-Fit (BF)
- chart: baseline_compare.png
