# Checkpoint Summary

- run_dir: runs\260326013713_gpt5mini_seed42
- generated_at: 2026-03-26T03:11:50

## Overall

| Metric | Value |
|---|---:|
| eval_events | 595 |
| accepted | 346 |
| dedup_expr_hit | 172 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 46 | 21 | 8 | 0 | 8.310% | 0 | 0 |  |
| 0 | 1 | 49 | 21 | 15 | 0 | 7.938% | 0 | 0 |  |
| 1 | 0 | 52 | 19 | 20 | 0 | 8.422% | 2 | 0 | 28.894 |
| 1 | 1 | 53 | 19 | 20 | 0 | 6.262% | 2 | 0 | 23.452 |
| 2 | 0 | 40 | 19 | 12 | 0 | 7.314% | 2 | 0 | 40.614 |
| 2 | 1 | 26 | 19 | 3 | 0 | 6.281% | 2 | 0 | 29.123 |
| 3 | 0 | 29 | 19 | 10 | 0 | 6.626% | 2 | 0 | 27.568 |
| 3 | 1 | 28 | 19 | 9 | 0 | 6.529% | 2 | 0 | 38.547 |
| 4 | 0 | 28 | 19 | 8 | 0 | 6.150% | 2 | 0 | 39.413 |
| 4 | 1 | 27 | 19 | 8 | 0 | 6.260% | 2 | 0 | 35.829 |
| 5 | 0 | 29 | 19 | 9 | 0 | 6.862% | 2 | 0 | 48.715 |
| 5 | 1 | 39 | 19 | 18 | 0 | 6.497% | 2 | 0 | 39.873 |
| 6 | 0 | 28 | 19 | 7 | 0 | 6.076% | 2 | 0 | 34.466 |
| 6 | 1 | 22 | 19 | 3 | 0 | 6.497% | 2 | 0 | 38.841 |
| 7 | 0 | 27 | 19 | 8 | 0 | 5.767% | 2 | 0 | 33.050 |
| 7 | 1 | 24 | 19 | 4 | 0 | 6.222% | 2 | 0 | 44.825 |
| 8 | 0 | 23 | 19 | 4 | 0 | 5.929% | 2 | 0 | 55.279 |
| 8 | 1 | 25 | 19 | 6 | 0 | 6.290% | 2 | 0 | 36.208 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.6125 | 4.96 | 1.29 | 1.43 | 20.68 | 22.41 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
