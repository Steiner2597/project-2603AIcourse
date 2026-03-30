# Checkpoint Summary

- run_dir: runs\260326031213_gpt5mini_seed43
- generated_at: 2026-03-26T04:52:07

## Overall

| Metric | Value |
|---|---:|
| eval_events | 745 |
| accepted | 346 |
| dedup_expr_hit | 224 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 62 | 21 | 18 | 0 | 7.957% | 0 | 0 |  |
| 0 | 1 | 55 | 21 | 13 | 0 | 8.188% | 0 | 0 |  |
| 1 | 0 | 35 | 19 | 7 | 0 | 7.148% | 2 | 0 | 39.413 |
| 1 | 1 | 63 | 19 | 22 | 0 | 7.117% | 2 | 0 | 35.461 |
| 2 | 0 | 44 | 19 | 11 | 0 | 6.739% | 2 | 0 | 38.772 |
| 2 | 1 | 75 | 19 | 26 | 0 | 7.324% | 2 | 0 | 26.312 |
| 3 | 0 | 44 | 19 | 19 | 0 | 6.793% | 2 | 0 | 35.922 |
| 3 | 1 | 34 | 19 | 10 | 0 | 6.477% | 2 | 0 | 44.008 |
| 4 | 0 | 39 | 19 | 11 | 0 | 6.678% | 2 | 0 | 40.442 |
| 4 | 1 | 31 | 19 | 9 | 0 | 6.594% | 2 | 0 | 47.511 |
| 5 | 0 | 37 | 19 | 10 | 0 | 6.509% | 2 | 0 | 37.963 |
| 5 | 1 | 29 | 19 | 7 | 0 | 6.348% | 2 | 0 | 39.857 |
| 6 | 0 | 28 | 19 | 6 | 0 | 7.278% | 2 | 0 | 33.873 |
| 6 | 1 | 34 | 19 | 12 | 0 | 6.859% | 2 | 0 | 25.733 |
| 7 | 0 | 37 | 19 | 14 | 0 | 6.505% | 2 | 0 | 23.587 |
| 7 | 1 | 30 | 19 | 11 | 0 | 7.034% | 2 | 0 | 32.515 |
| 8 | 0 | 35 | 19 | 9 | 0 | 6.505% | 2 | 0 | 33.099 |
| 8 | 1 | 33 | 19 | 9 | 0 | 6.278% | 2 | 0 | 23.513 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 140.2188 | 6.25 | 0.00 | 0.14 | 0.06 | 2.24 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
