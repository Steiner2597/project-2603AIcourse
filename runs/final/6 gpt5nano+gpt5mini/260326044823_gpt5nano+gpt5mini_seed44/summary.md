# Checkpoint Summary

- run_dir: runs\260326044823_gpt5nano+gpt5mini_seed44
- generated_at: 2026-03-26T06:19:11

## Overall

| Metric | Value |
|---|---:|
| eval_events | 584 |
| accepted | 346 |
| dedup_expr_hit | 144 |
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
| 1 | 0 | 36 | 19 | 8 | 0 | 7.390% | 2 | 0 | 35.747 |
| 1 | 1 | 45 | 19 | 12 | 0 | 6.353% | 2 | 0 | 35.290 |
| 2 | 0 | 37 | 19 | 10 | 0 | 6.336% | 2 | 0 | 37.281 |
| 2 | 1 | 55 | 19 | 21 | 0 | 6.276% | 2 | 0 | 40.144 |
| 3 | 0 | 21 | 19 | 2 | 0 | 5.836% | 2 | 0 | 36.698 |
| 3 | 1 | 21 | 19 | 2 | 0 | 6.413% | 2 | 0 | 32.381 |
| 4 | 0 | 22 | 19 | 3 | 0 | 6.176% | 2 | 0 | 29.791 |
| 4 | 1 | 32 | 19 | 13 | 0 | 6.069% | 2 | 0 | 25.362 |
| 5 | 0 | 23 | 19 | 2 | 0 | 6.108% | 2 | 0 | 29.919 |
| 5 | 1 | 25 | 19 | 4 | 0 | 6.133% | 2 | 0 | 24.867 |
| 6 | 0 | 26 | 19 | 6 | 0 | 5.489% | 2 | 0 | 39.165 |
| 6 | 1 | 34 | 19 | 12 | 0 | 6.190% | 2 | 0 | 29.998 |
| 7 | 0 | 22 | 19 | 3 | 0 | 5.645% | 2 | 0 | 32.011 |
| 7 | 1 | 32 | 19 | 12 | 0 | 5.855% | 2 | 0 | 25.532 |
| 8 | 0 | 21 | 19 | 2 | 0 | 6.393% | 2 | 0 | 41.413 |
| 8 | 1 | 22 | 19 | 3 | 0 | 5.831% | 2 | 0 | 29.318 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.6687 | 5.02 | 1.23 | 1.36 | 19.60 | 21.36 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
