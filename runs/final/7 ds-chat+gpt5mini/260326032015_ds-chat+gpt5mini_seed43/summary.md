# Checkpoint Summary

- run_dir: runs\260326032015_ds-chat+gpt5mini_seed43
- generated_at: 2026-03-26T04:50:32

## Overall

| Metric | Value |
|---|---:|
| eval_events | 701 |
| accepted | 346 |
| dedup_expr_hit | 208 |
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
| 1 | 0 | 35 | 19 | 7 | 0 | 7.146% | 2 | 0 | 19.371 |
| 1 | 1 | 52 | 19 | 18 | 0 | 7.317% | 2 | 0 | 16.810 |
| 2 | 0 | 56 | 19 | 17 | 0 | 7.422% | 2 | 0 | 14.383 |
| 2 | 1 | 73 | 19 | 27 | 0 | 7.347% | 2 | 0 | 15.570 |
| 3 | 0 | 27 | 19 | 6 | 0 | 6.979% | 2 | 0 | 13.938 |
| 3 | 1 | 31 | 19 | 8 | 0 | 6.512% | 2 | 0 | 22.290 |
| 4 | 0 | 37 | 19 | 11 | 0 | 7.154% | 2 | 0 | 23.436 |
| 4 | 1 | 32 | 19 | 9 | 0 | 6.521% | 2 | 0 | 17.218 |
| 5 | 0 | 28 | 19 | 7 | 0 | 6.847% | 2 | 0 | 25.599 |
| 5 | 1 | 37 | 19 | 12 | 0 | 6.520% | 2 | 0 | 33.361 |
| 6 | 0 | 27 | 19 | 7 | 0 | 6.746% | 2 | 0 | 23.213 |
| 6 | 1 | 27 | 19 | 6 | 0 | 6.761% | 2 | 0 | 23.913 |
| 7 | 0 | 29 | 19 | 6 | 0 | 6.948% | 2 | 0 | 29.058 |
| 7 | 1 | 36 | 19 | 17 | 0 | 6.320% | 2 | 0 | 25.258 |
| 8 | 0 | 30 | 19 | 11 | 0 | 6.899% | 2 | 0 | 26.322 |
| 8 | 1 | 27 | 19 | 8 | 0 | 6.697% | 2 | 0 | 22.693 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 140.0750 | 6.14 | 0.11 | 0.25 | 1.82 | 3.97 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
