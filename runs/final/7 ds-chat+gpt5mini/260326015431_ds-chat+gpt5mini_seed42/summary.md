# Checkpoint Summary

- run_dir: runs\260326015431_ds-chat+gpt5mini_seed42
- generated_at: 2026-03-26T03:19:53

## Overall

| Metric | Value |
|---|---:|
| eval_events | 577 |
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
| 0 | 0 | 46 | 21 | 8 | 0 | 8.310% | 0 | 0 |  |
| 0 | 1 | 49 | 21 | 15 | 0 | 7.938% | 0 | 0 |  |
| 1 | 0 | 51 | 19 | 18 | 0 | 8.422% | 2 | 0 | 16.199 |
| 1 | 1 | 43 | 19 | 14 | 0 | 6.519% | 2 | 0 | 13.491 |
| 2 | 0 | 37 | 19 | 9 | 0 | 7.679% | 2 | 0 | 20.331 |
| 2 | 1 | 41 | 19 | 9 | 0 | 6.424% | 2 | 0 | 13.470 |
| 3 | 0 | 24 | 19 | 5 | 0 | 6.631% | 2 | 0 | 19.201 |
| 3 | 1 | 34 | 19 | 14 | 0 | 6.460% | 2 | 0 | 21.216 |
| 4 | 0 | 24 | 19 | 3 | 0 | 6.218% | 2 | 0 | 22.031 |
| 4 | 1 | 29 | 19 | 9 | 0 | 6.493% | 2 | 0 | 16.512 |
| 5 | 0 | 31 | 19 | 12 | 0 | 6.427% | 2 | 0 | 24.588 |
| 5 | 1 | 24 | 19 | 5 | 0 | 6.493% | 2 | 0 | 31.131 |
| 6 | 0 | 22 | 19 | 3 | 0 | 7.053% | 2 | 0 | 36.831 |
| 6 | 1 | 29 | 19 | 9 | 0 | 6.491% | 2 | 0 | 26.582 |
| 7 | 0 | 26 | 19 | 7 | 0 | 6.020% | 2 | 0 | 27.825 |
| 7 | 1 | 22 | 19 | 3 | 0 | 6.785% | 2 | 0 | 18.593 |
| 8 | 0 | 22 | 19 | 3 | 0 | 6.358% | 2 | 0 | 20.959 |
| 8 | 1 | 23 | 19 | 4 | 0 | 6.063% | 2 | 0 | 28.987 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.0000 | 5.19 | 1.06 | 1.20 | 16.97 | 18.79 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
