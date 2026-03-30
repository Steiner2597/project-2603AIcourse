# Checkpoint Summary

- run_dir: runs\260326091818_gpt5nano_seed46
- generated_at: 2026-03-26T10:59:19

## Overall

| Metric | Value |
|---|---:|
| eval_events | 569 |
| accepted | 346 |
| dedup_expr_hit | 143 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 43 | 21 | 5 | 0 | 8.008% | 0 | 0 |  |
| 0 | 1 | 53 | 21 | 14 | 0 | 8.675% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 16 | 0 | 6.704% | 2 | 0 | 18.909 |
| 1 | 1 | 39 | 19 | 9 | 0 | 7.402% | 2 | 0 | 24.475 |
| 2 | 0 | 39 | 19 | 14 | 0 | 5.825% | 2 | 0 | 28.715 |
| 2 | 1 | 34 | 19 | 6 | 0 | 7.183% | 2 | 0 | 33.688 |
| 3 | 0 | 37 | 19 | 15 | 0 | 5.760% | 2 | 0 | 62.620 |
| 3 | 1 | 26 | 19 | 5 | 0 | 6.434% | 2 | 0 | 29.844 |
| 4 | 0 | 28 | 19 | 9 | 0 | 5.858% | 2 | 0 | 50.128 |
| 4 | 1 | 23 | 19 | 4 | 0 | 6.548% | 2 | 0 | 52.953 |
| 5 | 0 | 24 | 19 | 5 | 0 | 5.452% | 2 | 0 | 34.473 |
| 5 | 1 | 31 | 19 | 9 | 0 | 7.145% | 2 | 0 | 35.436 |
| 6 | 0 | 24 | 19 | 4 | 0 | 5.741% | 2 | 0 | 58.502 |
| 6 | 1 | 28 | 19 | 6 | 0 | 5.886% | 2 | 0 | 43.037 |
| 7 | 0 | 26 | 19 | 6 | 0 | 5.500% | 2 | 0 | 92.584 |
| 7 | 1 | 25 | 19 | 6 | 0 | 6.574% | 2 | 0 | 53.455 |
| 8 | 0 | 25 | 19 | 5 | 1 | 6.067% | 2 | 0 | 63.390 |
| 8 | 1 | 25 | 19 | 5 | 0 | 5.429% | 2 | 0 | 62.282 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.5312 | 4.89 | 1.36 | 1.50 | 21.82 | 23.53 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
