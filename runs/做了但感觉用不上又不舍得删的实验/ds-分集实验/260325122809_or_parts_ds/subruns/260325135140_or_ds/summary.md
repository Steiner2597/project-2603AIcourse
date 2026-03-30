# Checkpoint Summary

- run_dir: runs\260325122809_or_parts_ds\subruns\260325135140_or_ds
- generated_at: 2026-03-25T15:16:59

## Overall

| Metric | Value |
|---|---:|
| eval_events | 657 |
| accepted | 346 |
| dedup_expr_hit | 167 |
| eval_errors | 2 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 82 | 21 | 13 | 0 | 8.583% | 0 | 0 |  |
| 0 | 1 | 84 | 21 | 28 | 0 | 8.583% | 0 | 0 |  |
| 1 | 0 | 34 | 19 | 9 | 0 | 8.329% | 2 | 0 | 10.230 |
| 1 | 1 | 33 | 19 | 6 | 0 | 8.421% | 2 | 0 | 9.576 |
| 2 | 0 | 47 | 19 | 17 | 0 | 8.092% | 2 | 0 | 11.569 |
| 2 | 1 | 36 | 19 | 7 | 0 | 8.197% | 2 | 0 | 13.653 |
| 3 | 0 | 26 | 19 | 5 | 2 | 8.013% | 2 | 0 | 10.977 |
| 3 | 1 | 30 | 19 | 7 | 0 | 8.000% | 2 | 0 | 11.259 |
| 4 | 0 | 32 | 19 | 9 | 0 | 7.579% | 2 | 0 | 11.901 |
| 4 | 1 | 29 | 19 | 7 | 0 | 7.855% | 2 | 0 | 10.026 |
| 5 | 0 | 28 | 19 | 7 | 0 | 7.461% | 2 | 0 | 18.262 |
| 5 | 1 | 20 | 19 | 1 | 0 | 7.829% | 2 | 0 | 10.730 |
| 6 | 0 | 32 | 19 | 10 | 0 | 6.974% | 2 | 0 | 17.382 |
| 6 | 1 | 40 | 19 | 17 | 0 | 7.724% | 2 | 0 | 14.087 |
| 7 | 0 | 23 | 19 | 4 | 0 | 7.329% | 2 | 0 | 27.659 |
| 7 | 1 | 22 | 19 | 3 | 0 | 7.342% | 2 | 0 | 16.195 |
| 8 | 0 | 27 | 19 | 8 | 0 | 7.263% | 2 | 0 | 23.199 |
| 8 | 1 | 32 | 19 | 9 | 0 | 7.053% | 2 | 0 | 31.507 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.8688 | 5.61 | 0.64 | 0.78 | 10.30 | 12.26 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
