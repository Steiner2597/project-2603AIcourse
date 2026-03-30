# Checkpoint Summary

- run_dir: runs\260325122809_or_parts_ds\subruns\260325142445_or_ds
- generated_at: 2026-03-25T15:17:48

## Overall

| Metric | Value |
|---|---:|
| eval_events | 585 |
| accepted | 346 |
| dedup_expr_hit | 156 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 59 | 21 | 11 | 0 | 6.025% | 0 | 0 |  |
| 0 | 1 | 49 | 21 | 16 | 0 | 5.964% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 14 | 0 | 5.711% | 2 | 0 | 10.886 |
| 1 | 1 | 31 | 19 | 6 | 0 | 5.310% | 2 | 0 | 8.375 |
| 2 | 0 | 37 | 19 | 11 | 0 | 5.648% | 2 | 0 | 9.980 |
| 2 | 1 | 39 | 19 | 9 | 0 | 4.872% | 2 | 0 | 11.352 |
| 3 | 0 | 27 | 19 | 8 | 0 | 5.345% | 2 | 0 | 11.867 |
| 3 | 1 | 30 | 19 | 9 | 0 | 4.452% | 2 | 0 | 12.151 |
| 4 | 0 | 26 | 19 | 5 | 0 | 5.241% | 2 | 0 | 14.027 |
| 4 | 1 | 24 | 19 | 5 | 0 | 4.496% | 2 | 0 | 15.832 |
| 5 | 0 | 25 | 19 | 4 | 0 | 5.583% | 2 | 0 | 19.860 |
| 5 | 1 | 27 | 19 | 5 | 0 | 4.455% | 2 | 0 | 12.161 |
| 6 | 0 | 38 | 19 | 16 | 0 | 5.564% | 2 | 0 | 16.176 |
| 6 | 1 | 26 | 19 | 7 | 0 | 4.606% | 2 | 0 | 15.872 |
| 7 | 0 | 29 | 19 | 10 | 0 | 4.820% | 2 | 0 | 22.111 |
| 7 | 1 | 31 | 19 | 11 | 0 | 4.392% | 2 | 0 | 16.934 |
| 8 | 0 | 26 | 19 | 6 | 0 | 4.589% | 2 | 0 | 22.642 |
| 8 | 1 | 22 | 19 | 3 | 0 | 4.609% | 2 | 0 | 22.619 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.8000 | 5.49 | 0.76 | 0.90 | 12.22 | 14.14 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
