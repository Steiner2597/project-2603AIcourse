# Checkpoint Summary

- run_dir: runs\260325122809_or_parts_ds\subruns\260325123606_or_ds
- generated_at: 2026-03-25T15:16:04

## Overall

| Metric | Value |
|---|---:|
| eval_events | 648 |
| accepted | 346 |
| dedup_expr_hit | 165 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 104 | 21 | 25 | 0 | 9.394% | 0 | 0 |  |
| 0 | 1 | 81 | 21 | 27 | 0 | 9.468% | 0 | 0 |  |
| 1 | 0 | 47 | 19 | 12 | 0 | 7.451% | 2 | 0 | 8.514 |
| 1 | 1 | 31 | 19 | 4 | 0 | 7.638% | 2 | 0 | 8.960 |
| 2 | 0 | 33 | 19 | 8 | 0 | 7.399% | 2 | 0 | 10.816 |
| 2 | 1 | 32 | 19 | 8 | 0 | 7.229% | 2 | 0 | 11.655 |
| 3 | 0 | 23 | 19 | 4 | 0 | 6.612% | 2 | 0 | 13.323 |
| 3 | 1 | 30 | 19 | 9 | 0 | 7.025% | 2 | 0 | 14.855 |
| 4 | 0 | 23 | 19 | 4 | 0 | 7.894% | 2 | 0 | 13.968 |
| 4 | 1 | 26 | 19 | 7 | 0 | 7.432% | 2 | 0 | 10.145 |
| 5 | 0 | 29 | 19 | 8 | 0 | 6.996% | 2 | 0 | 18.503 |
| 5 | 1 | 24 | 19 | 5 | 0 | 7.355% | 2 | 0 | 19.279 |
| 6 | 0 | 25 | 19 | 4 | 0 | 5.763% | 2 | 0 | 13.213 |
| 6 | 1 | 32 | 19 | 9 | 0 | 7.674% | 2 | 0 | 19.681 |
| 7 | 0 | 24 | 19 | 5 | 0 | 6.023% | 2 | 0 | 14.605 |
| 7 | 1 | 26 | 19 | 7 | 0 | 7.521% | 2 | 0 | 15.396 |
| 8 | 0 | 31 | 19 | 12 | 0 | 6.364% | 2 | 0 | 11.415 |
| 8 | 1 | 27 | 19 | 7 | 0 | 6.979% | 2 | 0 | 12.535 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.8625 | 5.07 | 1.18 | 1.32 | 18.91 | 20.68 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
