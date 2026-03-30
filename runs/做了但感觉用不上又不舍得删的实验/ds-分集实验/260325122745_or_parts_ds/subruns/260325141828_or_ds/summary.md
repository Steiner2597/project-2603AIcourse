# Checkpoint Summary

- run_dir: runs\260325122745_or_parts_ds\subruns\260325141828_or_ds
- generated_at: 2026-03-25T15:14:49

## Overall

| Metric | Value |
|---|---:|
| eval_events | 588 |
| accepted | 346 |
| dedup_expr_hit | 160 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 48 | 21 | 9 | 0 | 5.893% | 0 | 0 |  |
| 0 | 1 | 64 | 21 | 21 | 0 | 6.135% | 0 | 0 |  |
| 1 | 0 | 33 | 19 | 10 | 0 | 5.523% | 2 | 0 | 6.870 |
| 1 | 1 | 39 | 19 | 12 | 0 | 6.005% | 2 | 0 | 9.721 |
| 2 | 0 | 61 | 19 | 24 | 0 | 4.997% | 2 | 0 | 11.596 |
| 2 | 1 | 28 | 19 | 5 | 0 | 5.925% | 2 | 0 | 10.573 |
| 3 | 0 | 34 | 19 | 14 | 0 | 4.593% | 2 | 0 | 12.234 |
| 3 | 1 | 28 | 19 | 9 | 0 | 5.318% | 2 | 0 | 10.810 |
| 4 | 0 | 35 | 19 | 15 | 0 | 4.718% | 2 | 0 | 18.116 |
| 4 | 1 | 27 | 19 | 8 | 0 | 5.180% | 2 | 0 | 15.407 |
| 5 | 0 | 31 | 19 | 9 | 0 | 4.794% | 2 | 0 | 14.896 |
| 5 | 1 | 23 | 19 | 2 | 0 | 4.773% | 2 | 0 | 9.924 |
| 6 | 0 | 19 | 19 | 0 | 0 | 4.732% | 2 | 0 | 32.073 |
| 6 | 1 | 22 | 19 | 2 | 0 | 5.200% | 2 | 0 | 12.468 |
| 7 | 0 | 21 | 19 | 2 | 0 | 4.363% | 2 | 0 | 22.365 |
| 7 | 1 | 27 | 19 | 8 | 0 | 4.948% | 2 | 0 | 14.099 |
| 8 | 0 | 24 | 19 | 5 | 0 | 4.593% | 2 | 0 | 19.063 |
| 8 | 1 | 24 | 19 | 5 | 0 | 4.833% | 2 | 0 | 25.637 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 173.5000 | 3.89 | 2.04 | 2.01 | 34.34 | 34.01 |
| First-Fit (FF) | 176.8500 | 5.90 | 0.03 | 0.00 | 0.51 | 0.00 |
| Best-Fit (BF) | 176.9000 | 5.93 | 0.00 | -0.03 | 0.00 | -0.51 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
