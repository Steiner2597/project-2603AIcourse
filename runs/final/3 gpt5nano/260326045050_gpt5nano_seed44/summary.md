# Checkpoint Summary

- run_dir: runs\260326045050_gpt5nano_seed44
- generated_at: 2026-03-26T06:23:31

## Overall

| Metric | Value |
|---|---:|
| eval_events | 577 |
| accepted | 346 |
| dedup_expr_hit | 161 |
| eval_errors | 3 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 59 | 21 | 11 | 0 | 8.320% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 18 | 0 | 8.076% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 9 | 0 | 6.818% | 2 | 0 | 31.180 |
| 1 | 1 | 34 | 19 | 9 | 0 | 6.287% | 2 | 0 | 23.014 |
| 2 | 0 | 33 | 19 | 11 | 0 | 6.485% | 2 | 0 | 30.325 |
| 2 | 1 | 34 | 19 | 13 | 1 | 6.194% | 2 | 0 | 53.216 |
| 3 | 0 | 28 | 19 | 8 | 0 | 6.428% | 2 | 0 | 39.114 |
| 3 | 1 | 31 | 19 | 10 | 0 | 6.660% | 2 | 0 | 35.200 |
| 4 | 0 | 23 | 19 | 4 | 0 | 5.994% | 2 | 0 | 40.379 |
| 4 | 1 | 24 | 19 | 4 | 1 | 6.086% | 2 | 0 | 54.220 |
| 5 | 0 | 37 | 19 | 15 | 0 | 6.260% | 2 | 0 | 37.678 |
| 5 | 1 | 28 | 19 | 9 | 0 | 6.072% | 2 | 0 | 47.596 |
| 6 | 0 | 26 | 19 | 7 | 0 | 5.849% | 2 | 0 | 36.012 |
| 6 | 1 | 27 | 19 | 7 | 1 | 6.587% | 2 | 0 | 37.767 |
| 7 | 0 | 26 | 19 | 6 | 0 | 6.188% | 2 | 0 | 29.432 |
| 7 | 1 | 24 | 19 | 5 | 0 | 6.377% | 2 | 0 | 30.395 |
| 8 | 0 | 24 | 19 | 5 | 0 | 6.287% | 2 | 0 | 40.429 |
| 8 | 1 | 29 | 19 | 10 | 0 | 7.179% | 2 | 0 | 25.071 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.1188 | 5.27 | 0.98 | 1.12 | 15.63 | 17.48 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
