# Checkpoint Summary

- run_dir: runs\260326111944_ds-chat+gpt5mini_seed45
- generated_at: 2026-03-26T12:49:37

## Overall

| Metric | Value |
|---|---:|
| eval_events | 667 |
| accepted | 346 |
| dedup_expr_hit | 202 |
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
| 1 | 0 | 50 | 19 | 19 | 0 | 7.036% | 2 | 0 | 18.654 |
| 1 | 1 | 43 | 19 | 15 | 0 | 7.051% | 2 | 0 | 20.323 |
| 2 | 0 | 42 | 19 | 19 | 0 | 6.278% | 2 | 0 | 16.822 |
| 2 | 1 | 48 | 19 | 14 | 0 | 6.625% | 2 | 0 | 26.069 |
| 3 | 0 | 27 | 19 | 5 | 0 | 6.532% | 2 | 0 | 20.454 |
| 3 | 1 | 25 | 19 | 2 | 0 | 6.317% | 2 | 0 | 22.841 |
| 4 | 0 | 29 | 19 | 9 | 0 | 6.393% | 2 | 0 | 19.659 |
| 4 | 1 | 45 | 19 | 16 | 0 | 7.031% | 2 | 0 | 23.122 |
| 5 | 0 | 24 | 19 | 4 | 0 | 6.507% | 2 | 0 | 21.005 |
| 5 | 1 | 34 | 19 | 13 | 0 | 7.368% | 2 | 0 | 18.638 |
| 6 | 0 | 34 | 19 | 15 | 0 | 6.232% | 2 | 0 | 29.559 |
| 6 | 1 | 57 | 19 | 19 | 0 | 6.932% | 2 | 0 | 22.014 |
| 7 | 0 | 24 | 19 | 5 | 0 | 6.297% | 2 | 0 | 22.483 |
| 7 | 1 | 30 | 19 | 10 | 0 | 6.030% | 2 | 0 | 18.079 |
| 8 | 0 | 26 | 19 | 7 | 0 | 6.078% | 2 | 0 | 22.767 |
| 8 | 1 | 28 | 19 | 9 | 0 | 5.936% | 2 | 0 | 26.175 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.6312 | 5.47 | 0.78 | 0.92 | 12.47 | 14.38 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
