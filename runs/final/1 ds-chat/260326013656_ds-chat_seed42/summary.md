# Checkpoint Summary

- run_dir: runs\260326013656_ds-chat_seed42
- generated_at: 2026-03-26T02:59:58

## Overall

| Metric | Value |
|---|---:|
| eval_events | 611 |
| accepted | 346 |
| dedup_expr_hit | 176 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 46 | 21 | 8 | 0 | 8.310% | 0 | 0 |  |
| 0 | 1 | 49 | 21 | 15 | 0 | 7.938% | 0 | 0 |  |
| 1 | 0 | 50 | 19 | 18 | 0 | 8.643% | 2 | 0 | 8.591 |
| 1 | 1 | 37 | 19 | 8 | 0 | 6.483% | 2 | 0 | 8.790 |
| 2 | 0 | 45 | 19 | 19 | 0 | 7.122% | 2 | 0 | 12.272 |
| 2 | 1 | 33 | 19 | 7 | 0 | 6.440% | 2 | 0 | 12.482 |
| 3 | 0 | 23 | 19 | 4 | 0 | 6.946% | 2 | 0 | 12.558 |
| 3 | 1 | 31 | 19 | 11 | 1 | 6.435% | 2 | 0 | 9.925 |
| 4 | 0 | 32 | 19 | 10 | 0 | 6.522% | 2 | 0 | 13.189 |
| 4 | 1 | 29 | 19 | 10 | 0 | 6.492% | 2 | 0 | 10.002 |
| 5 | 0 | 36 | 19 | 17 | 0 | 6.561% | 2 | 0 | 15.487 |
| 5 | 1 | 25 | 19 | 3 | 0 | 6.477% | 2 | 0 | 14.851 |
| 6 | 0 | 24 | 19 | 5 | 0 | 6.483% | 2 | 0 | 22.117 |
| 6 | 1 | 31 | 19 | 8 | 0 | 7.079% | 2 | 0 | 12.701 |
| 7 | 0 | 27 | 19 | 8 | 0 | 6.030% | 2 | 0 | 13.267 |
| 7 | 1 | 29 | 19 | 7 | 0 | 6.589% | 2 | 0 | 14.871 |
| 8 | 0 | 28 | 19 | 9 | 0 | 6.540% | 2 | 0 | 16.986 |
| 8 | 1 | 36 | 19 | 9 | 0 | 6.330% | 2 | 0 | 15.980 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.4313 | 5.11 | 1.14 | 1.28 | 18.27 | 20.05 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
