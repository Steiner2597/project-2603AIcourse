# Checkpoint Summary

- run_dir: runs\260325120006_or_ds
- generated_at: 2026-03-25T13:58:54

## Overall

| Metric | Value |
|---|---:|
| eval_events | 638 |
| accepted | 346 |
| dedup_expr_hit | 175 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 62 | 21 | 18 | 0 | 7.957% | 0 | 0 |  |
| 0 | 1 | 55 | 21 | 13 | 0 | 8.188% | 0 | 0 |  |
| 1 | 0 | 42 | 19 | 9 | 0 | 7.409% | 2 | 0 | 10.873 |
| 1 | 1 | 44 | 19 | 12 | 0 | 7.723% | 2 | 0 | 8.989 |
| 2 | 0 | 34 | 19 | 9 | 0 | 7.384% | 2 | 0 | 12.767 |
| 2 | 1 | 40 | 19 | 9 | 0 | 7.320% | 2 | 0 | 10.095 |
| 3 | 0 | 36 | 19 | 9 | 0 | 7.004% | 2 | 0 | 13.410 |
| 3 | 1 | 25 | 19 | 5 | 0 | 6.667% | 2 | 0 | 13.377 |
| 4 | 0 | 26 | 19 | 6 | 0 | 7.262% | 2 | 0 | 10.316 |
| 4 | 1 | 28 | 19 | 7 | 0 | 6.766% | 2 | 0 | 11.514 |
| 5 | 0 | 29 | 19 | 8 | 0 | 6.928% | 2 | 0 | 10.660 |
| 5 | 1 | 38 | 19 | 16 | 0 | 7.187% | 2 | 0 | 9.380 |
| 6 | 0 | 26 | 19 | 6 | 0 | 6.939% | 2 | 0 | 9.551 |
| 6 | 1 | 39 | 19 | 12 | 0 | 6.757% | 2 | 0 | 8.737 |
| 7 | 0 | 34 | 19 | 13 | 0 | 6.598% | 2 | 0 | 7.975 |
| 7 | 1 | 27 | 19 | 8 | 0 | 6.254% | 2 | 0 | 8.523 |
| 8 | 0 | 25 | 19 | 6 | 0 | 6.394% | 2 | 0 | 8.076 |
| 8 | 1 | 28 | 19 | 9 | 0 | 5.917% | 2 | 0 | 11.055 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.7875 | 5.23 | 1.02 | 1.16 | 16.35 | 18.18 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
