# Checkpoint Summary

- run_dir: runs\260325122809_or_parts_ds\subruns\260325140103_or_ds
- generated_at: 2026-03-25T15:17:14

## Overall

| Metric | Value |
|---|---:|
| eval_events | 581 |
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
| 0 | 0 | 58 | 21 | 7 | 0 | 7.464% | 0 | 0 |  |
| 0 | 1 | 72 | 21 | 26 | 0 | 7.167% | 0 | 0 |  |
| 1 | 0 | 27 | 19 | 5 | 0 | 7.211% | 2 | 0 | 11.456 |
| 1 | 1 | 33 | 19 | 9 | 0 | 7.072% | 2 | 0 | 10.679 |
| 2 | 0 | 37 | 19 | 14 | 0 | 6.605% | 2 | 0 | 8.376 |
| 2 | 1 | 38 | 19 | 9 | 0 | 6.717% | 2 | 0 | 9.838 |
| 3 | 0 | 25 | 19 | 6 | 0 | 6.533% | 2 | 0 | 15.734 |
| 3 | 1 | 28 | 19 | 9 | 0 | 6.888% | 2 | 0 | 13.150 |
| 4 | 0 | 25 | 19 | 6 | 0 | 6.184% | 2 | 0 | 23.386 |
| 4 | 1 | 24 | 19 | 5 | 0 | 6.605% | 2 | 0 | 9.632 |
| 5 | 0 | 24 | 19 | 5 | 0 | 6.230% | 2 | 0 | 20.494 |
| 5 | 1 | 22 | 19 | 2 | 0 | 6.461% | 2 | 0 | 14.910 |
| 6 | 0 | 31 | 19 | 9 | 0 | 6.053% | 2 | 0 | 17.674 |
| 6 | 1 | 29 | 19 | 9 | 0 | 6.599% | 2 | 0 | 19.113 |
| 7 | 0 | 29 | 19 | 8 | 0 | 6.086% | 2 | 0 | 18.175 |
| 7 | 1 | 27 | 19 | 8 | 0 | 6.099% | 2 | 0 | 16.020 |
| 8 | 0 | 28 | 19 | 8 | 0 | 6.270% | 2 | 0 | 17.771 |
| 8 | 1 | 24 | 19 | 5 | 0 | 6.862% | 2 | 0 | 20.639 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 140.1875 | 5.70 | 0.55 | 0.69 | 8.80 | 10.79 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
