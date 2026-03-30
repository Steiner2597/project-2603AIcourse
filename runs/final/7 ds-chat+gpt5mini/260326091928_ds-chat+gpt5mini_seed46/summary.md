# Checkpoint Summary

- run_dir: runs\260326091928_ds-chat+gpt5mini_seed46
- generated_at: 2026-03-26T10:48:31

## Overall

| Metric | Value |
|---|---:|
| eval_events | 586 |
| accepted | 346 |
| dedup_expr_hit | 165 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 43 | 21 | 5 | 0 | 8.008% | 0 | 0 |  |
| 0 | 1 | 53 | 21 | 14 | 0 | 8.675% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 16 | 0 | 6.470% | 2 | 0 | 23.210 |
| 1 | 1 | 39 | 19 | 9 | 0 | 7.402% | 2 | 0 | 23.958 |
| 2 | 0 | 38 | 19 | 13 | 0 | 6.129% | 2 | 0 | 29.136 |
| 2 | 1 | 44 | 19 | 15 | 0 | 7.061% | 2 | 0 | 28.829 |
| 3 | 0 | 28 | 19 | 9 | 0 | 5.485% | 2 | 0 | 29.477 |
| 3 | 1 | 30 | 19 | 10 | 0 | 6.893% | 2 | 0 | 19.113 |
| 4 | 0 | 27 | 19 | 7 | 0 | 5.718% | 2 | 0 | 23.584 |
| 4 | 1 | 30 | 19 | 9 | 0 | 6.647% | 2 | 0 | 21.080 |
| 5 | 0 | 20 | 19 | 1 | 0 | 5.589% | 2 | 0 | 17.438 |
| 5 | 1 | 26 | 19 | 7 | 0 | 6.523% | 2 | 0 | 23.017 |
| 6 | 0 | 28 | 19 | 6 | 0 | 5.702% | 2 | 0 | 31.927 |
| 6 | 1 | 27 | 19 | 7 | 0 | 5.824% | 2 | 0 | 19.589 |
| 7 | 0 | 29 | 19 | 9 | 0 | 5.706% | 2 | 0 | 18.963 |
| 7 | 1 | 37 | 19 | 18 | 0 | 6.237% | 2 | 0 | 17.739 |
| 8 | 0 | 23 | 19 | 4 | 0 | 5.722% | 2 | 0 | 34.167 |
| 8 | 1 | 25 | 19 | 6 | 0 | 5.527% | 2 | 0 | 38.231 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.5375 | 4.86 | 1.39 | 1.53 | 22.23 | 23.93 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
