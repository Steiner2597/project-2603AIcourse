# Checkpoint Summary

- run_dir: runs\260326030020_ds-chat_seed43
- generated_at: 2026-03-26T04:23:04

## Overall

| Metric | Value |
|---|---:|
| eval_events | 677 |
| accepted | 346 |
| dedup_expr_hit | 191 |
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
| 1 | 0 | 27 | 19 | 1 | 0 | 7.078% | 2 | 0 | 8.031 |
| 1 | 1 | 44 | 19 | 11 | 0 | 7.442% | 2 | 0 | 6.389 |
| 2 | 0 | 49 | 19 | 16 | 0 | 6.291% | 2 | 0 | 7.895 |
| 2 | 1 | 92 | 19 | 40 | 0 | 6.943% | 2 | 0 | 6.708 |
| 3 | 0 | 29 | 19 | 7 | 0 | 6.916% | 2 | 0 | 9.450 |
| 3 | 1 | 25 | 19 | 5 | 0 | 6.767% | 2 | 0 | 8.549 |
| 4 | 0 | 26 | 19 | 5 | 0 | 6.511% | 2 | 0 | 8.193 |
| 4 | 1 | 35 | 19 | 13 | 0 | 6.465% | 2 | 0 | 11.349 |
| 5 | 0 | 25 | 19 | 6 | 0 | 6.446% | 2 | 0 | 12.573 |
| 5 | 1 | 43 | 19 | 16 | 0 | 6.406% | 2 | 0 | 9.026 |
| 6 | 0 | 32 | 19 | 8 | 0 | 6.577% | 2 | 0 | 13.092 |
| 6 | 1 | 28 | 19 | 5 | 0 | 6.078% | 2 | 0 | 8.720 |
| 7 | 0 | 28 | 19 | 9 | 0 | 7.060% | 2 | 0 | 6.490 |
| 7 | 1 | 31 | 19 | 12 | 0 | 6.050% | 2 | 0 | 10.001 |
| 8 | 0 | 23 | 19 | 3 | 0 | 6.126% | 2 | 0 | 15.659 |
| 8 | 1 | 23 | 19 | 3 | 0 | 5.657% | 2 | 0 | 9.642 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.5938 | 5.12 | 1.13 | 1.27 | 18.09 | 19.88 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
