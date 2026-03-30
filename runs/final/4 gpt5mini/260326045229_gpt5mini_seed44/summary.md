# Checkpoint Summary

- run_dir: runs\260326045229_gpt5mini_seed44
- generated_at: 2026-03-26T06:22:18

## Overall

| Metric | Value |
|---|---:|
| eval_events | 578 |
| accepted | 346 |
| dedup_expr_hit | 143 |
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
| 1 | 0 | 40 | 19 | 9 | 0 | 6.837% | 2 | 0 | 28.872 |
| 1 | 1 | 47 | 19 | 13 | 0 | 6.373% | 2 | 0 | 22.734 |
| 2 | 0 | 27 | 19 | 6 | 0 | 6.168% | 2 | 0 | 30.267 |
| 2 | 1 | 28 | 19 | 7 | 0 | 6.088% | 2 | 0 | 25.968 |
| 3 | 0 | 26 | 19 | 5 | 0 | 6.496% | 2 | 0 | 30.702 |
| 3 | 1 | 30 | 19 | 11 | 0 | 6.890% | 2 | 0 | 27.837 |
| 4 | 0 | 23 | 19 | 3 | 0 | 6.782% | 2 | 0 | 33.724 |
| 4 | 1 | 35 | 19 | 10 | 0 | 6.347% | 2 | 0 | 32.102 |
| 5 | 0 | 23 | 19 | 4 | 0 | 6.448% | 2 | 0 | 27.717 |
| 5 | 1 | 35 | 19 | 11 | 0 | 6.158% | 2 | 0 | 31.450 |
| 6 | 0 | 25 | 19 | 3 | 0 | 6.001% | 2 | 0 | 36.497 |
| 6 | 1 | 30 | 19 | 10 | 0 | 6.355% | 2 | 0 | 31.346 |
| 7 | 0 | 22 | 19 | 3 | 0 | 6.102% | 2 | 0 | 26.075 |
| 7 | 1 | 26 | 19 | 7 | 0 | 7.459% | 2 | 0 | 29.705 |
| 8 | 0 | 23 | 19 | 4 | 0 | 6.156% | 2 | 0 | 30.956 |
| 8 | 1 | 28 | 19 | 8 | 0 | 6.810% | 2 | 0 | 29.537 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.9688 | 5.16 | 1.09 | 1.23 | 17.42 | 19.22 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
