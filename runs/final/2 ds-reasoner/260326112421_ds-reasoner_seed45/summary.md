# Checkpoint Summary

- run_dir: runs\260326112421_ds-reasoner_seed45
- generated_at: 2026-03-26T14:01:35

## Overall

| Metric | Value |
|---|---:|
| eval_events | 631 |
| accepted | 346 |
| dedup_expr_hit | 175 |
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
| 1 | 0 | 39 | 19 | 11 | 0 | 7.022% | 2 | 0 | 160.238 |
| 1 | 1 | 36 | 19 | 5 | 0 | 6.643% | 2 | 0 | 144.800 |
| 2 | 0 | 42 | 19 | 16 | 0 | 6.774% | 2 | 0 | 158.577 |
| 2 | 1 | 47 | 19 | 18 | 0 | 6.531% | 2 | 0 | 163.501 |
| 3 | 0 | 22 | 19 | 3 | 0 | 6.526% | 2 | 0 | 178.904 |
| 3 | 1 | 45 | 19 | 15 | 0 | 6.461% | 2 | 0 | 103.090 |
| 4 | 0 | 28 | 19 | 8 | 0 | 7.148% | 2 | 0 | 212.939 |
| 4 | 1 | 29 | 19 | 6 | 0 | 6.450% | 2 | 0 | 136.731 |
| 5 | 0 | 35 | 19 | 13 | 0 | 6.504% | 2 | 0 | 120.810 |
| 5 | 1 | 34 | 19 | 10 | 0 | 6.215% | 2 | 0 | 155.438 |
| 6 | 0 | 28 | 19 | 7 | 0 | 6.632% | 2 | 0 | 180.720 |
| 6 | 1 | 32 | 19 | 8 | 0 | 6.010% | 2 | 0 | 193.158 |
| 7 | 0 | 24 | 19 | 5 | 0 | 6.111% | 2 | 0 | 106.556 |
| 7 | 1 | 35 | 19 | 15 | 0 | 5.992% | 2 | 0 | 146.995 |
| 8 | 0 | 23 | 19 | 4 | 0 | 5.856% | 2 | 0 | 130.309 |
| 8 | 1 | 31 | 19 | 10 | 0 | 5.680% | 2 | 0 | 231.787 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.5938 | 4.94 | 1.31 | 1.45 | 20.94 | 22.67 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
