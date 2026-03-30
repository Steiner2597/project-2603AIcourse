# Checkpoint Summary

- run_dir: runs\260326091944_gpt5nano+ds-reasoner_seed46
- generated_at: 2026-03-26T11:23:44

## Overall

| Metric | Value |
|---|---:|
| eval_events | 556 |
| accepted | 346 |
| dedup_expr_hit | 139 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 43 | 21 | 5 | 0 | 8.008% | 0 | 0 |  |
| 0 | 1 | 53 | 21 | 14 | 0 | 8.675% | 0 | 0 |  |
| 1 | 0 | 39 | 19 | 16 | 0 | 6.712% | 2 | 0 | 117.383 |
| 1 | 1 | 36 | 19 | 7 | 0 | 7.219% | 2 | 0 | 73.660 |
| 2 | 0 | 36 | 19 | 9 | 0 | 6.292% | 2 | 0 | 85.866 |
| 2 | 1 | 32 | 19 | 8 | 0 | 6.857% | 2 | 0 | 81.760 |
| 3 | 0 | 22 | 19 | 3 | 0 | 6.366% | 2 | 0 | 91.400 |
| 3 | 1 | 30 | 19 | 11 | 0 | 6.660% | 2 | 0 | 85.764 |
| 4 | 0 | 30 | 19 | 9 | 0 | 5.940% | 2 | 0 | 108.288 |
| 4 | 1 | 24 | 19 | 5 | 0 | 6.628% | 2 | 0 | 72.482 |
| 5 | 0 | 20 | 19 | 1 | 0 | 5.942% | 2 | 0 | 94.346 |
| 5 | 1 | 22 | 19 | 3 | 0 | 5.948% | 2 | 0 | 95.279 |
| 6 | 0 | 32 | 19 | 11 | 0 | 5.897% | 2 | 0 | 107.162 |
| 6 | 1 | 33 | 19 | 11 | 0 | 5.839% | 2 | 0 | 140.825 |
| 7 | 0 | 25 | 19 | 6 | 0 | 5.449% | 2 | 0 | 89.276 |
| 7 | 1 | 34 | 19 | 15 | 0 | 5.633% | 2 | 0 | 69.518 |
| 8 | 0 | 26 | 19 | 5 | 0 | 6.398% | 2 | 0 | 72.165 |
| 8 | 1 | 19 | 19 | 0 | 0 | 5.777% | 2 | 0 | 66.952 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.6438 | 4.89 | 1.36 | 1.50 | 21.77 | 23.48 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
