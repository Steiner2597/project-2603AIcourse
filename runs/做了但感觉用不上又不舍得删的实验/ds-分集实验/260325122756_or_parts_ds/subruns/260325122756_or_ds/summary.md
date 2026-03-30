# Checkpoint Summary

- run_dir: runs\260325122756_or_parts_ds\subruns\260325122756_or_ds
- generated_at: 2026-03-25T15:14:50

## Overall

| Metric | Value |
|---|---:|
| eval_events | 752 |
| accepted | 346 |
| dedup_expr_hit | 222 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 93 | 21 | 24 | 0 | 8.368% | 0 | 0 |  |
| 0 | 1 | 107 | 21 | 38 | 0 | 8.989% | 0 | 0 |  |
| 1 | 0 | 49 | 19 | 11 | 0 | 6.639% | 2 | 0 | 8.475 |
| 1 | 1 | 45 | 19 | 13 | 0 | 6.871% | 2 | 0 | 9.528 |
| 2 | 0 | 58 | 19 | 22 | 0 | 7.556% | 2 | 0 | 10.742 |
| 2 | 1 | 30 | 19 | 6 | 0 | 6.721% | 2 | 0 | 12.192 |
| 3 | 0 | 39 | 19 | 13 | 0 | 5.536% | 2 | 0 | 8.301 |
| 3 | 1 | 27 | 19 | 6 | 0 | 5.529% | 2 | 0 | 12.128 |
| 4 | 0 | 28 | 19 | 8 | 0 | 6.835% | 2 | 0 | 10.767 |
| 4 | 1 | 22 | 19 | 3 | 0 | 6.617% | 2 | 0 | 10.687 |
| 5 | 0 | 28 | 19 | 7 | 0 | 6.166% | 2 | 0 | 12.663 |
| 5 | 1 | 27 | 19 | 6 | 0 | 6.750% | 2 | 0 | 17.702 |
| 6 | 0 | 22 | 19 | 2 | 0 | 7.091% | 2 | 0 | 11.503 |
| 6 | 1 | 60 | 19 | 27 | 0 | 6.489% | 2 | 0 | 15.044 |
| 7 | 0 | 31 | 19 | 10 | 0 | 6.052% | 2 | 0 | 11.503 |
| 7 | 1 | 32 | 19 | 11 | 0 | 6.251% | 2 | 0 | 16.296 |
| 8 | 0 | 26 | 19 | 6 | 0 | 6.681% | 2 | 0 | 8.935 |
| 8 | 1 | 28 | 19 | 9 | 0 | 7.024% | 2 | 0 | 20.129 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 51.6500 | 5.10 | 0.50 | 1.10 | 8.88 | 17.78 |
| Best-Fit (BF) | 51.9000 | 5.59 | 0.00 | 0.61 | 0.00 | 9.76 |
| First-Fit (FF) | 52.2000 | 6.20 | -0.61 | 0.00 | -10.82 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
