# Checkpoint Summary

- run_dir: runs\260326091904_gpt5nano+gpt5mini_seed46
- generated_at: 2026-03-26T10:53:02

## Overall

| Metric | Value |
|---|---:|
| eval_events | 560 |
| accepted | 346 |
| dedup_expr_hit | 150 |
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
| 1 | 0 | 38 | 19 | 14 | 0 | 6.384% | 2 | 0 | 33.099 |
| 1 | 1 | 39 | 19 | 9 | 0 | 6.897% | 2 | 0 | 42.215 |
| 2 | 0 | 33 | 19 | 11 | 0 | 6.012% | 2 | 0 | 38.335 |
| 2 | 1 | 26 | 19 | 5 | 0 | 7.123% | 2 | 0 | 27.703 |
| 3 | 0 | 20 | 19 | 1 | 0 | 6.121% | 2 | 0 | 36.406 |
| 3 | 1 | 28 | 19 | 9 | 0 | 7.165% | 2 | 0 | 33.225 |
| 4 | 0 | 26 | 19 | 7 | 0 | 5.585% | 2 | 0 | 49.100 |
| 4 | 1 | 26 | 19 | 6 | 0 | 6.182% | 2 | 0 | 49.135 |
| 5 | 0 | 30 | 19 | 10 | 0 | 5.845% | 2 | 0 | 32.923 |
| 5 | 1 | 26 | 19 | 6 | 0 | 6.042% | 2 | 0 | 30.134 |
| 6 | 0 | 36 | 19 | 14 | 0 | 6.135% | 2 | 0 | 18.865 |
| 6 | 1 | 31 | 19 | 12 | 0 | 6.174% | 2 | 0 | 31.945 |
| 7 | 0 | 28 | 19 | 9 | 0 | 5.480% | 2 | 0 | 42.531 |
| 7 | 1 | 27 | 19 | 8 | 0 | 6.511% | 2 | 0 | 37.742 |
| 8 | 0 | 29 | 19 | 8 | 0 | 5.580% | 2 | 0 | 32.021 |
| 8 | 1 | 21 | 19 | 2 | 0 | 5.542% | 2 | 0 | 44.655 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.7375 | 4.92 | 1.33 | 1.47 | 21.33 | 23.05 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
