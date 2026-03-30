# Checkpoint Summary

- run_dir: runs\260326111835_gpt5nano_seed45
- generated_at: 2026-03-26T12:53:57

## Overall

| Metric | Value |
|---|---:|
| eval_events | 607 |
| accepted | 346 |
| dedup_expr_hit | 160 |
| eval_errors | 2 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 50 | 21 | 10 | 0 | 8.209% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 11 | 0 | 8.297% | 0 | 0 |  |
| 1 | 0 | 50 | 19 | 18 | 0 | 6.775% | 2 | 0 | 37.024 |
| 1 | 1 | 39 | 19 | 10 | 0 | 7.030% | 2 | 0 | 30.611 |
| 2 | 0 | 58 | 19 | 18 | 0 | 6.954% | 2 | 0 | 26.428 |
| 2 | 1 | 28 | 19 | 4 | 1 | 6.613% | 2 | 0 | 42.847 |
| 3 | 0 | 25 | 19 | 4 | 0 | 6.396% | 2 | 0 | 36.012 |
| 3 | 1 | 22 | 19 | 2 | 0 | 6.915% | 2 | 0 | 27.990 |
| 4 | 0 | 27 | 19 | 7 | 0 | 6.363% | 2 | 0 | 23.018 |
| 4 | 1 | 29 | 19 | 8 | 0 | 6.680% | 2 | 0 | 31.788 |
| 5 | 0 | 31 | 19 | 9 | 0 | 5.663% | 2 | 0 | 28.672 |
| 5 | 1 | 34 | 19 | 12 | 0 | 5.814% | 2 | 0 | 48.602 |
| 6 | 0 | 30 | 19 | 11 | 0 | 5.895% | 2 | 0 | 41.852 |
| 6 | 1 | 32 | 19 | 12 | 0 | 5.722% | 2 | 0 | 27.260 |
| 7 | 0 | 24 | 19 | 5 | 0 | 5.905% | 2 | 0 | 43.200 |
| 7 | 1 | 21 | 19 | 2 | 0 | 5.892% | 2 | 0 | 37.510 |
| 8 | 0 | 33 | 19 | 13 | 1 | 5.746% | 2 | 0 | 39.707 |
| 8 | 1 | 23 | 19 | 4 | 0 | 6.154% | 2 | 0 | 27.699 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.5062 | 5.01 | 1.24 | 1.38 | 19.84 | 21.60 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
