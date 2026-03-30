# Checkpoint Summary

- run_dir: runs\260325155154_or_gpt
- generated_at: 2026-03-25T16:23:44

## Overall

| Metric | Value |
|---|---:|
| eval_events | 223 |
| accepted | 116 |
| dedup_expr_hit | 63 |
| eval_errors | 0 |
| llm_events | 24 |
| llm_request_start | 12 |
| llm_request_done | 12 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 36 | 16 | 4 | 0 | 8.347% | 0 | 0 |  |
| 0 | 1 | 30 | 16 | 10 | 0 | 8.995% | 0 | 0 |  |
| 1 | 0 | 27 | 14 | 8 | 0 | 7.243% | 2 | 0 | 26.547 |
| 1 | 1 | 38 | 14 | 11 | 0 | 7.834% | 2 | 0 | 39.182 |
| 2 | 0 | 22 | 14 | 6 | 0 | 6.237% | 2 | 0 | 36.106 |
| 2 | 1 | 28 | 14 | 10 | 0 | 7.235% | 2 | 0 | 35.172 |
| 3 | 0 | 17 | 14 | 3 | 0 | 5.758% | 2 | 0 | 32.362 |
| 3 | 1 | 25 | 14 | 11 | 0 | 6.172% | 2 | 0 | 33.887 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.7688 | 4.99 | 1.25 | 1.39 | 20.08 | 21.82 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
