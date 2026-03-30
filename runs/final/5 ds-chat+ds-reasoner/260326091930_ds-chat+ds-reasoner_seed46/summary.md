# Checkpoint Summary

- run_dir: runs\260326091930_ds-chat+ds-reasoner_seed46
- generated_at: 2026-03-26T11:11:24

## Overall

| Metric | Value |
|---|---:|
| eval_events | 563 |
| accepted | 346 |
| dedup_expr_hit | 133 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 43 | 21 | 5 | 0 | 8.008% | 0 | 0 |  |
| 0 | 1 | 53 | 21 | 14 | 0 | 8.675% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 16 | 0 | 6.702% | 2 | 0 | 51.371 |
| 1 | 1 | 39 | 19 | 9 | 0 | 6.999% | 2 | 0 | 55.942 |
| 2 | 0 | 34 | 19 | 8 | 0 | 6.079% | 2 | 0 | 52.074 |
| 2 | 1 | 37 | 19 | 9 | 0 | 7.306% | 2 | 0 | 54.157 |
| 3 | 0 | 22 | 19 | 3 | 0 | 5.817% | 2 | 0 | 62.434 |
| 3 | 1 | 29 | 19 | 10 | 0 | 5.688% | 2 | 0 | 73.756 |
| 4 | 0 | 22 | 19 | 2 | 0 | 5.758% | 2 | 0 | 60.273 |
| 4 | 1 | 20 | 19 | 1 | 0 | 5.972% | 2 | 0 | 62.608 |
| 5 | 0 | 21 | 19 | 1 | 0 | 5.954% | 2 | 0 | 122.105 |
| 5 | 1 | 20 | 19 | 1 | 0 | 5.713% | 2 | 0 | 99.344 |
| 6 | 0 | 33 | 19 | 8 | 0 | 5.754% | 2 | 0 | 76.634 |
| 6 | 1 | 41 | 19 | 16 | 1 | 6.438% | 2 | 0 | 51.445 |
| 7 | 0 | 29 | 19 | 10 | 0 | 5.519% | 2 | 0 | 69.124 |
| 7 | 1 | 25 | 19 | 6 | 0 | 6.083% | 2 | 0 | 55.286 |
| 8 | 0 | 24 | 19 | 5 | 0 | 5.989% | 2 | 0 | 97.178 |
| 8 | 1 | 32 | 19 | 9 | 0 | 6.108% | 2 | 0 | 54.527 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.5125 | 4.90 | 1.35 | 1.49 | 21.67 | 23.38 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
