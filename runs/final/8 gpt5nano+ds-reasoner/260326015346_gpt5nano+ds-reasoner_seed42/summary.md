# Checkpoint Summary

- run_dir: runs\260326015346_gpt5nano+ds-reasoner_seed42
- generated_at: 2026-03-26T03:45:14

## Overall

| Metric | Value |
|---|---:|
| eval_events | 568 |
| accepted | 346 |
| dedup_expr_hit | 139 |
| eval_errors | 2 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 46 | 21 | 8 | 0 | 8.310% | 0 | 0 |  |
| 0 | 1 | 49 | 21 | 15 | 0 | 7.938% | 0 | 0 |  |
| 1 | 0 | 38 | 19 | 15 | 0 | 8.584% | 2 | 0 | 48.180 |
| 1 | 1 | 48 | 19 | 14 | 0 | 6.525% | 2 | 0 | 73.370 |
| 2 | 0 | 36 | 19 | 8 | 0 | 7.216% | 2 | 0 | 80.915 |
| 2 | 1 | 33 | 19 | 4 | 0 | 6.476% | 2 | 0 | 48.853 |
| 3 | 0 | 27 | 19 | 8 | 0 | 6.506% | 2 | 0 | 133.406 |
| 3 | 1 | 24 | 19 | 5 | 0 | 6.250% | 2 | 0 | 71.782 |
| 4 | 0 | 27 | 19 | 6 | 0 | 5.846% | 2 | 0 | 39.275 |
| 4 | 1 | 28 | 19 | 8 | 0 | 6.469% | 2 | 0 | 65.391 |
| 5 | 0 | 28 | 19 | 8 | 0 | 6.243% | 2 | 0 | 69.154 |
| 5 | 1 | 23 | 19 | 3 | 0 | 6.236% | 2 | 0 | 79.983 |
| 6 | 0 | 27 | 19 | 5 | 0 | 5.858% | 2 | 0 | 97.888 |
| 6 | 1 | 26 | 19 | 7 | 0 | 6.728% | 2 | 0 | 62.841 |
| 7 | 0 | 25 | 19 | 2 | 1 | 5.913% | 2 | 0 | 73.127 |
| 7 | 1 | 27 | 19 | 7 | 0 | 6.033% | 2 | 0 | 55.189 |
| 8 | 0 | 32 | 19 | 12 | 1 | 5.625% | 2 | 0 | 71.949 |
| 8 | 1 | 24 | 19 | 4 | 0 | 6.189% | 2 | 0 | 51.458 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.7937 | 4.97 | 1.28 | 1.42 | 20.52 | 22.26 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
