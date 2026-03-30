# Checkpoint Summary

- run_dir: runs\260326031035_gpt5nano_seed43
- generated_at: 2026-03-26T04:50:26

## Overall

| Metric | Value |
|---|---:|
| eval_events | 693 |
| accepted | 346 |
| dedup_expr_hit | 194 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 62 | 21 | 18 | 0 | 7.957% | 0 | 0 |  |
| 0 | 1 | 55 | 21 | 13 | 0 | 8.188% | 0 | 0 |  |
| 1 | 0 | 35 | 19 | 7 | 0 | 7.150% | 2 | 0 | 28.999 |
| 1 | 1 | 63 | 19 | 21 | 0 | 7.364% | 2 | 0 | 27.683 |
| 2 | 0 | 44 | 19 | 11 | 0 | 6.745% | 2 | 0 | 28.745 |
| 2 | 1 | 64 | 19 | 21 | 0 | 7.573% | 2 | 0 | 20.535 |
| 3 | 0 | 35 | 19 | 12 | 0 | 7.486% | 2 | 0 | 34.395 |
| 3 | 1 | 36 | 19 | 10 | 0 | 7.032% | 2 | 0 | 31.031 |
| 4 | 0 | 32 | 19 | 9 | 0 | 6.787% | 2 | 0 | 41.090 |
| 4 | 1 | 31 | 19 | 9 | 0 | 7.096% | 2 | 0 | 31.026 |
| 5 | 0 | 27 | 19 | 5 | 0 | 6.410% | 2 | 0 | 51.233 |
| 5 | 1 | 23 | 19 | 3 | 0 | 6.581% | 2 | 0 | 37.471 |
| 6 | 0 | 30 | 19 | 9 | 0 | 6.812% | 2 | 0 | 41.376 |
| 6 | 1 | 35 | 19 | 8 | 0 | 6.999% | 2 | 0 | 59.916 |
| 7 | 0 | 35 | 19 | 13 | 1 | 6.687% | 2 | 0 | 40.779 |
| 7 | 1 | 36 | 19 | 14 | 0 | 6.713% | 2 | 0 | 42.498 |
| 8 | 0 | 24 | 19 | 5 | 0 | 6.724% | 2 | 0 | 30.081 |
| 8 | 1 | 26 | 19 | 6 | 0 | 6.839% | 2 | 0 | 52.074 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 140.1500 | 6.20 | 0.05 | 0.19 | 0.79 | 2.96 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
