# Checkpoint Summary

- run_dir: runs\260326111814_ds-chat_seed45
- generated_at: 2026-03-26T12:42:12

## Overall

| Metric | Value |
|---|---:|
| eval_events | 610 |
| accepted | 346 |
| dedup_expr_hit | 162 |
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
| 1 | 0 | 39 | 19 | 10 | 0 | 7.375% | 2 | 0 | 9.171 |
| 1 | 1 | 47 | 19 | 8 | 0 | 6.576% | 2 | 0 | 7.312 |
| 2 | 0 | 35 | 19 | 14 | 0 | 6.225% | 2 | 0 | 8.798 |
| 2 | 1 | 43 | 19 | 12 | 0 | 6.703% | 2 | 0 | 6.940 |
| 3 | 0 | 29 | 19 | 7 | 0 | 6.476% | 2 | 0 | 7.980 |
| 3 | 1 | 41 | 19 | 16 | 0 | 6.819% | 2 | 0 | 9.597 |
| 4 | 0 | 26 | 19 | 6 | 0 | 6.458% | 2 | 0 | 8.985 |
| 4 | 1 | 24 | 19 | 4 | 0 | 6.414% | 2 | 0 | 10.781 |
| 5 | 0 | 32 | 19 | 10 | 0 | 6.044% | 2 | 0 | 10.538 |
| 5 | 1 | 28 | 19 | 7 | 0 | 7.136% | 2 | 0 | 14.297 |
| 6 | 0 | 26 | 19 | 5 | 0 | 5.672% | 2 | 0 | 12.964 |
| 6 | 1 | 27 | 19 | 8 | 0 | 6.843% | 2 | 0 | 9.927 |
| 7 | 0 | 26 | 19 | 6 | 0 | 5.701% | 2 | 0 | 17.108 |
| 7 | 1 | 28 | 19 | 9 | 0 | 6.491% | 2 | 0 | 11.296 |
| 8 | 0 | 33 | 19 | 13 | 0 | 5.497% | 2 | 0 | 23.378 |
| 8 | 1 | 25 | 19 | 6 | 0 | 6.284% | 2 | 0 | 9.721 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.3250 | 4.88 | 1.37 | 1.51 | 21.86 | 23.57 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
