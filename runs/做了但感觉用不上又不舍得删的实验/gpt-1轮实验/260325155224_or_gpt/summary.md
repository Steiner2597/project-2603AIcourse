# Checkpoint Summary

- run_dir: runs\260325155224_or_gpt
- generated_at: 2026-03-25T16:25:25

## Overall

| Metric | Value |
|---|---:|
| eval_events | 238 |
| accepted | 116 |
| dedup_expr_hit | 64 |
| eval_errors | 0 |
| llm_events | 24 |
| llm_request_start | 12 |
| llm_request_done | 12 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 48 | 16 | 8 | 0 | 8.064% | 0 | 0 |  |
| 0 | 1 | 43 | 16 | 11 | 0 | 8.460% | 0 | 0 |  |
| 1 | 0 | 21 | 14 | 3 | 0 | 7.302% | 2 | 0 | 25.916 |
| 1 | 1 | 45 | 14 | 18 | 0 | 7.917% | 2 | 0 | 44.245 |
| 2 | 0 | 21 | 14 | 6 | 0 | 6.722% | 2 | 0 | 29.819 |
| 2 | 1 | 15 | 14 | 1 | 0 | 6.432% | 2 | 0 | 29.387 |
| 3 | 0 | 26 | 14 | 12 | 0 | 6.842% | 2 | 0 | 30.794 |
| 3 | 1 | 19 | 14 | 5 | 0 | 5.709% | 2 | 0 | 40.837 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.1562 | 5.25 | 1.00 | 1.14 | 15.99 | 17.82 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
