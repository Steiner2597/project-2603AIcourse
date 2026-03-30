# Checkpoint Summary

- run_dir: runs\260325122756_or_parts_ds\subruns\260325140328_or_ds
- generated_at: 2026-03-25T15:15:16

## Overall

| Metric | Value |
|---|---:|
| eval_events | 557 |
| accepted | 346 |
| dedup_expr_hit | 128 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 70 | 21 | 19 | 0 | 6.449% | 0 | 0 |  |
| 0 | 1 | 65 | 21 | 19 | 0 | 6.400% | 0 | 0 |  |
| 1 | 0 | 26 | 19 | 3 | 0 | 6.018% | 2 | 0 | 10.268 |
| 1 | 1 | 39 | 19 | 12 | 0 | 6.027% | 2 | 0 | 10.368 |
| 2 | 0 | 26 | 19 | 5 | 0 | 5.621% | 2 | 0 | 11.948 |
| 2 | 1 | 26 | 19 | 5 | 0 | 5.758% | 2 | 0 | 10.002 |
| 3 | 0 | 23 | 19 | 3 | 0 | 5.637% | 2 | 0 | 11.053 |
| 3 | 1 | 21 | 19 | 2 | 0 | 5.609% | 2 | 0 | 16.585 |
| 4 | 0 | 25 | 19 | 5 | 0 | 5.365% | 2 | 0 | 10.604 |
| 4 | 1 | 24 | 19 | 4 | 0 | 5.736% | 2 | 0 | 12.768 |
| 5 | 0 | 25 | 19 | 5 | 0 | 5.361% | 2 | 0 | 10.373 |
| 5 | 1 | 30 | 19 | 9 | 0 | 5.704% | 2 | 0 | 16.532 |
| 6 | 0 | 26 | 19 | 5 | 0 | 5.006% | 2 | 0 | 13.884 |
| 6 | 1 | 29 | 19 | 9 | 0 | 5.843% | 2 | 0 | 14.810 |
| 7 | 0 | 26 | 19 | 7 | 0 | 5.346% | 2 | 0 | 13.181 |
| 7 | 1 | 27 | 19 | 8 | 0 | 5.374% | 2 | 0 | 21.191 |
| 8 | 0 | 27 | 19 | 5 | 0 | 5.656% | 2 | 0 | 21.660 |
| 8 | 1 | 22 | 19 | 3 | 0 | 5.580% | 2 | 0 | 20.553 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 86.5000 | 4.22 | 2.17 | 2.17 | 33.96 | 33.96 |
| First-Fit (FF) | 88.3000 | 6.39 | 0.00 | 0.00 | 0.00 | 0.00 |
| Best-Fit (BF) | 88.3000 | 6.39 | 0.00 | 0.00 | 0.00 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
