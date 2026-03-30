# Checkpoint Summary

- run_dir: runs\260326013733_ds-chat+ds-reasoner_seed42
- generated_at: 2026-03-26T03:32:51

## Overall

| Metric | Value |
|---|---:|
| eval_events | 630 |
| accepted | 346 |
| dedup_expr_hit | 192 |
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
| 1 | 0 | 52 | 19 | 20 | 0 | 8.422% | 2 | 0 | 89.842 |
| 1 | 1 | 43 | 19 | 14 | 0 | 6.518% | 2 | 0 | 49.807 |
| 2 | 0 | 43 | 19 | 15 | 0 | 7.604% | 2 | 0 | 94.849 |
| 2 | 1 | 33 | 19 | 6 | 0 | 6.620% | 2 | 0 | 60.984 |
| 3 | 0 | 39 | 19 | 16 | 0 | 6.817% | 2 | 0 | 67.586 |
| 3 | 1 | 27 | 19 | 7 | 0 | 6.496% | 2 | 0 | 48.414 |
| 4 | 0 | 31 | 19 | 10 | 0 | 6.437% | 2 | 0 | 136.085 |
| 4 | 1 | 33 | 19 | 11 | 0 | 6.291% | 2 | 0 | 67.323 |
| 5 | 0 | 38 | 19 | 16 | 0 | 6.977% | 2 | 0 | 59.717 |
| 5 | 1 | 23 | 19 | 4 | 0 | 6.747% | 2 | 0 | 75.698 |
| 6 | 0 | 35 | 19 | 13 | 0 | 7.295% | 2 | 0 | 81.564 |
| 6 | 1 | 39 | 19 | 14 | 0 | 6.227% | 2 | 0 | 42.504 |
| 7 | 0 | 28 | 19 | 9 | 0 | 6.779% | 2 | 0 | 65.031 |
| 7 | 1 | 26 | 19 | 7 | 0 | 6.425% | 2 | 0 | 65.096 |
| 8 | 0 | 23 | 19 | 4 | 0 | 7.643% | 2 | 0 | 70.985 |
| 8 | 1 | 22 | 19 | 3 | 0 | 6.809% | 2 | 0 | 74.821 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.7750 | 5.59 | 0.66 | 0.80 | 10.52 | 12.47 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
