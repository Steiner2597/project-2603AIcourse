# Checkpoint Summary

- run_dir: runs\260326052134_ds-chat+ds-reasoner_seed44
- generated_at: 2026-03-26T06:58:03

## Overall

| Metric | Value |
|---|---:|
| eval_events | 583 |
| accepted | 346 |
| dedup_expr_hit | 166 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 59 | 21 | 11 | 0 | 8.320% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 18 | 0 | 8.076% | 0 | 0 |  |
| 1 | 0 | 40 | 19 | 8 | 0 | 7.135% | 2 | 0 | 32.517 |
| 1 | 1 | 34 | 19 | 9 | 0 | 6.287% | 2 | 0 | 31.931 |
| 2 | 0 | 29 | 19 | 7 | 0 | 6.369% | 2 | 0 | 40.413 |
| 2 | 1 | 34 | 19 | 11 | 0 | 6.210% | 2 | 0 | 75.688 |
| 3 | 0 | 26 | 19 | 7 | 0 | 5.876% | 2 | 0 | 63.982 |
| 3 | 1 | 30 | 19 | 10 | 0 | 6.646% | 2 | 0 | 32.861 |
| 4 | 0 | 23 | 19 | 4 | 0 | 5.816% | 2 | 0 | 56.707 |
| 4 | 1 | 25 | 19 | 6 | 0 | 6.709% | 2 | 0 | 47.896 |
| 5 | 0 | 39 | 19 | 18 | 0 | 6.069% | 2 | 0 | 30.017 |
| 5 | 1 | 30 | 19 | 9 | 0 | 6.524% | 2 | 0 | 75.701 |
| 6 | 0 | 29 | 19 | 9 | 0 | 6.069% | 2 | 0 | 61.057 |
| 6 | 1 | 24 | 19 | 5 | 0 | 7.098% | 2 | 0 | 53.889 |
| 7 | 0 | 27 | 19 | 8 | 0 | 5.688% | 2 | 0 | 54.187 |
| 7 | 1 | 25 | 19 | 6 | 0 | 6.119% | 2 | 0 | 45.573 |
| 8 | 0 | 34 | 19 | 15 | 0 | 5.310% | 2 | 0 | 69.189 |
| 8 | 1 | 24 | 19 | 5 | 0 | 6.859% | 2 | 0 | 59.179 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.7562 | 4.93 | 1.32 | 1.46 | 21.09 | 22.82 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
