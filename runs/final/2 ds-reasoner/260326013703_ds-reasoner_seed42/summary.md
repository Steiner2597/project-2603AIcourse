# Checkpoint Summary

- run_dir: runs\260326013703_ds-reasoner_seed42
- generated_at: 2026-03-26T03:52:01

## Overall

| Metric | Value |
|---|---:|
| eval_events | 596 |
| accepted | 346 |
| dedup_expr_hit | 170 |
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
| 1 | 0 | 45 | 19 | 16 | 0 | 8.419% | 2 | 0 | 49.390 |
| 1 | 1 | 58 | 19 | 22 | 0 | 6.869% | 2 | 0 | 139.201 |
| 2 | 0 | 36 | 19 | 14 | 0 | 7.592% | 2 | 0 | 124.485 |
| 2 | 1 | 39 | 19 | 9 | 0 | 6.671% | 2 | 0 | 111.461 |
| 3 | 0 | 30 | 19 | 10 | 0 | 6.833% | 2 | 0 | 115.939 |
| 3 | 1 | 30 | 19 | 10 | 0 | 6.499% | 2 | 0 | 110.805 |
| 4 | 0 | 25 | 19 | 5 | 0 | 6.804% | 2 | 0 | 134.370 |
| 4 | 1 | 34 | 19 | 11 | 0 | 6.922% | 2 | 0 | 84.382 |
| 5 | 0 | 28 | 19 | 9 | 0 | 6.925% | 2 | 0 | 121.666 |
| 5 | 1 | 25 | 19 | 6 | 0 | 6.492% | 2 | 0 | 123.813 |
| 6 | 0 | 19 | 19 | 0 | 0 | 6.872% | 2 | 0 | 93.444 |
| 6 | 1 | 26 | 19 | 5 | 0 | 6.747% | 2 | 0 | 169.353 |
| 7 | 0 | 24 | 19 | 5 | 0 | 6.456% | 2 | 0 | 85.950 |
| 7 | 1 | 26 | 19 | 7 | 0 | 6.629% | 2 | 0 | 83.514 |
| 8 | 0 | 28 | 19 | 9 | 0 | 6.319% | 2 | 0 | 104.619 |
| 8 | 1 | 28 | 19 | 9 | 0 | 6.354% | 2 | 0 | 117.299 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.3187 | 5.27 | 0.98 | 1.12 | 15.64 | 17.48 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
