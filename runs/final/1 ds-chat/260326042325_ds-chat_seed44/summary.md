# Checkpoint Summary

- run_dir: runs\260326042325_ds-chat_seed44
- generated_at: 2026-03-26T05:40:10

## Overall

| Metric | Value |
|---|---:|
| eval_events | 569 |
| accepted | 346 |
| dedup_expr_hit | 147 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 59 | 21 | 11 | 0 | 8.320% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 18 | 0 | 8.076% | 0 | 0 |  |
| 1 | 0 | 40 | 19 | 9 | 0 | 7.135% | 2 | 0 | 9.042 |
| 1 | 1 | 35 | 19 | 12 | 0 | 6.400% | 2 | 0 | 5.804 |
| 2 | 0 | 32 | 19 | 7 | 0 | 6.070% | 2 | 0 | 6.476 |
| 2 | 1 | 38 | 19 | 14 | 0 | 6.314% | 2 | 0 | 6.063 |
| 3 | 0 | 33 | 19 | 12 | 0 | 5.795% | 2 | 0 | 8.208 |
| 3 | 1 | 27 | 19 | 6 | 0 | 6.562% | 2 | 0 | 7.692 |
| 4 | 0 | 23 | 19 | 4 | 0 | 6.428% | 2 | 0 | 7.909 |
| 4 | 1 | 20 | 19 | 1 | 0 | 5.834% | 2 | 0 | 6.918 |
| 5 | 0 | 29 | 19 | 10 | 0 | 5.662% | 2 | 0 | 7.879 |
| 5 | 1 | 26 | 19 | 6 | 0 | 5.734% | 2 | 0 | 8.526 |
| 6 | 0 | 27 | 19 | 8 | 0 | 5.712% | 2 | 0 | 10.934 |
| 6 | 1 | 31 | 19 | 8 | 0 | 5.610% | 2 | 0 | 7.881 |
| 7 | 0 | 24 | 19 | 4 | 0 | 5.546% | 2 | 0 | 8.962 |
| 7 | 1 | 26 | 19 | 7 | 0 | 6.188% | 2 | 0 | 10.354 |
| 8 | 0 | 22 | 19 | 3 | 0 | 6.175% | 2 | 0 | 9.386 |
| 8 | 1 | 26 | 19 | 7 | 0 | 5.760% | 2 | 0 | 11.622 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.7125 | 4.98 | 1.27 | 1.41 | 20.39 | 22.13 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
