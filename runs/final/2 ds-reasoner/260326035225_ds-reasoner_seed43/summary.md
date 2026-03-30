# Checkpoint Summary

- run_dir: runs\260326035225_ds-reasoner_seed43
- generated_at: 2026-03-26T06:11:39

## Overall

| Metric | Value |
|---|---:|
| eval_events | 687 |
| accepted | 346 |
| dedup_expr_hit | 200 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 62 | 21 | 18 | 0 | 7.957% | 0 | 0 |  |
| 0 | 1 | 55 | 21 | 13 | 0 | 8.188% | 0 | 0 |  |
| 1 | 0 | 24 | 19 | 3 | 0 | 7.203% | 2 | 0 | 95.383 |
| 1 | 1 | 37 | 19 | 3 | 0 | 6.890% | 2 | 0 | 77.284 |
| 2 | 0 | 51 | 19 | 22 | 0 | 6.796% | 2 | 0 | 137.645 |
| 2 | 1 | 61 | 19 | 20 | 0 | 7.102% | 2 | 0 | 120.455 |
| 3 | 0 | 37 | 19 | 14 | 0 | 6.729% | 2 | 0 | 108.854 |
| 3 | 1 | 41 | 19 | 15 | 0 | 6.751% | 2 | 0 | 105.975 |
| 4 | 0 | 40 | 19 | 15 | 0 | 6.840% | 2 | 0 | 110.013 |
| 4 | 1 | 34 | 19 | 8 | 0 | 6.811% | 2 | 0 | 136.857 |
| 5 | 0 | 31 | 19 | 10 | 0 | 7.276% | 2 | 0 | 92.322 |
| 5 | 1 | 29 | 19 | 6 | 0 | 7.108% | 2 | 0 | 144.215 |
| 6 | 0 | 37 | 19 | 14 | 0 | 6.515% | 2 | 0 | 117.422 |
| 6 | 1 | 29 | 19 | 8 | 0 | 7.115% | 2 | 0 | 111.580 |
| 7 | 0 | 32 | 19 | 8 | 0 | 6.508% | 2 | 0 | 161.840 |
| 7 | 1 | 28 | 19 | 7 | 0 | 6.247% | 2 | 0 | 130.838 |
| 8 | 0 | 28 | 19 | 8 | 0 | 6.688% | 2 | 0 | 57.535 |
| 8 | 1 | 31 | 19 | 8 | 0 | 6.903% | 2 | 0 | 118.956 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 140.1562 | 6.22 | 0.03 | 0.17 | 0.46 | 2.63 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
