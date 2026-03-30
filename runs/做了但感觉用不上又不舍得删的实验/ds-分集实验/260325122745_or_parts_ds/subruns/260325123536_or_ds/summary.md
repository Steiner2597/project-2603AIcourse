# Checkpoint Summary

- run_dir: runs\260325122745_or_parts_ds\subruns\260325123536_or_ds
- generated_at: 2026-03-25T15:14:19

## Overall

| Metric | Value |
|---|---:|
| eval_events | 699 |
| accepted | 346 |
| dedup_expr_hit | 194 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 89 | 21 | 22 | 0 | 9.185% | 0 | 0 |  |
| 0 | 1 | 99 | 21 | 37 | 0 | 9.894% | 0 | 0 |  |
| 1 | 0 | 48 | 19 | 12 | 0 | 7.854% | 2 | 0 | 8.522 |
| 1 | 1 | 51 | 19 | 8 | 0 | 7.882% | 2 | 0 | 9.951 |
| 2 | 0 | 33 | 19 | 10 | 0 | 7.303% | 2 | 0 | 8.337 |
| 2 | 1 | 37 | 19 | 10 | 0 | 6.081% | 2 | 0 | 10.758 |
| 3 | 0 | 27 | 19 | 7 | 0 | 7.776% | 2 | 0 | 10.686 |
| 3 | 1 | 27 | 19 | 7 | 0 | 6.490% | 2 | 0 | 14.193 |
| 4 | 0 | 33 | 19 | 11 | 0 | 6.964% | 2 | 0 | 15.918 |
| 4 | 1 | 28 | 19 | 9 | 0 | 6.901% | 2 | 0 | 24.238 |
| 5 | 0 | 23 | 19 | 4 | 0 | 6.666% | 2 | 0 | 14.820 |
| 5 | 1 | 24 | 19 | 4 | 0 | 6.138% | 2 | 0 | 15.822 |
| 6 | 0 | 30 | 19 | 8 | 0 | 6.764% | 2 | 0 | 14.687 |
| 6 | 1 | 39 | 19 | 12 | 0 | 5.932% | 2 | 0 | 29.914 |
| 7 | 0 | 34 | 19 | 13 | 0 | 6.729% | 2 | 0 | 45.209 |
| 7 | 1 | 28 | 19 | 9 | 0 | 5.654% | 2 | 0 | 15.553 |
| 8 | 0 | 25 | 19 | 6 | 0 | 6.858% | 2 | 0 | 22.110 |
| 8 | 1 | 24 | 19 | 5 | 0 | 5.598% | 2 | 0 | 26.633 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 106.8500 | 5.07 | 0.84 | 1.22 | 14.16 | 19.40 |
| Best-Fit (BF) | 107.7000 | 5.90 | 0.00 | 0.38 | 0.00 | 6.09 |
| First-Fit (FF) | 108.1000 | 6.29 | -0.38 | 0.00 | -6.49 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
