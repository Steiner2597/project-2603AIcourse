# Checkpoint Summary

- run_dir: runs\260326053853_gpt5nano+ds-reasoner_seed44
- generated_at: 2026-03-26T07:19:37

## Overall

| Metric | Value |
|---|---:|
| eval_events | 573 |
| accepted | 346 |
| dedup_expr_hit | 155 |
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
| 1 | 0 | 35 | 19 | 10 | 0 | 7.073% | 2 | 0 | 64.998 |
| 1 | 1 | 33 | 19 | 6 | 0 | 6.847% | 2 | 0 | 61.223 |
| 2 | 0 | 36 | 19 | 12 | 0 | 6.185% | 2 | 0 | 56.421 |
| 2 | 1 | 32 | 19 | 8 | 0 | 5.991% | 2 | 0 | 64.807 |
| 3 | 0 | 27 | 19 | 7 | 0 | 5.724% | 2 | 0 | 38.410 |
| 3 | 1 | 30 | 19 | 10 | 0 | 6.865% | 2 | 0 | 57.482 |
| 4 | 0 | 23 | 19 | 4 | 0 | 5.776% | 2 | 0 | 47.698 |
| 4 | 1 | 28 | 19 | 7 | 0 | 6.731% | 2 | 0 | 67.139 |
| 5 | 0 | 22 | 19 | 3 | 0 | 5.737% | 2 | 0 | 62.398 |
| 5 | 1 | 27 | 19 | 6 | 0 | 6.555% | 2 | 0 | 84.294 |
| 6 | 0 | 24 | 19 | 5 | 0 | 5.696% | 2 | 0 | 71.999 |
| 6 | 1 | 25 | 19 | 5 | 0 | 5.858% | 2 | 0 | 57.083 |
| 7 | 0 | 32 | 19 | 13 | 0 | 5.702% | 2 | 0 | 41.177 |
| 7 | 1 | 28 | 19 | 7 | 0 | 6.079% | 2 | 0 | 79.668 |
| 8 | 0 | 34 | 19 | 15 | 0 | 5.103% | 2 | 0 | 79.381 |
| 8 | 1 | 27 | 19 | 8 | 0 | 6.399% | 2 | 0 | 51.408 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.2500 | 4.79 | 1.46 | 1.60 | 23.31 | 24.99 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
