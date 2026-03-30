# Checkpoint Summary

- run_dir: runs\260326111931_ds-chat+ds-reasoner_seed45
- generated_at: 2026-03-26T13:16:45

## Overall

| Metric | Value |
|---|---:|
| eval_events | 630 |
| accepted | 346 |
| dedup_expr_hit | 185 |
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
| 1 | 0 | 55 | 19 | 21 | 0 | 6.783% | 2 | 0 | 89.101 |
| 1 | 1 | 47 | 19 | 13 | 0 | 6.854% | 2 | 0 | 49.767 |
| 2 | 0 | 54 | 19 | 20 | 0 | 6.541% | 2 | 0 | 105.961 |
| 2 | 1 | 39 | 19 | 14 | 0 | 6.771% | 2 | 0 | 45.446 |
| 3 | 0 | 29 | 19 | 8 | 0 | 6.214% | 2 | 0 | 95.493 |
| 3 | 1 | 34 | 19 | 14 | 0 | 7.549% | 2 | 0 | 103.316 |
| 4 | 0 | 28 | 19 | 8 | 0 | 6.892% | 2 | 0 | 148.028 |
| 4 | 1 | 32 | 19 | 13 | 0 | 6.505% | 2 | 0 | 73.660 |
| 5 | 0 | 23 | 19 | 4 | 0 | 6.996% | 2 | 0 | 89.667 |
| 5 | 1 | 30 | 19 | 10 | 0 | 6.496% | 2 | 0 | 80.963 |
| 6 | 0 | 27 | 19 | 6 | 0 | 5.792% | 2 | 0 | 91.410 |
| 6 | 1 | 30 | 19 | 9 | 0 | 6.996% | 2 | 0 | 45.999 |
| 7 | 0 | 24 | 19 | 5 | 0 | 5.894% | 2 | 0 | 71.553 |
| 7 | 1 | 29 | 19 | 10 | 0 | 6.339% | 2 | 0 | 73.903 |
| 8 | 0 | 26 | 19 | 6 | 0 | 6.326% | 2 | 0 | 45.580 |
| 8 | 1 | 22 | 19 | 3 | 0 | 6.300% | 2 | 0 | 44.102 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.2875 | 5.41 | 0.84 | 0.98 | 13.49 | 15.38 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
