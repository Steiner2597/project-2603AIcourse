# Checkpoint Summary

- run_dir: runs\260325205612_or_gpt
- generated_at: 2026-03-25T22:23:10

## Overall

| Metric | Value |
|---|---:|
| eval_events | 604 |
| accepted | 346 |
| dedup_expr_hit | 159 |
| eval_errors | 1 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 62 | 21 | 18 | 0 | 7.957% | 0 | 0 |  |
| 0 | 1 | 55 | 21 | 13 | 0 | 8.188% | 0 | 0 |  |
| 1 | 0 | 24 | 19 | 3 | 0 | 7.441% | 2 | 0 | 43.336 |
| 1 | 1 | 37 | 19 | 3 | 0 | 6.890% | 2 | 0 | 41.651 |
| 2 | 0 | 51 | 19 | 22 | 0 | 6.546% | 2 | 0 | 56.343 |
| 2 | 1 | 43 | 19 | 11 | 0 | 7.102% | 2 | 0 | 37.098 |
| 3 | 0 | 27 | 19 | 6 | 0 | 6.453% | 2 | 0 | 46.242 |
| 3 | 1 | 25 | 19 | 3 | 0 | 6.974% | 2 | 0 | 30.968 |
| 4 | 0 | 27 | 19 | 8 | 0 | 6.966% | 2 | 0 | 33.309 |
| 4 | 1 | 31 | 19 | 11 | 0 | 6.258% | 2 | 0 | 31.877 |
| 5 | 0 | 37 | 19 | 14 | 0 | 7.211% | 2 | 0 | 39.211 |
| 5 | 1 | 28 | 19 | 8 | 0 | 6.600% | 2 | 0 | 21.110 |
| 6 | 0 | 30 | 19 | 9 | 1 | 7.157% | 2 | 0 | 27.672 |
| 6 | 1 | 24 | 19 | 5 | 0 | 6.707% | 2 | 0 | 23.602 |
| 7 | 0 | 25 | 19 | 6 | 0 | 6.929% | 2 | 0 | 38.698 |
| 7 | 1 | 23 | 19 | 4 | 0 | 6.739% | 2 | 0 | 30.676 |
| 8 | 0 | 28 | 19 | 8 | 0 | 6.717% | 2 | 0 | 33.979 |
| 8 | 1 | 27 | 19 | 7 | 0 | 6.190% | 2 | 0 | 36.716 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 139.9688 | 5.86 | 0.39 | 0.53 | 6.22 | 8.27 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
