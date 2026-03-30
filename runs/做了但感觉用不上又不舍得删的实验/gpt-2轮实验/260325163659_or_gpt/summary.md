# Checkpoint Summary

- run_dir: runs\260325163659_or_gpt
- generated_at: 2026-03-25T17:17:28

## Overall

| Metric | Value |
|---|---:|
| eval_events | 287 |
| accepted | 144 |
| dedup_expr_hit | 75 |
| eval_errors | 0 |
| llm_events | 32 |
| llm_request_start | 16 |
| llm_request_done | 16 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 46 | 16 | 14 | 0 | 7.938% | 0 | 0 |  |
| 0 | 1 | 52 | 16 | 12 | 0 | 7.728% | 0 | 0 |  |
| 1 | 0 | 28 | 14 | 6 | 0 | 6.601% | 2 | 0 | 36.358 |
| 1 | 1 | 32 | 14 | 11 | 0 | 6.615% | 2 | 0 | 37.536 |
| 2 | 0 | 21 | 14 | 3 | 0 | 7.578% | 2 | 0 | 29.072 |
| 2 | 1 | 20 | 14 | 6 | 0 | 6.888% | 2 | 0 | 33.502 |
| 3 | 0 | 23 | 14 | 7 | 0 | 7.762% | 2 | 0 | 27.459 |
| 3 | 1 | 16 | 14 | 2 | 0 | 7.747% | 2 | 0 | 32.822 |
| 4 | 0 | 29 | 14 | 8 | 0 | 7.295% | 2 | 0 | 29.276 |
| 4 | 1 | 20 | 14 | 6 | 0 | 6.923% | 2 | 0 | 41.887 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.1188 | 5.22 | 1.03 | 1.17 | 16.41 | 18.24 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
