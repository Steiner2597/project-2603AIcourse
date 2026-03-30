# Checkpoint Summary

- run_dir: runs\260325122756_or_parts_ds\subruns\260325123608_or_ds
- generated_at: 2026-03-25T15:14:52

## Overall

| Metric | Value |
|---|---:|
| eval_events | 656 |
| accepted | 346 |
| dedup_expr_hit | 168 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 88 | 21 | 24 | 0 | 8.493% | 0 | 0 |  |
| 0 | 1 | 108 | 21 | 39 | 0 | 9.219% | 0 | 0 |  |
| 1 | 0 | 42 | 19 | 12 | 0 | 6.363% | 2 | 0 | 8.330 |
| 1 | 1 | 32 | 19 | 7 | 0 | 8.370% | 2 | 0 | 7.305 |
| 2 | 0 | 36 | 19 | 7 | 0 | 7.265% | 2 | 0 | 8.048 |
| 2 | 1 | 42 | 19 | 14 | 0 | 7.263% | 2 | 0 | 8.570 |
| 3 | 0 | 25 | 19 | 4 | 0 | 6.211% | 2 | 0 | 10.453 |
| 3 | 1 | 28 | 19 | 7 | 0 | 5.881% | 2 | 0 | 15.841 |
| 4 | 0 | 24 | 19 | 4 | 0 | 5.964% | 2 | 0 | 11.247 |
| 4 | 1 | 26 | 19 | 5 | 0 | 6.697% | 2 | 0 | 14.852 |
| 5 | 0 | 27 | 19 | 7 | 0 | 5.712% | 2 | 0 | 11.018 |
| 5 | 1 | 24 | 19 | 5 | 0 | 6.811% | 2 | 0 | 16.814 |
| 6 | 0 | 23 | 19 | 4 | 0 | 5.838% | 2 | 0 | 24.484 |
| 6 | 1 | 35 | 19 | 10 | 0 | 6.263% | 2 | 0 | 22.236 |
| 7 | 0 | 23 | 19 | 4 | 0 | 6.708% | 2 | 0 | 12.951 |
| 7 | 1 | 28 | 19 | 8 | 0 | 6.586% | 2 | 0 | 15.933 |
| 8 | 0 | 23 | 19 | 4 | 0 | 5.612% | 2 | 0 | 16.370 |
| 8 | 1 | 22 | 19 | 3 | 0 | 6.697% | 2 | 0 | 20.352 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 106.5500 | 4.76 | 1.14 | 1.52 | 19.32 | 24.24 |
| Best-Fit (BF) | 107.7000 | 5.90 | 0.00 | 0.38 | 0.00 | 6.09 |
| First-Fit (FF) | 108.1000 | 6.29 | -0.38 | 0.00 | -6.49 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
