# Checkpoint Summary

- run_dir: runs\260326091750_ds-reasoner_seed46
- generated_at: 2026-03-26T11:50:13

## Overall

| Metric | Value |
|---|---:|
| eval_events | 588 |
| accepted | 346 |
| dedup_expr_hit | 163 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 43 | 21 | 5 | 0 | 8.008% | 0 | 0 |  |
| 0 | 1 | 53 | 21 | 14 | 0 | 8.675% | 0 | 0 |  |
| 1 | 0 | 38 | 19 | 14 | 0 | 6.384% | 2 | 0 | 86.469 |
| 1 | 1 | 39 | 19 | 13 | 0 | 7.195% | 2 | 0 | 125.079 |
| 2 | 0 | 32 | 19 | 8 | 0 | 5.999% | 2 | 0 | 106.581 |
| 2 | 1 | 34 | 19 | 7 | 0 | 6.700% | 2 | 0 | 161.929 |
| 3 | 0 | 28 | 19 | 9 | 0 | 6.191% | 2 | 0 | 163.863 |
| 3 | 1 | 33 | 19 | 14 | 0 | 6.474% | 2 | 0 | 144.798 |
| 4 | 0 | 36 | 19 | 9 | 0 | 5.925% | 2 | 0 | 151.818 |
| 4 | 1 | 33 | 19 | 13 | 0 | 6.344% | 2 | 0 | 143.299 |
| 5 | 0 | 25 | 19 | 5 | 0 | 5.620% | 2 | 0 | 135.517 |
| 5 | 1 | 29 | 19 | 8 | 0 | 6.091% | 2 | 0 | 238.225 |
| 6 | 0 | 34 | 19 | 9 | 0 | 5.747% | 2 | 0 | 93.501 |
| 6 | 1 | 24 | 19 | 5 | 0 | 5.705% | 2 | 0 | 154.782 |
| 7 | 0 | 27 | 19 | 7 | 0 | 5.838% | 2 | 0 | 145.962 |
| 7 | 1 | 28 | 19 | 9 | 0 | 6.860% | 2 | 0 | 140.374 |
| 8 | 0 | 26 | 19 | 7 | 0 | 5.415% | 2 | 0 | 118.835 |
| 8 | 1 | 26 | 19 | 7 | 0 | 6.428% | 2 | 0 | 127.119 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.6312 | 4.88 | 1.37 | 1.51 | 21.87 | 23.57 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
