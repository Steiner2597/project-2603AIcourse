# Checkpoint Summary

- run_dir: runs\260325205620_or_gpt
- generated_at: 2026-03-25T22:25:49

## Overall

| Metric | Value |
|---|---:|
| eval_events | 569 |
| accepted | 346 |
| dedup_expr_hit | 154 |
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
| 1 | 0 | 34 | 19 | 10 | 0 | 7.361% | 2 | 0 | 50.219 |
| 1 | 1 | 35 | 19 | 7 | 0 | 6.191% | 2 | 0 | 41.835 |
| 2 | 0 | 34 | 19 | 8 | 0 | 6.786% | 2 | 0 | 43.188 |
| 2 | 1 | 31 | 19 | 8 | 0 | 6.507% | 2 | 0 | 50.699 |
| 3 | 0 | 28 | 19 | 8 | 0 | 6.626% | 2 | 0 | 44.332 |
| 3 | 1 | 27 | 19 | 8 | 0 | 6.910% | 2 | 0 | 65.323 |
| 4 | 0 | 24 | 19 | 5 | 0 | 6.569% | 2 | 0 | 27.093 |
| 4 | 1 | 22 | 19 | 3 | 0 | 6.571% | 2 | 0 | 50.607 |
| 5 | 0 | 31 | 19 | 11 | 0 | 6.425% | 2 | 0 | 37.453 |
| 5 | 1 | 26 | 19 | 6 | 0 | 6.423% | 2 | 0 | 32.416 |
| 6 | 0 | 29 | 19 | 10 | 0 | 5.846% | 2 | 0 | 25.646 |
| 6 | 1 | 30 | 19 | 11 | 0 | 6.860% | 2 | 0 | 42.794 |
| 7 | 0 | 23 | 19 | 4 | 0 | 6.519% | 2 | 0 | 34.990 |
| 7 | 1 | 23 | 19 | 4 | 0 | 6.303% | 2 | 0 | 30.490 |
| 8 | 0 | 41 | 19 | 20 | 0 | 5.321% | 2 | 0 | 65.899 |
| 8 | 1 | 21 | 19 | 2 | 0 | 6.883% | 2 | 0 | 40.297 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.8625 | 4.98 | 1.27 | 1.41 | 20.31 | 22.05 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
