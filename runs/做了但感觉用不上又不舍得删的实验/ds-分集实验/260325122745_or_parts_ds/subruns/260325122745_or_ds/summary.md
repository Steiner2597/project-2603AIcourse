# Checkpoint Summary

- run_dir: runs\260325122745_or_parts_ds\subruns\260325122745_or_ds
- generated_at: 2026-03-25T15:14:17

## Overall

| Metric | Value |
|---|---:|
| eval_events | 679 |
| accepted | 346 |
| dedup_expr_hit | 174 |
| eval_errors | 2 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 89 | 21 | 22 | 0 | 9.068% | 0 | 0 |  |
| 0 | 1 | 99 | 21 | 37 | 0 | 9.719% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 6 | 0 | 7.139% | 2 | 0 | 8.171 |
| 1 | 1 | 35 | 19 | 5 | 0 | 7.397% | 2 | 0 | 8.407 |
| 2 | 0 | 43 | 19 | 11 | 0 | 7.220% | 2 | 0 | 7.346 |
| 2 | 1 | 31 | 19 | 8 | 0 | 6.726% | 2 | 0 | 9.337 |
| 3 | 0 | 22 | 19 | 2 | 0 | 7.436% | 2 | 0 | 9.124 |
| 3 | 1 | 28 | 19 | 6 | 0 | 6.945% | 2 | 0 | 9.465 |
| 4 | 0 | 34 | 19 | 13 | 0 | 6.759% | 2 | 0 | 12.436 |
| 4 | 1 | 34 | 19 | 11 | 2 | 7.954% | 2 | 0 | 10.127 |
| 5 | 0 | 22 | 19 | 3 | 0 | 6.890% | 2 | 0 | 13.555 |
| 5 | 1 | 28 | 19 | 7 | 0 | 7.398% | 2 | 0 | 12.189 |
| 6 | 0 | 23 | 19 | 0 | 0 | 5.492% | 2 | 0 | 10.945 |
| 6 | 1 | 43 | 19 | 13 | 0 | 5.507% | 2 | 0 | 18.652 |
| 7 | 0 | 32 | 19 | 13 | 0 | 6.999% | 2 | 0 | 10.619 |
| 7 | 1 | 27 | 19 | 6 | 0 | 5.982% | 2 | 0 | 13.549 |
| 8 | 0 | 26 | 19 | 7 | 0 | 5.556% | 2 | 0 | 17.706 |
| 8 | 1 | 24 | 19 | 4 | 0 | 5.971% | 2 | 0 | 17.407 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 51.8000 | 5.39 | 0.21 | 0.81 | 3.69 | 13.09 |
| Best-Fit (BF) | 51.9000 | 5.59 | 0.00 | 0.61 | 0.00 | 9.76 |
| First-Fit (FF) | 52.2000 | 6.20 | -0.61 | 0.00 | -10.82 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
