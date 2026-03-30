# Checkpoint Summary

- run_dir: runs\260325175819_or_ds
- generated_at: 2026-03-25T19:30:59

## Overall

| Metric | Value |
|---|---:|
| eval_events | 687 |
| accepted | 346 |
| dedup_expr_hit | 173 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 62 | 21 | 18 | 0 | 7.957% | 0 | 0 |  |
| 0 | 1 | 55 | 21 | 13 | 0 | 8.188% | 0 | 0 |  |
| 1 | 0 | 42 | 19 | 9 | 0 | 7.394% | 2 | 0 | 9.848 |
| 1 | 1 | 59 | 19 | 18 | 0 | 7.847% | 2 | 0 | 8.075 |
| 2 | 0 | 38 | 19 | 7 | 0 | 7.260% | 2 | 0 | 11.453 |
| 2 | 1 | 48 | 19 | 13 | 0 | 7.624% | 2 | 0 | 8.978 |
| 3 | 0 | 57 | 19 | 20 | 0 | 7.019% | 2 | 0 | 9.526 |
| 3 | 1 | 28 | 19 | 8 | 0 | 6.942% | 2 | 0 | 10.800 |
| 4 | 0 | 40 | 19 | 13 | 0 | 7.014% | 2 | 0 | 9.344 |
| 4 | 1 | 22 | 19 | 2 | 0 | 7.330% | 2 | 0 | 9.026 |
| 5 | 0 | 48 | 19 | 13 | 0 | 6.298% | 2 | 0 | 12.753 |
| 5 | 1 | 27 | 19 | 5 | 0 | 6.426% | 2 | 0 | 9.268 |
| 6 | 0 | 34 | 19 | 6 | 0 | 6.542% | 2 | 0 | 14.488 |
| 6 | 1 | 24 | 19 | 2 | 0 | 7.180% | 2 | 0 | 8.971 |
| 7 | 0 | 25 | 19 | 5 | 0 | 6.836% | 2 | 0 | 16.230 |
| 7 | 1 | 30 | 19 | 11 | 0 | 6.863% | 2 | 0 | 14.343 |
| 8 | 0 | 25 | 19 | 6 | 0 | 6.410% | 2 | 0 | 15.234 |
| 8 | 1 | 23 | 19 | 4 | 0 | 6.058% | 2 | 0 | 11.105 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.7125 | 5.72 | 0.53 | 0.67 | 8.53 | 10.53 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
