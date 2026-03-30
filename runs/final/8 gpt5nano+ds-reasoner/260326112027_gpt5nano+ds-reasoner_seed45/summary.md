# Checkpoint Summary

- run_dir: runs\260326112027_gpt5nano+ds-reasoner_seed45
- generated_at: 2026-03-26T13:15:02

## Overall

| Metric | Value |
|---|---:|
| eval_events | 613 |
| accepted | 346 |
| dedup_expr_hit | 171 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 50 | 21 | 10 | 0 | 8.209% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 11 | 0 | 8.297% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 11 | 0 | 6.746% | 2 | 0 | 47.218 |
| 1 | 1 | 36 | 19 | 5 | 0 | 6.390% | 2 | 0 | 72.763 |
| 2 | 0 | 49 | 19 | 22 | 0 | 6.626% | 2 | 0 | 53.437 |
| 2 | 1 | 50 | 19 | 16 | 0 | 6.408% | 2 | 0 | 83.566 |
| 3 | 0 | 23 | 19 | 2 | 0 | 6.603% | 2 | 0 | 116.206 |
| 3 | 1 | 30 | 19 | 8 | 0 | 6.700% | 2 | 0 | 73.466 |
| 4 | 0 | 26 | 19 | 7 | 0 | 6.971% | 2 | 0 | 66.609 |
| 4 | 1 | 26 | 19 | 5 | 0 | 7.120% | 2 | 0 | 124.402 |
| 5 | 0 | 30 | 19 | 9 | 0 | 6.476% | 2 | 0 | 97.294 |
| 5 | 1 | 34 | 19 | 11 | 0 | 6.483% | 2 | 0 | 64.453 |
| 6 | 0 | 28 | 19 | 9 | 0 | 6.049% | 2 | 0 | 79.095 |
| 6 | 1 | 28 | 19 | 9 | 0 | 6.236% | 2 | 0 | 74.519 |
| 7 | 0 | 24 | 19 | 5 | 0 | 5.753% | 2 | 0 | 64.748 |
| 7 | 1 | 28 | 19 | 8 | 0 | 6.905% | 2 | 0 | 44.555 |
| 8 | 0 | 33 | 19 | 14 | 0 | 6.344% | 2 | 0 | 55.728 |
| 8 | 1 | 28 | 19 | 9 | 0 | 6.494% | 2 | 0 | 78.958 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.8375 | 5.12 | 1.13 | 1.27 | 18.15 | 19.94 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
