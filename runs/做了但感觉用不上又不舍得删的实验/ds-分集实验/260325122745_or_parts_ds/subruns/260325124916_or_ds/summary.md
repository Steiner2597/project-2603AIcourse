# Checkpoint Summary

- run_dir: runs\260325122745_or_parts_ds\subruns\260325124916_or_ds
- generated_at: 2026-03-25T15:14:24

## Overall

| Metric | Value |
|---|---:|
| eval_events | 656 |
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
| 0 | 0 | 89 | 21 | 22 | 0 | 8.462% | 0 | 0 |  |
| 0 | 1 | 99 | 21 | 37 | 0 | 9.157% | 0 | 0 |  |
| 1 | 0 | 41 | 19 | 9 | 0 | 5.855% | 2 | 0 | 9.993 |
| 1 | 1 | 41 | 19 | 5 | 0 | 7.143% | 2 | 0 | 9.829 |
| 2 | 0 | 28 | 19 | 4 | 0 | 5.872% | 2 | 0 | 8.480 |
| 2 | 1 | 39 | 19 | 16 | 0 | 6.329% | 2 | 0 | 11.585 |
| 3 | 0 | 25 | 19 | 4 | 0 | 5.338% | 2 | 0 | 11.733 |
| 3 | 1 | 27 | 19 | 7 | 0 | 5.877% | 2 | 0 | 11.119 |
| 4 | 0 | 35 | 19 | 13 | 0 | 6.275% | 2 | 0 | 9.262 |
| 4 | 1 | 20 | 19 | 0 | 0 | 5.142% | 2 | 0 | 15.255 |
| 5 | 0 | 25 | 19 | 6 | 0 | 6.396% | 2 | 0 | 9.506 |
| 5 | 1 | 26 | 19 | 6 | 0 | 5.481% | 2 | 0 | 10.645 |
| 6 | 0 | 25 | 19 | 5 | 0 | 6.301% | 2 | 0 | 26.663 |
| 6 | 1 | 25 | 19 | 5 | 0 | 5.033% | 2 | 0 | 11.732 |
| 7 | 0 | 33 | 19 | 11 | 0 | 6.608% | 2 | 0 | 9.471 |
| 7 | 1 | 28 | 19 | 9 | 0 | 5.975% | 2 | 0 | 19.025 |
| 8 | 0 | 23 | 19 | 4 | 0 | 6.238% | 2 | 0 | 16.023 |
| 8 | 1 | 27 | 19 | 8 | 0 | 6.182% | 2 | 0 | 27.253 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 209.8500 | 4.30 | 1.07 | 1.44 | 19.95 | 25.12 |
| Best-Fit (BF) | 212.0000 | 5.37 | 0.00 | 0.37 | 0.00 | 6.45 |
| First-Fit (FF) | 212.7500 | 5.74 | -0.37 | 0.00 | -6.90 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
