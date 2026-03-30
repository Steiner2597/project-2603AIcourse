# Checkpoint Summary

- run_dir: runs\260326045055_ds-chat+gpt5mini_seed44
- generated_at: 2026-03-26T06:15:38

## Overall

| Metric | Value |
|---|---:|
| eval_events | 557 |
| accepted | 346 |
| dedup_expr_hit | 134 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 59 | 21 | 11 | 0 | 8.320% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 18 | 0 | 8.076% | 0 | 0 |  |
| 1 | 0 | 36 | 19 | 8 | 0 | 7.390% | 2 | 0 | 14.921 |
| 1 | 1 | 38 | 19 | 8 | 0 | 6.683% | 2 | 0 | 17.558 |
| 2 | 0 | 33 | 19 | 9 | 1 | 6.341% | 2 | 0 | 23.245 |
| 2 | 1 | 30 | 19 | 9 | 0 | 6.361% | 2 | 0 | 25.335 |
| 3 | 0 | 29 | 19 | 8 | 0 | 6.098% | 2 | 0 | 19.329 |
| 3 | 1 | 25 | 19 | 5 | 0 | 5.925% | 2 | 0 | 14.415 |
| 4 | 0 | 22 | 19 | 3 | 0 | 6.068% | 2 | 0 | 18.236 |
| 4 | 1 | 25 | 19 | 6 | 0 | 5.953% | 2 | 0 | 22.119 |
| 5 | 0 | 21 | 19 | 2 | 0 | 6.642% | 2 | 0 | 20.674 |
| 5 | 1 | 26 | 19 | 7 | 0 | 6.116% | 2 | 0 | 20.885 |
| 6 | 0 | 30 | 19 | 9 | 0 | 6.042% | 2 | 0 | 25.893 |
| 6 | 1 | 25 | 19 | 5 | 0 | 5.817% | 2 | 0 | 33.838 |
| 7 | 0 | 24 | 19 | 5 | 0 | 6.395% | 2 | 0 | 20.928 |
| 7 | 1 | 30 | 19 | 7 | 0 | 6.150% | 2 | 0 | 29.599 |
| 8 | 0 | 26 | 19 | 7 | 0 | 7.074% | 2 | 0 | 27.915 |
| 8 | 1 | 27 | 19 | 7 | 0 | 5.652% | 2 | 0 | 29.324 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.1062 | 5.28 | 0.97 | 1.11 | 15.45 | 17.30 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
