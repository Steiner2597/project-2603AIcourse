# Checkpoint Summary

- run_dir: runs\260326034536_gpt5nano+ds-reasoner_seed43
- generated_at: 2026-03-26T05:38:31

## Overall

| Metric | Value |
|---|---:|
| eval_events | 696 |
| accepted | 346 |
| dedup_expr_hit | 203 |
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
| 1 | 0 | 27 | 19 | 1 | 0 | 7.078% | 2 | 0 | 72.455 |
| 1 | 1 | 39 | 19 | 12 | 0 | 7.435% | 2 | 0 | 89.660 |
| 2 | 0 | 51 | 19 | 15 | 0 | 6.755% | 2 | 0 | 69.636 |
| 2 | 1 | 67 | 19 | 24 | 0 | 7.196% | 2 | 0 | 63.454 |
| 3 | 0 | 35 | 19 | 7 | 0 | 6.757% | 2 | 0 | 64.880 |
| 3 | 1 | 30 | 19 | 9 | 0 | 6.846% | 2 | 0 | 45.403 |
| 4 | 0 | 47 | 19 | 11 | 0 | 6.467% | 2 | 0 | 75.370 |
| 4 | 1 | 33 | 19 | 12 | 0 | 6.851% | 2 | 0 | 41.462 |
| 5 | 0 | 35 | 19 | 10 | 0 | 6.397% | 2 | 0 | 52.710 |
| 5 | 1 | 23 | 19 | 4 | 0 | 6.590% | 2 | 0 | 54.323 |
| 6 | 0 | 32 | 19 | 10 | 0 | 5.986% | 2 | 0 | 66.465 |
| 6 | 1 | 27 | 19 | 5 | 0 | 6.988% | 2 | 0 | 36.324 |
| 7 | 0 | 45 | 19 | 23 | 0 | 6.097% | 2 | 0 | 61.321 |
| 7 | 1 | 38 | 19 | 19 | 0 | 6.335% | 2 | 0 | 61.572 |
| 8 | 0 | 29 | 19 | 8 | 0 | 5.768% | 2 | 0 | 73.861 |
| 8 | 1 | 21 | 19 | 2 | 0 | 6.082% | 2 | 0 | 69.879 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.4938 | 4.99 | 1.26 | 1.40 | 20.17 | 21.92 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
