# Checkpoint Summary

- run_dir: runs\260326033313_ds-chat+ds-reasoner_seed43
- generated_at: 2026-03-26T05:21:12

## Overall

| Metric | Value |
|---|---:|
| eval_events | 671 |
| accepted | 346 |
| dedup_expr_hit | 181 |
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
| 1 | 0 | 27 | 19 | 1 | 0 | 7.078% | 2 | 0 | 9.345 |
| 1 | 1 | 67 | 19 | 23 | 0 | 7.335% | 2 | 0 | 42.256 |
| 2 | 0 | 41 | 19 | 11 | 0 | 7.011% | 2 | 0 | 109.256 |
| 2 | 1 | 76 | 19 | 27 | 0 | 7.080% | 2 | 0 | 83.038 |
| 3 | 0 | 33 | 19 | 8 | 0 | 6.564% | 2 | 0 | 71.325 |
| 3 | 1 | 26 | 19 | 7 | 0 | 6.768% | 2 | 0 | 49.926 |
| 4 | 0 | 36 | 19 | 11 | 0 | 7.199% | 2 | 0 | 99.942 |
| 4 | 1 | 32 | 19 | 9 | 0 | 7.256% | 2 | 0 | 57.589 |
| 5 | 0 | 27 | 19 | 7 | 0 | 6.420% | 2 | 0 | 35.841 |
| 5 | 1 | 27 | 19 | 8 | 0 | 7.240% | 2 | 0 | 31.558 |
| 6 | 0 | 28 | 19 | 5 | 0 | 6.379% | 2 | 0 | 31.532 |
| 6 | 1 | 23 | 19 | 3 | 0 | 7.112% | 2 | 0 | 35.489 |
| 7 | 0 | 32 | 19 | 12 | 0 | 5.962% | 2 | 0 | 31.103 |
| 7 | 1 | 27 | 19 | 8 | 0 | 7.022% | 2 | 0 | 68.466 |
| 8 | 0 | 30 | 19 | 7 | 0 | 5.445% | 2 | 0 | 62.795 |
| 8 | 1 | 22 | 19 | 3 | 0 | 6.160% | 2 | 0 | 43.843 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.4375 | 4.87 | 1.38 | 1.52 | 22.04 | 23.74 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
