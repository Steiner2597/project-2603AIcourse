# Checkpoint Summary

- run_dir: runs\260325122756_or_parts_ds\subruns\260325130643_or_ds
- generated_at: 2026-03-25T15:15:11

## Overall

| Metric | Value |
|---|---:|
| eval_events | 590 |
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
| 0 | 0 | 78 | 21 | 23 | 0 | 7.236% | 0 | 0 |  |
| 0 | 1 | 109 | 21 | 40 | 0 | 7.793% | 0 | 0 |  |
| 1 | 0 | 41 | 19 | 13 | 0 | 5.773% | 2 | 0 | 9.383 |
| 1 | 1 | 22 | 19 | 2 | 0 | 5.738% | 2 | 0 | 10.668 |
| 2 | 0 | 25 | 19 | 3 | 0 | 5.813% | 2 | 0 | 13.415 |
| 2 | 1 | 25 | 19 | 4 | 0 | 5.505% | 2 | 0 | 10.803 |
| 3 | 0 | 27 | 19 | 7 | 0 | 5.114% | 2 | 0 | 10.434 |
| 3 | 1 | 21 | 19 | 1 | 0 | 5.911% | 2 | 0 | 10.621 |
| 4 | 0 | 19 | 19 | 0 | 0 | 4.510% | 2 | 0 | 8.680 |
| 4 | 1 | 25 | 19 | 5 | 0 | 6.493% | 2 | 0 | 13.122 |
| 5 | 0 | 25 | 19 | 6 | 0 | 5.927% | 2 | 0 | 12.590 |
| 5 | 1 | 25 | 19 | 5 | 0 | 4.528% | 2 | 0 | 9.034 |
| 6 | 0 | 26 | 19 | 7 | 0 | 5.128% | 2 | 0 | 11.847 |
| 6 | 1 | 25 | 19 | 6 | 0 | 5.681% | 2 | 0 | 14.439 |
| 7 | 0 | 23 | 19 | 4 | 0 | 5.112% | 2 | 0 | 15.804 |
| 7 | 1 | 26 | 19 | 7 | 0 | 4.864% | 2 | 0 | 17.410 |
| 8 | 0 | 23 | 19 | 4 | 0 | 6.613% | 2 | 0 | 16.496 |
| 8 | 1 | 25 | 19 | 6 | 0 | 4.874% | 2 | 0 | 10.935 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 414.6000 | 3.51 | 1.43 | 1.72 | 29.01 | 32.91 |
| Best-Fit (BF) | 420.3500 | 4.94 | 0.00 | 0.29 | 0.00 | 5.50 |
| First-Fit (FF) | 421.5000 | 5.23 | -0.29 | 0.00 | -5.83 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
