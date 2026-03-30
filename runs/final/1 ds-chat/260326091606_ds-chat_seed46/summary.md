# Checkpoint Summary

- run_dir: runs\260326091606_ds-chat_seed46
- generated_at: 2026-03-26T10:40:23

## Overall

| Metric | Value |
|---|---:|
| eval_events | 579 |
| accepted | 346 |
| dedup_expr_hit | 150 |
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
| 1 | 0 | 39 | 19 | 16 | 0 | 6.666% | 2 | 0 | 6.122 |
| 1 | 1 | 36 | 19 | 7 | 0 | 7.221% | 2 | 0 | 9.295 |
| 2 | 0 | 40 | 19 | 13 | 0 | 6.383% | 2 | 0 | 10.543 |
| 2 | 1 | 36 | 19 | 10 | 0 | 6.810% | 2 | 0 | 8.178 |
| 3 | 0 | 22 | 19 | 3 | 0 | 5.884% | 2 | 0 | 7.719 |
| 3 | 1 | 29 | 19 | 10 | 0 | 6.873% | 2 | 0 | 19.301 |
| 4 | 0 | 28 | 19 | 8 | 0 | 5.463% | 2 | 0 | 8.322 |
| 4 | 1 | 38 | 19 | 18 | 0 | 6.962% | 2 | 0 | 9.422 |
| 5 | 0 | 24 | 19 | 4 | 0 | 5.535% | 2 | 0 | 12.521 |
| 5 | 1 | 32 | 19 | 9 | 0 | 6.238% | 2 | 0 | 11.986 |
| 6 | 0 | 22 | 19 | 1 | 0 | 5.911% | 2 | 0 | 11.435 |
| 6 | 1 | 30 | 19 | 8 | 0 | 5.637% | 2 | 0 | 14.689 |
| 7 | 0 | 29 | 19 | 6 | 0 | 5.940% | 2 | 0 | 47.303 |
| 7 | 1 | 23 | 19 | 4 | 0 | 6.757% | 2 | 0 | 17.702 |
| 8 | 0 | 28 | 19 | 9 | 0 | 5.599% | 2 | 0 | 34.267 |
| 8 | 1 | 27 | 19 | 5 | 0 | 5.911% | 2 | 0 | 12.759 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.4938 | 4.85 | 1.40 | 1.54 | 22.37 | 24.07 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
