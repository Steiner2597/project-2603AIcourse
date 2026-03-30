# Checkpoint Summary

- run_dir: runs\260325122809_or_parts_ds\subruns\260325122809_or_ds
- generated_at: 2026-03-25T15:15:48

## Overall

| Metric | Value |
|---|---:|
| eval_events | 679 |
| accepted | 346 |
| dedup_expr_hit | 171 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 104 | 21 | 25 | 0 | 9.259% | 0 | 0 |  |
| 0 | 1 | 81 | 21 | 27 | 0 | 9.437% | 0 | 0 |  |
| 1 | 0 | 51 | 19 | 9 | 0 | 7.225% | 2 | 0 | 9.476 |
| 1 | 1 | 36 | 19 | 7 | 0 | 6.871% | 2 | 0 | 12.219 |
| 2 | 0 | 39 | 19 | 7 | 0 | 7.592% | 2 | 0 | 9.269 |
| 2 | 1 | 31 | 19 | 5 | 0 | 6.389% | 2 | 0 | 7.708 |
| 3 | 0 | 25 | 19 | 2 | 0 | 7.318% | 2 | 0 | 9.032 |
| 3 | 1 | 27 | 19 | 8 | 0 | 6.164% | 2 | 0 | 8.644 |
| 4 | 0 | 21 | 19 | 2 | 0 | 7.373% | 2 | 0 | 10.752 |
| 4 | 1 | 27 | 19 | 7 | 0 | 6.998% | 2 | 0 | 8.584 |
| 5 | 0 | 34 | 19 | 9 | 0 | 8.152% | 2 | 0 | 10.326 |
| 5 | 1 | 31 | 19 | 10 | 0 | 6.027% | 2 | 0 | 7.795 |
| 6 | 0 | 30 | 19 | 10 | 0 | 7.554% | 2 | 0 | 12.036 |
| 6 | 1 | 24 | 19 | 5 | 0 | 6.692% | 2 | 0 | 10.637 |
| 7 | 0 | 27 | 19 | 7 | 0 | 7.426% | 2 | 0 | 13.352 |
| 7 | 1 | 34 | 19 | 15 | 0 | 5.890% | 2 | 0 | 27.538 |
| 8 | 0 | 32 | 19 | 10 | 0 | 6.754% | 2 | 0 | 12.858 |
| 8 | 1 | 25 | 19 | 6 | 0 | 7.777% | 2 | 0 | 20.062 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| FunSearch-Lite (Ours) | 140.4125 | 6.37 | -0.12 | 0.02 | -1.90 | 0.33 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: Best-Fit (BF)
- chart: baseline_compare.png
