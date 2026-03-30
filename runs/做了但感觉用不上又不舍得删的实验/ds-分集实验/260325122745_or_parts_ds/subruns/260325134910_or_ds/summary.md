# Checkpoint Summary

- run_dir: runs\260325122745_or_parts_ds\subruns\260325134910_or_ds
- generated_at: 2026-03-25T15:14:38

## Overall

| Metric | Value |
|---|---:|
| eval_events | 660 |
| accepted | 346 |
| dedup_expr_hit | 194 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 71 | 21 | 18 | 0 | 8.643% | 0 | 0 |  |
| 0 | 1 | 95 | 21 | 38 | 0 | 8.607% | 0 | 0 |  |
| 1 | 0 | 48 | 19 | 16 | 0 | 8.118% | 2 | 0 | 9.649 |
| 1 | 1 | 34 | 19 | 9 | 0 | 8.158% | 2 | 0 | 7.861 |
| 2 | 0 | 31 | 19 | 5 | 0 | 7.671% | 2 | 0 | 8.371 |
| 2 | 1 | 44 | 19 | 15 | 0 | 7.224% | 2 | 0 | 12.598 |
| 3 | 0 | 26 | 19 | 7 | 0 | 7.224% | 2 | 0 | 9.284 |
| 3 | 1 | 27 | 19 | 8 | 0 | 7.053% | 2 | 0 | 10.192 |
| 4 | 0 | 30 | 19 | 6 | 0 | 7.158% | 2 | 0 | 9.184 |
| 4 | 1 | 30 | 19 | 10 | 0 | 6.921% | 2 | 0 | 8.899 |
| 5 | 0 | 33 | 19 | 11 | 0 | 7.316% | 2 | 0 | 13.492 |
| 5 | 1 | 23 | 19 | 4 | 0 | 6.908% | 2 | 0 | 12.834 |
| 6 | 0 | 37 | 19 | 11 | 0 | 7.329% | 2 | 0 | 13.030 |
| 6 | 1 | 24 | 19 | 5 | 0 | 6.829% | 2 | 0 | 13.204 |
| 7 | 0 | 31 | 19 | 12 | 0 | 6.934% | 2 | 0 | 14.245 |
| 7 | 1 | 28 | 19 | 9 | 0 | 6.737% | 2 | 0 | 13.183 |
| 8 | 0 | 22 | 19 | 3 | 0 | 7.171% | 2 | 0 | 11.740 |
| 8 | 1 | 26 | 19 | 7 | 0 | 7.092% | 2 | 0 | 13.155 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 21.2500 | 6.25 | 2.25 | 1.75 | 26.47 | 21.88 |
| First-Fit (FF) | 21.6000 | 8.00 | 0.50 | 0.00 | 5.88 | 0.00 |
| Best-Fit (BF) | 21.7000 | 8.50 | 0.00 | -0.50 | 0.00 | -6.25 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
