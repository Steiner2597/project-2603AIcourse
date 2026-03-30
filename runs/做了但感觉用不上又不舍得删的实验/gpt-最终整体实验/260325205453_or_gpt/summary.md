# Checkpoint Summary

- run_dir: runs\260325205453_or_gpt
- generated_at: 2026-03-25T22:23:49

## Overall

| Metric | Value |
|---|---:|
| eval_events | 596 |
| accepted | 346 |
| dedup_expr_hit | 173 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 46 | 21 | 8 | 0 | 8.310% | 0 | 0 |  |
| 0 | 1 | 49 | 21 | 15 | 0 | 7.938% | 0 | 0 |  |
| 1 | 0 | 45 | 19 | 16 | 0 | 8.524% | 2 | 0 | 49.134 |
| 1 | 1 | 59 | 19 | 25 | 0 | 6.611% | 2 | 0 | 45.099 |
| 2 | 0 | 37 | 19 | 12 | 0 | 7.406% | 2 | 0 | 42.283 |
| 2 | 1 | 29 | 19 | 5 | 0 | 6.781% | 2 | 0 | 34.956 |
| 3 | 0 | 30 | 19 | 6 | 1 | 6.421% | 2 | 0 | 32.823 |
| 3 | 1 | 34 | 19 | 15 | 0 | 6.866% | 2 | 0 | 38.910 |
| 4 | 0 | 32 | 19 | 9 | 0 | 6.111% | 2 | 0 | 42.252 |
| 4 | 1 | 25 | 19 | 6 | 0 | 6.484% | 2 | 0 | 46.585 |
| 5 | 0 | 32 | 19 | 12 | 0 | 5.420% | 2 | 0 | 49.837 |
| 5 | 1 | 25 | 19 | 6 | 0 | 6.737% | 2 | 0 | 39.904 |
| 6 | 0 | 24 | 19 | 5 | 0 | 5.875% | 2 | 0 | 31.233 |
| 6 | 1 | 25 | 19 | 6 | 0 | 6.517% | 2 | 0 | 42.194 |
| 7 | 0 | 29 | 19 | 9 | 0 | 5.605% | 2 | 0 | 42.963 |
| 7 | 1 | 30 | 19 | 11 | 0 | 5.941% | 2 | 0 | 35.037 |
| 8 | 0 | 21 | 19 | 2 | 0 | 5.424% | 2 | 0 | 41.085 |
| 8 | 1 | 24 | 19 | 5 | 0 | 5.472% | 2 | 0 | 55.224 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.6937 | 4.88 | 1.36 | 1.50 | 21.83 | 23.54 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
