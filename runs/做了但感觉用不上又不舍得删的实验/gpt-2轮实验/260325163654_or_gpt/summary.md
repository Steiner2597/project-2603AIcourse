# Checkpoint Summary

- run_dir: runs\260325163654_or_gpt
- generated_at: 2026-03-25T17:16:11

## Overall

| Metric | Value |
|---|---:|
| eval_events | 269 |
| accepted | 144 |
| dedup_expr_hit | 69 |
| eval_errors | 0 |
| llm_events | 32 |
| llm_request_start | 16 |
| llm_request_done | 16 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 36 | 16 | 4 | 0 | 8.347% | 0 | 0 |  |
| 0 | 1 | 30 | 16 | 10 | 0 | 8.995% | 0 | 0 |  |
| 1 | 0 | 28 | 14 | 7 | 0 | 7.538% | 2 | 0 | 28.914 |
| 1 | 1 | 49 | 14 | 17 | 0 | 7.867% | 2 | 0 | 25.319 |
| 2 | 0 | 20 | 14 | 4 | 0 | 6.140% | 2 | 0 | 23.131 |
| 2 | 1 | 22 | 14 | 5 | 0 | 7.562% | 2 | 0 | 26.140 |
| 3 | 0 | 20 | 14 | 6 | 0 | 5.940% | 2 | 0 | 37.861 |
| 3 | 1 | 20 | 14 | 6 | 0 | 7.646% | 2 | 0 | 37.584 |
| 4 | 0 | 24 | 14 | 4 | 0 | 5.775% | 2 | 0 | 45.308 |
| 4 | 1 | 20 | 14 | 6 | 0 | 6.945% | 2 | 0 | 35.896 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.6188 | 4.89 | 1.36 | 1.50 | 21.76 | 23.47 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
