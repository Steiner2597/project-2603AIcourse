# Checkpoint Summary

- run_dir: runs\260326013725_gpt5nano+gpt5mini_seed42
- generated_at: 2026-03-26T03:10:42

## Overall

| Metric | Value |
|---|---:|
| eval_events | 615 |
| accepted | 346 |
| dedup_expr_hit | 179 |
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
| 1 | 0 | 38 | 19 | 15 | 0 | 8.646% | 2 | 0 | 38.752 |
| 1 | 1 | 46 | 19 | 15 | 0 | 6.518% | 2 | 0 | 26.979 |
| 2 | 0 | 47 | 19 | 15 | 0 | 7.551% | 2 | 0 | 31.029 |
| 2 | 1 | 43 | 19 | 7 | 0 | 6.519% | 2 | 0 | 25.185 |
| 3 | 0 | 31 | 19 | 11 | 0 | 6.220% | 2 | 0 | 36.634 |
| 3 | 1 | 22 | 19 | 3 | 0 | 6.801% | 2 | 0 | 35.177 |
| 4 | 0 | 25 | 19 | 5 | 0 | 6.165% | 2 | 0 | 32.385 |
| 4 | 1 | 31 | 19 | 11 | 0 | 6.512% | 2 | 0 | 35.374 |
| 5 | 0 | 34 | 19 | 14 | 0 | 5.797% | 2 | 0 | 22.369 |
| 5 | 1 | 25 | 19 | 6 | 0 | 6.999% | 2 | 0 | 30.031 |
| 6 | 0 | 32 | 19 | 11 | 0 | 5.829% | 2 | 0 | 32.032 |
| 6 | 1 | 38 | 19 | 11 | 0 | 6.730% | 2 | 0 | 38.776 |
| 7 | 0 | 24 | 19 | 5 | 0 | 5.525% | 2 | 0 | 30.937 |
| 7 | 1 | 28 | 19 | 9 | 0 | 6.475% | 2 | 0 | 27.965 |
| 8 | 0 | 31 | 19 | 12 | 0 | 5.351% | 2 | 0 | 40.573 |
| 8 | 1 | 25 | 19 | 6 | 0 | 5.995% | 2 | 0 | 41.142 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.8375 | 4.99 | 1.26 | 1.40 | 20.13 | 21.87 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
