# Checkpoint Summary

- run_dir: runs\260326013708_gpt5nano_seed42
- generated_at: 2026-03-26T03:10:14

## Overall

| Metric | Value |
|---|---:|
| eval_events | 599 |
| accepted | 346 |
| dedup_expr_hit | 178 |
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
| 1 | 0 | 45 | 19 | 16 | 0 | 8.424% | 2 | 0 | 38.770 |
| 1 | 1 | 59 | 19 | 25 | 0 | 6.358% | 2 | 0 | 38.825 |
| 2 | 0 | 37 | 19 | 12 | 0 | 7.280% | 2 | 0 | 35.425 |
| 2 | 1 | 25 | 19 | 4 | 0 | 6.870% | 2 | 0 | 25.819 |
| 3 | 0 | 32 | 19 | 8 | 0 | 6.626% | 2 | 0 | 34.062 |
| 3 | 1 | 29 | 19 | 10 | 0 | 6.542% | 2 | 0 | 32.471 |
| 4 | 0 | 30 | 19 | 11 | 0 | 6.363% | 2 | 0 | 37.763 |
| 4 | 1 | 28 | 19 | 8 | 0 | 6.745% | 2 | 0 | 33.219 |
| 5 | 0 | 28 | 19 | 9 | 0 | 6.530% | 2 | 0 | 24.069 |
| 5 | 1 | 31 | 19 | 12 | 0 | 6.455% | 2 | 0 | 30.728 |
| 6 | 0 | 28 | 19 | 6 | 0 | 6.881% | 2 | 0 | 29.306 |
| 6 | 1 | 24 | 19 | 3 | 0 | 6.501% | 2 | 0 | 23.466 |
| 7 | 0 | 28 | 19 | 9 | 0 | 6.861% | 2 | 0 | 31.227 |
| 7 | 1 | 25 | 19 | 6 | 0 | 6.395% | 2 | 0 | 63.220 |
| 8 | 0 | 26 | 19 | 6 | 0 | 5.999% | 2 | 0 | 41.913 |
| 8 | 1 | 29 | 19 | 10 | 0 | 5.649% | 2 | 0 | 36.486 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.7125 | 5.02 | 1.23 | 1.37 | 19.63 | 21.38 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
