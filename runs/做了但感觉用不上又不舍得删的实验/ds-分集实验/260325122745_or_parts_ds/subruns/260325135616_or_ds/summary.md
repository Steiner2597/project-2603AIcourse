# Checkpoint Summary

- run_dir: runs\260325122745_or_parts_ds\subruns\260325135616_or_ds
- generated_at: 2026-03-25T15:14:39

## Overall

| Metric | Value |
|---|---:|
| eval_events | 580 |
| accepted | 346 |
| dedup_expr_hit | 143 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 57 | 21 | 11 | 0 | 7.274% | 0 | 0 |  |
| 0 | 1 | 63 | 21 | 20 | 0 | 7.446% | 0 | 0 |  |
| 1 | 0 | 33 | 19 | 4 | 0 | 6.888% | 2 | 0 | 8.670 |
| 1 | 1 | 29 | 19 | 6 | 0 | 7.204% | 2 | 0 | 9.783 |
| 2 | 0 | 34 | 19 | 9 | 0 | 6.441% | 2 | 0 | 9.995 |
| 2 | 1 | 29 | 19 | 6 | 0 | 6.730% | 2 | 0 | 10.162 |
| 3 | 0 | 22 | 19 | 3 | 0 | 6.250% | 2 | 0 | 14.296 |
| 3 | 1 | 30 | 19 | 10 | 0 | 6.099% | 2 | 0 | 10.689 |
| 4 | 0 | 20 | 19 | 1 | 0 | 6.164% | 2 | 0 | 9.345 |
| 4 | 1 | 23 | 19 | 3 | 0 | 6.178% | 2 | 0 | 11.599 |
| 5 | 0 | 25 | 19 | 5 | 0 | 5.928% | 2 | 0 | 27.742 |
| 5 | 1 | 45 | 19 | 20 | 0 | 5.467% | 2 | 0 | 10.508 |
| 6 | 0 | 34 | 19 | 9 | 0 | 6.092% | 2 | 0 | 21.257 |
| 6 | 1 | 28 | 19 | 5 | 0 | 5.638% | 2 | 0 | 11.449 |
| 7 | 0 | 27 | 19 | 8 | 0 | 6.007% | 2 | 0 | 13.459 |
| 7 | 1 | 25 | 19 | 5 | 0 | 5.658% | 2 | 0 | 13.256 |
| 8 | 0 | 27 | 19 | 8 | 0 | 5.664% | 2 | 0 | 32.761 |
| 8 | 1 | 29 | 19 | 10 | 0 | 5.770% | 2 | 0 | 13.950 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 41.9000 | 4.75 | 2.62 | 2.62 | 35.59 | 35.59 |
| First-Fit (FF) | 42.9500 | 7.38 | 0.00 | 0.00 | 0.00 | 0.00 |
| Best-Fit (BF) | 42.9500 | 7.38 | 0.00 | 0.00 | 0.00 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
