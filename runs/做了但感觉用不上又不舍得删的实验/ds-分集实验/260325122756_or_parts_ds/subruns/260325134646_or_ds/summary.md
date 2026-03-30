# Checkpoint Summary

- run_dir: runs\260325122756_or_parts_ds\subruns\260325134646_or_ds
- generated_at: 2026-03-25T15:15:12

## Overall

| Metric | Value |
|---|---:|
| eval_events | 616 |
| accepted | 346 |
| dedup_expr_hit | 149 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 88 | 21 | 26 | 0 | 8.381% | 0 | 0 |  |
| 0 | 1 | 69 | 21 | 20 | 0 | 8.571% | 0 | 0 |  |
| 1 | 0 | 61 | 19 | 20 | 0 | 8.039% | 2 | 0 | 9.066 |
| 1 | 1 | 35 | 19 | 5 | 0 | 8.382% | 2 | 0 | 6.924 |
| 2 | 0 | 32 | 19 | 9 | 0 | 7.947% | 2 | 0 | 9.352 |
| 2 | 1 | 33 | 19 | 8 | 0 | 8.355% | 2 | 0 | 8.570 |
| 3 | 0 | 30 | 19 | 10 | 0 | 7.711% | 2 | 0 | 10.241 |
| 3 | 1 | 24 | 19 | 5 | 0 | 8.184% | 2 | 0 | 12.088 |
| 4 | 0 | 21 | 19 | 1 | 0 | 7.684% | 2 | 0 | 13.424 |
| 4 | 1 | 24 | 19 | 4 | 0 | 7.895% | 2 | 0 | 10.647 |
| 5 | 0 | 27 | 19 | 6 | 0 | 7.092% | 2 | 0 | 20.227 |
| 5 | 1 | 21 | 19 | 1 | 0 | 7.566% | 2 | 0 | 8.087 |
| 6 | 0 | 29 | 19 | 7 | 0 | 7.171% | 2 | 0 | 18.922 |
| 6 | 1 | 23 | 19 | 4 | 0 | 7.776% | 2 | 0 | 7.295 |
| 7 | 0 | 24 | 19 | 5 | 0 | 7.158% | 2 | 0 | 30.274 |
| 7 | 1 | 24 | 19 | 5 | 0 | 7.829% | 2 | 0 | 10.407 |
| 8 | 0 | 21 | 19 | 2 | 0 | 7.276% | 2 | 0 | 19.837 |
| 8 | 1 | 30 | 19 | 11 | 0 | 7.211% | 2 | 0 | 13.053 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 21.3000 | 6.50 | 2.00 | 1.50 | 23.53 | 18.75 |
| First-Fit (FF) | 21.6000 | 8.00 | 0.50 | 0.00 | 5.88 | 0.00 |
| Best-Fit (BF) | 21.7000 | 8.50 | 0.00 | -0.50 | 0.00 | -6.25 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
