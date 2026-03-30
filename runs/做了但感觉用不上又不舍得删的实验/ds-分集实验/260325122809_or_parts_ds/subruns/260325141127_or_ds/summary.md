# Checkpoint Summary

- run_dir: runs\260325122809_or_parts_ds\subruns\260325141127_or_ds
- generated_at: 2026-03-25T15:17:30

## Overall

| Metric | Value |
|---|---:|
| eval_events | 580 |
| accepted | 346 |
| dedup_expr_hit | 142 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 71 | 21 | 11 | 0 | 6.417% | 0 | 0 |  |
| 0 | 1 | 68 | 21 | 28 | 0 | 6.225% | 0 | 0 |  |
| 1 | 0 | 31 | 19 | 7 | 0 | 6.008% | 2 | 0 | 10.845 |
| 1 | 1 | 27 | 19 | 3 | 0 | 5.843% | 2 | 0 | 8.110 |
| 2 | 0 | 32 | 19 | 9 | 0 | 5.828% | 2 | 0 | 11.373 |
| 2 | 1 | 29 | 19 | 8 | 0 | 5.254% | 2 | 0 | 8.729 |
| 3 | 0 | 32 | 19 | 11 | 0 | 5.441% | 2 | 0 | 10.795 |
| 3 | 1 | 27 | 19 | 7 | 0 | 4.975% | 2 | 0 | 10.046 |
| 4 | 0 | 22 | 19 | 2 | 0 | 5.384% | 2 | 0 | 12.204 |
| 4 | 1 | 21 | 19 | 2 | 0 | 4.927% | 2 | 0 | 15.453 |
| 5 | 0 | 29 | 19 | 10 | 0 | 5.479% | 2 | 0 | 14.666 |
| 5 | 1 | 33 | 19 | 12 | 0 | 4.841% | 2 | 0 | 20.400 |
| 6 | 0 | 26 | 19 | 6 | 0 | 5.266% | 2 | 0 | 15.408 |
| 6 | 1 | 34 | 19 | 7 | 0 | 5.396% | 2 | 0 | 24.490 |
| 7 | 0 | 26 | 19 | 6 | 0 | 5.431% | 2 | 0 | 11.704 |
| 7 | 1 | 28 | 19 | 8 | 0 | 5.450% | 2 | 0 | 16.380 |
| 8 | 0 | 22 | 19 | 2 | 0 | 5.231% | 2 | 0 | 19.401 |
| 8 | 1 | 22 | 19 | 3 | 0 | 5.032% | 2 | 0 | 28.519 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 140.5312 | 5.98 | 0.27 | 0.41 | 4.25 | 6.34 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
