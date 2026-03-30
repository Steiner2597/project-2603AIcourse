# Checkpoint Summary

- run_dir: runs\260325122809_or_parts_ds\subruns\260325124717_or_ds
- generated_at: 2026-03-25T15:16:21

## Overall

| Metric | Value |
|---|---:|
| eval_events | 711 |
| accepted | 346 |
| dedup_expr_hit | 208 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 104 | 21 | 25 | 0 | 8.686% | 0 | 0 |  |
| 0 | 1 | 81 | 21 | 27 | 0 | 8.712% | 0 | 0 |  |
| 1 | 0 | 44 | 19 | 11 | 0 | 6.181% | 2 | 0 | 10.628 |
| 1 | 1 | 46 | 19 | 16 | 0 | 6.256% | 2 | 0 | 8.153 |
| 2 | 0 | 31 | 19 | 9 | 0 | 6.150% | 2 | 0 | 10.616 |
| 2 | 1 | 35 | 19 | 9 | 0 | 5.859% | 2 | 0 | 8.629 |
| 3 | 0 | 31 | 19 | 9 | 0 | 5.673% | 2 | 0 | 11.293 |
| 3 | 1 | 39 | 19 | 17 | 0 | 5.335% | 2 | 0 | 9.977 |
| 4 | 0 | 29 | 19 | 7 | 1 | 6.270% | 2 | 0 | 11.854 |
| 4 | 1 | 28 | 19 | 5 | 0 | 5.320% | 2 | 0 | 7.467 |
| 5 | 0 | 26 | 19 | 6 | 0 | 5.495% | 2 | 0 | 14.339 |
| 5 | 1 | 25 | 19 | 6 | 0 | 5.804% | 2 | 0 | 11.195 |
| 6 | 0 | 34 | 19 | 7 | 0 | 4.740% | 2 | 0 | 60.038 |
| 6 | 1 | 33 | 19 | 10 | 0 | 6.530% | 2 | 0 | 10.631 |
| 7 | 0 | 26 | 19 | 7 | 0 | 5.699% | 2 | 0 | 71.282 |
| 7 | 1 | 41 | 19 | 20 | 0 | 5.709% | 2 | 0 | 18.455 |
| 8 | 0 | 25 | 19 | 6 | 0 | 4.644% | 2 | 0 | 68.321 |
| 8 | 1 | 33 | 19 | 11 | 0 | 6.416% | 2 | 0 | 27.258 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.9688 | 5.48 | 0.77 | 0.91 | 12.26 | 14.18 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
