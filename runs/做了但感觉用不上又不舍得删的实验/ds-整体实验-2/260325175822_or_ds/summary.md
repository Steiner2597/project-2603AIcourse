# Checkpoint Summary

- run_dir: runs\260325175822_or_ds
- generated_at: 2026-03-25T19:24:43

## Overall

| Metric | Value |
|---|---:|
| eval_events | 550 |
| accepted | 346 |
| dedup_expr_hit | 133 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 59 | 21 | 11 | 0 | 8.320% | 0 | 0 |  |
| 0 | 1 | 51 | 21 | 18 | 0 | 8.076% | 0 | 0 |  |
| 1 | 0 | 34 | 19 | 5 | 0 | 7.563% | 2 | 0 | 8.857 |
| 1 | 1 | 34 | 19 | 6 | 0 | 6.743% | 2 | 0 | 10.075 |
| 2 | 0 | 36 | 19 | 11 | 0 | 6.728% | 2 | 0 | 9.889 |
| 2 | 1 | 25 | 19 | 5 | 0 | 6.788% | 2 | 0 | 11.671 |
| 3 | 0 | 32 | 19 | 9 | 0 | 6.102% | 2 | 0 | 10.886 |
| 3 | 1 | 26 | 19 | 7 | 0 | 6.633% | 2 | 0 | 12.081 |
| 4 | 0 | 22 | 19 | 3 | 0 | 6.435% | 2 | 0 | 11.316 |
| 4 | 1 | 22 | 19 | 3 | 0 | 7.117% | 2 | 0 | 14.400 |
| 5 | 0 | 20 | 19 | 1 | 0 | 6.326% | 2 | 0 | 12.053 |
| 5 | 1 | 22 | 19 | 3 | 0 | 6.361% | 2 | 0 | 14.649 |
| 6 | 0 | 25 | 19 | 6 | 0 | 5.989% | 2 | 0 | 10.020 |
| 6 | 1 | 34 | 19 | 13 | 0 | 6.977% | 2 | 0 | 18.974 |
| 7 | 0 | 26 | 19 | 7 | 0 | 5.976% | 2 | 0 | 18.188 |
| 7 | 1 | 31 | 19 | 12 | 0 | 6.903% | 2 | 0 | 12.333 |
| 8 | 0 | 20 | 19 | 1 | 0 | 5.904% | 2 | 0 | 13.935 |
| 8 | 1 | 31 | 19 | 12 | 0 | 6.753% | 2 | 0 | 19.934 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.9812 | 5.04 | 1.21 | 1.35 | 19.36 | 21.12 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
