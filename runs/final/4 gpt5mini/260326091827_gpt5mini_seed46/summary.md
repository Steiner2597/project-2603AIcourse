# Checkpoint Summary

- run_dir: runs\260326091827_gpt5mini_seed46
- generated_at: 2026-03-26T10:50:36

## Overall

| Metric | Value |
|---|---:|
| eval_events | 585 |
| accepted | 346 |
| dedup_expr_hit | 157 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 43 | 21 | 5 | 0 | 8.008% | 0 | 0 |  |
| 0 | 1 | 53 | 21 | 14 | 0 | 8.675% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 16 | 0 | 6.667% | 2 | 0 | 36.397 |
| 1 | 1 | 39 | 19 | 9 | 0 | 7.123% | 2 | 0 | 21.881 |
| 2 | 0 | 32 | 19 | 11 | 0 | 6.061% | 2 | 0 | 33.190 |
| 2 | 1 | 41 | 19 | 11 | 0 | 6.916% | 2 | 0 | 19.910 |
| 3 | 0 | 29 | 19 | 7 | 0 | 5.733% | 2 | 0 | 32.133 |
| 3 | 1 | 27 | 19 | 7 | 0 | 6.180% | 2 | 0 | 37.937 |
| 4 | 0 | 29 | 19 | 7 | 0 | 5.986% | 2 | 0 | 44.977 |
| 4 | 1 | 27 | 19 | 7 | 0 | 5.977% | 2 | 0 | 30.335 |
| 5 | 0 | 33 | 19 | 9 | 0 | 5.905% | 2 | 0 | 31.555 |
| 5 | 1 | 36 | 19 | 15 | 0 | 5.711% | 2 | 0 | 26.278 |
| 6 | 0 | 33 | 19 | 12 | 0 | 5.535% | 2 | 0 | 27.357 |
| 6 | 1 | 25 | 19 | 4 | 0 | 6.120% | 2 | 0 | 31.161 |
| 7 | 0 | 24 | 19 | 5 | 0 | 6.330% | 2 | 0 | 27.752 |
| 7 | 1 | 23 | 19 | 4 | 0 | 5.716% | 2 | 0 | 26.974 |
| 8 | 0 | 23 | 19 | 4 | 0 | 6.046% | 2 | 0 | 25.492 |
| 8 | 1 | 29 | 19 | 10 | 0 | 6.327% | 2 | 0 | 33.087 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.5188 | 4.92 | 1.33 | 1.47 | 21.30 | 23.02 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
