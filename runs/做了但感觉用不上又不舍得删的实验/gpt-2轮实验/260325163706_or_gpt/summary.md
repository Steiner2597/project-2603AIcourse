# Checkpoint Summary

- run_dir: runs\260325163706_or_gpt
- generated_at: 2026-03-25T17:17:11

## Overall

| Metric | Value |
|---|---:|
| eval_events | 273 |
| accepted | 144 |
| dedup_expr_hit | 68 |
| eval_errors | 1 |
| llm_events | 32 |
| llm_request_start | 16 |
| llm_request_done | 16 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 48 | 16 | 8 | 0 | 8.064% | 0 | 0 |  |
| 0 | 1 | 43 | 16 | 11 | 0 | 8.460% | 0 | 0 |  |
| 1 | 0 | 21 | 14 | 3 | 0 | 7.233% | 2 | 0 | 35.698 |
| 1 | 1 | 34 | 14 | 11 | 0 | 8.232% | 2 | 0 | 29.593 |
| 2 | 0 | 19 | 14 | 4 | 0 | 6.820% | 2 | 0 | 35.650 |
| 2 | 1 | 21 | 14 | 5 | 0 | 6.606% | 2 | 0 | 31.070 |
| 3 | 0 | 23 | 14 | 8 | 0 | 5.943% | 2 | 0 | 36.863 |
| 3 | 1 | 24 | 14 | 8 | 0 | 6.765% | 2 | 0 | 31.811 |
| 4 | 0 | 18 | 14 | 4 | 0 | 6.266% | 2 | 0 | 33.611 |
| 4 | 1 | 22 | 14 | 6 | 1 | 6.739% | 2 | 0 | 39.151 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.3750 | 5.52 | 0.73 | 0.87 | 11.72 | 13.65 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
