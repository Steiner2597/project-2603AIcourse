# Checkpoint Summary

- run_dir: runs\260325122756_or_parts_ds\subruns\260325124738_or_ds
- generated_at: 2026-03-25T15:14:57

## Overall

| Metric | Value |
|---|---:|
| eval_events | 618 |
| accepted | 346 |
| dedup_expr_hit | 164 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 78 | 21 | 23 | 0 | 7.705% | 0 | 0 |  |
| 0 | 1 | 109 | 21 | 40 | 0 | 8.226% | 0 | 0 |  |
| 1 | 0 | 37 | 19 | 14 | 0 | 6.827% | 2 | 0 | 9.779 |
| 1 | 1 | 25 | 19 | 3 | 0 | 6.287% | 2 | 0 | 12.463 |
| 2 | 0 | 33 | 19 | 5 | 0 | 6.832% | 2 | 0 | 11.019 |
| 2 | 1 | 30 | 19 | 4 | 0 | 6.506% | 2 | 0 | 14.804 |
| 3 | 0 | 24 | 19 | 5 | 0 | 7.332% | 2 | 0 | 13.470 |
| 3 | 1 | 27 | 19 | 8 | 0 | 6.447% | 2 | 0 | 12.586 |
| 4 | 0 | 26 | 19 | 7 | 0 | 5.879% | 2 | 0 | 25.548 |
| 4 | 1 | 27 | 19 | 8 | 0 | 5.763% | 2 | 0 | 15.916 |
| 5 | 0 | 26 | 19 | 6 | 0 | 4.988% | 2 | 0 | 17.674 |
| 5 | 1 | 33 | 19 | 14 | 0 | 6.856% | 2 | 0 | 14.445 |
| 6 | 0 | 23 | 19 | 4 | 0 | 5.089% | 2 | 0 | 12.743 |
| 6 | 1 | 21 | 19 | 2 | 0 | 5.970% | 2 | 0 | 19.253 |
| 7 | 0 | 25 | 19 | 6 | 0 | 5.538% | 2 | 0 | 18.067 |
| 7 | 1 | 21 | 19 | 2 | 0 | 5.497% | 2 | 0 | 16.936 |
| 8 | 0 | 25 | 19 | 5 | 0 | 5.036% | 2 | 0 | 13.619 |
| 8 | 1 | 28 | 19 | 8 | 0 | 5.014% | 2 | 0 | 20.380 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 208.8500 | 3.80 | 1.57 | 1.94 | 29.23 | 33.80 |
| Best-Fit (BF) | 212.0000 | 5.37 | 0.00 | 0.37 | 0.00 | 6.45 |
| First-Fit (FF) | 212.7500 | 5.74 | -0.37 | 0.00 | -6.90 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
