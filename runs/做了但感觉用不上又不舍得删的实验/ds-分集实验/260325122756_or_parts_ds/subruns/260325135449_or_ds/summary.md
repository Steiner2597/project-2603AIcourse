# Checkpoint Summary

- run_dir: runs\260325122756_or_parts_ds\subruns\260325135449_or_ds
- generated_at: 2026-03-25T15:15:13

## Overall

| Metric | Value |
|---|---:|
| eval_events | 593 |
| accepted | 346 |
| dedup_expr_hit | 144 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 80 | 21 | 23 | 0 | 7.363% | 0 | 0 |  |
| 0 | 1 | 59 | 21 | 19 | 0 | 7.446% | 0 | 0 |  |
| 1 | 0 | 26 | 19 | 1 | 0 | 6.875% | 2 | 0 | 9.012 |
| 1 | 1 | 44 | 19 | 11 | 0 | 7.072% | 2 | 0 | 10.841 |
| 2 | 0 | 39 | 19 | 11 | 0 | 6.599% | 2 | 0 | 10.532 |
| 2 | 1 | 31 | 19 | 7 | 0 | 6.632% | 2 | 0 | 9.854 |
| 3 | 0 | 21 | 19 | 2 | 0 | 6.592% | 2 | 0 | 7.859 |
| 3 | 1 | 24 | 19 | 5 | 0 | 6.520% | 2 | 0 | 11.960 |
| 4 | 0 | 30 | 19 | 9 | 0 | 6.586% | 2 | 0 | 9.506 |
| 4 | 1 | 27 | 19 | 7 | 0 | 6.007% | 2 | 0 | 10.896 |
| 5 | 0 | 29 | 19 | 9 | 0 | 6.474% | 2 | 0 | 10.825 |
| 5 | 1 | 28 | 19 | 6 | 0 | 5.980% | 2 | 0 | 8.680 |
| 6 | 0 | 28 | 19 | 6 | 0 | 6.145% | 2 | 0 | 10.361 |
| 6 | 1 | 23 | 19 | 3 | 0 | 5.954% | 2 | 0 | 12.995 |
| 7 | 0 | 22 | 19 | 2 | 0 | 5.921% | 2 | 0 | 16.514 |
| 7 | 1 | 23 | 19 | 4 | 0 | 5.921% | 2 | 0 | 19.271 |
| 8 | 0 | 28 | 19 | 9 | 0 | 5.882% | 2 | 0 | 17.295 |
| 8 | 1 | 31 | 19 | 10 | 0 | 5.809% | 2 | 0 | 17.099 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 42.0500 | 5.13 | 2.25 | 2.25 | 30.51 | 30.51 |
| First-Fit (FF) | 42.9500 | 7.38 | 0.00 | 0.00 | 0.00 | 0.00 |
| Best-Fit (BF) | 42.9500 | 7.38 | 0.00 | 0.00 | 0.00 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
