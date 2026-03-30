# Checkpoint Summary

- run_dir: runs\260325155211_or_gpt
- generated_at: 2026-03-25T16:26:15

## Overall

| Metric | Value |
|---|---:|
| eval_events | 253 |
| accepted | 116 |
| dedup_expr_hit | 67 |
| eval_errors | 0 |
| llm_events | 24 |
| llm_request_start | 12 |
| llm_request_done | 12 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 46 | 16 | 14 | 0 | 7.938% | 0 | 0 |  |
| 0 | 1 | 52 | 16 | 12 | 0 | 7.728% | 0 | 0 |  |
| 1 | 0 | 28 | 14 | 6 | 0 | 6.530% | 2 | 0 | 40.989 |
| 1 | 1 | 19 | 14 | 3 | 0 | 8.189% | 2 | 0 | 35.823 |
| 2 | 0 | 42 | 14 | 12 | 0 | 6.640% | 2 | 0 | 26.532 |
| 2 | 1 | 15 | 14 | 1 | 0 | 6.877% | 2 | 0 | 37.056 |
| 3 | 0 | 34 | 14 | 16 | 0 | 6.546% | 2 | 0 | 37.698 |
| 3 | 1 | 17 | 14 | 3 | 0 | 6.953% | 2 | 0 | 33.436 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 140.2188 | 6.25 | 0.00 | 0.14 | 0.03 | 2.21 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
