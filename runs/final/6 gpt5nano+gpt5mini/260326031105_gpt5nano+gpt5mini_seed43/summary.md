# Checkpoint Summary

- run_dir: runs\260326031105_gpt5nano+gpt5mini_seed43
- generated_at: 2026-03-26T04:48:01

## Overall

| Metric | Value |
|---|---:|
| eval_events | 689 |
| accepted | 346 |
| dedup_expr_hit | 210 |
| eval_errors | 0 |
| llm_events | 64 |
| llm_request_start | 32 |
| llm_request_done | 32 |
| llm_request_error | 0 |

## By Generation/Island

| generation | island | eval_events | accepted | dedup_expr_hit | eval_error | avg_score_accepted | llm_requests | llm_errors | llm_avg_elapsed_sec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 62 | 21 | 18 | 0 | 7.957% | 0 | 0 |  |
| 0 | 1 | 55 | 21 | 13 | 0 | 8.188% | 0 | 0 |  |
| 1 | 0 | 27 | 19 | 1 | 0 | 7.078% | 2 | 0 | 30.936 |
| 1 | 1 | 51 | 19 | 16 | 0 | 7.398% | 2 | 0 | 24.192 |
| 2 | 0 | 53 | 19 | 18 | 0 | 6.506% | 2 | 0 | 30.456 |
| 2 | 1 | 80 | 19 | 30 | 0 | 6.956% | 2 | 0 | 25.315 |
| 3 | 0 | 29 | 19 | 10 | 0 | 6.707% | 2 | 0 | 37.938 |
| 3 | 1 | 26 | 19 | 6 | 0 | 6.986% | 2 | 0 | 45.403 |
| 4 | 0 | 34 | 19 | 13 | 0 | 6.363% | 2 | 0 | 24.687 |
| 4 | 1 | 32 | 19 | 10 | 0 | 6.512% | 2 | 0 | 34.852 |
| 5 | 0 | 30 | 19 | 11 | 0 | 5.811% | 2 | 0 | 48.630 |
| 5 | 1 | 45 | 19 | 19 | 0 | 6.667% | 2 | 0 | 35.920 |
| 6 | 0 | 24 | 19 | 5 | 0 | 5.553% | 2 | 0 | 55.526 |
| 6 | 1 | 33 | 19 | 8 | 0 | 6.927% | 2 | 0 | 35.477 |
| 7 | 0 | 29 | 19 | 10 | 0 | 5.662% | 2 | 0 | 42.672 |
| 7 | 1 | 29 | 19 | 10 | 0 | 6.424% | 2 | 0 | 31.526 |
| 8 | 0 | 28 | 19 | 9 | 0 | 5.154% | 2 | 0 | 47.846 |
| 8 | 1 | 22 | 19 | 3 | 0 | 6.146% | 2 | 0 | 37.346 |

## Baseline Comparison

| Method | Avg Bins | Gap to Opt (%) | vs BF (pp) | vs FF (pp) | Improve vs BF (%) | Improve vs FF (%) |
|---|---:|---:|---:|---:|---:|---:|
| FunSearch-Lite (Ours) | 138.5250 | 4.84 | 1.41 | 1.55 | 22.63 | 24.32 |
| Best-Fit (BF) | 140.2250 | 6.25 | 0.00 | 0.14 | 0.00 | 2.18 |
| First-Fit (FF) | 140.5312 | 6.39 | -0.14 | 0.00 | -2.23 | 0.00 |

- winner: FunSearch-Lite (Ours)
- chart: baseline_compare.png
