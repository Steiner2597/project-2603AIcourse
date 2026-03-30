# OR-Library 8 个测试集特性与调参分析

## 1. 目的

本文档用于支持 `--dataset orlib --orlib-mode per-source` 的分集优化实验，回答两个问题：

1. 每个 `binpack` 子集各自在考察算法的什么能力。
2. 在 FunSearch-Lite 当前框架下，优先该调哪些参数。

说明：以下统计均由当前代码直接读取 `data/orlib/binpack*.txt` 计算得到（每个子集 20 个实例）。

## 2. 全局观察

OR-Library 的 8 个子集可以自然分成两组：

1. `binpack1-4`：容量 `150`，物品规模更分散，`tight_mean < 1`（平均装载紧度不满 1），说明存在不可避免的碎片和舍入损失。
2. `binpack5-8`：容量 `100`，实例几乎是“精确可装满”（`tight_mean = 1`），对“避免额外开箱”的精细决策更敏感。

这里的装载紧度定义为：

`tightness = sum(items) / (capacity * optimal_bins)`

越接近 1，越说明最优解接近“满箱利用”。

## 3. 数据统计（按子集）

### 3.1 规模与最优箱数统计

| 子集 | 实例数 | 平均物品数 | 容量 | 平均最优箱数 | 最优箱数范围 | 平均紧度 |
|---|---:|---:|---:|---:|---:|---:|
| binpack1 | 20 | 120 | 150 | 49.15 | 46-52 | 0.9860 |
| binpack2 | 20 | 250 | 150 | 101.70 | 97-106 | 0.9939 |
| binpack3 | 20 | 500 | 150 | 201.20 | 196-207 | 0.9972 |
| binpack4 | 20 | 1000 | 150 | 400.55 | 393-411 | 0.9986 |
| binpack5 | 20 | 60 | 100 | 20.00 | 20-20 | 1.0000 |
| binpack6 | 20 | 120 | 100 | 40.00 | 40-40 | 1.0000 |
| binpack7 | 20 | 249 | 100 | 83-83 | 83-83 | 1.0000 |
| binpack8 | 20 | 501 | 100 | 167-167 | 167-167 | 1.0000 |

### 3.2 物品分布结构统计

| 子集 | item 均值 | q10 | q50 | q90 | 大件占比(>0.5cap) | 小件占比(<0.2cap) | 变异系数 CV |
|---|---:|---:|---:|---:|---:|---:|---:|
| binpack1 | 60.57 | 28.0 | 60.0 | 92.0 | 0.3137 | 0.1117 | 0.3816 |
| binpack2 | 60.64 | 28.0 | 61.0 | 93.0 | 0.3144 | 0.1122 | 0.3817 |
| binpack3 | 60.19 | 28.0 | 60.0 | 93.0 | 0.3100 | 0.1209 | 0.3877 |
| binpack4 | 60.00 | 27.0 | 60.0 | 92.0 | 0.3080 | 0.1246 | 0.3890 |
| binpack5 | 33.33 | 25.4 | 30.4 | 45.9 | 0.0000 | 0.0000 | 0.2281 |
| binpack6 | 33.33 | 25.5 | 30.8 | 45.4 | 0.0000 | 0.0000 | 0.2234 |
| binpack7 | 33.33 | 25.5 | 30.7 | 45.7 | 0.0000 | 0.0000 | 0.2254 |
| binpack8 | 33.33 | 25.5 | 30.8 | 45.5 | 0.0000 | 0.0000 | 0.2227 |

解释：

1. `binpack1-4` 含明显“大件+小件”混合，考察“先填紧还是留余量”的策略平衡。
2. `binpack5-8` 物品集中在中等区间（约 25-46，相对容量 100），更像“组合匹配”问题，要求减少不必要碎片。

## 4. 每个测试集在考察什么能力

### 4.1 binpack1

1. 能力重点：在中等规模下学习到有效的开箱/复用平衡。
2. 风险：过度贪心地追求立即紧填，可能导致后续碎片上升。
3. 关注指标：`avg_gap_ratio` 稳定下降、`stability` 不要过低。

### 4.2 binpack2

1. 能力重点：规模翻倍后的策略一致性与泛化。
2. 风险：同一表达式在更长序列上放大误差。
3. 关注指标：分代曲线波动幅度、局部搜索提升幅度。

### 4.3 binpack3

1. 能力重点：大规模下对行为同质化的抑制能力。
2. 风险：大量候选坍缩到少数行为签名。
3. 关注指标：`dedup_behavior_overuse` 频次、有效接受率。

### 4.4 binpack4

1. 能力重点：超大规模时的稳定排序与鲁棒性。
2. 风险：早期错误模式在长序列中累计成额外开箱。
3. 关注指标：最终 `best_score` 与 `avg_score` 的收敛差距。

### 4.5 binpack5

1. 能力重点：在“理论可满箱”场景下减少 1 箱级别的失误。
2. 风险：表达式对微小余量差异不敏感，导致错失精确配对。
3. 关注指标：是否接近 0 gap，和 BF 的差距。

### 4.6 binpack6

1. 能力重点：在更长序列的可满箱场景保持一致决策。
2. 风险：局部最优偏好在长序列中滚雪球。
3. 关注指标：`stability`、局部搜索是否能进一步压低 gap。

### 4.7 binpack7

1. 能力重点：高实例长度下的中尺度组合匹配。
2. 风险：若搜索多样性不足，容易锁死在次优组合模式。
3. 关注指标：新颖性贡献是否有效（而非只靠 score）。

### 4.8 binpack8

1. 能力重点：最大规模下的整体鲁棒性与抗退化能力。
2. 风险：搜索后期出现平台期，难以突破。
3. 关注指标：平台检测触发后的改善幅度（重启/LLM boost 是否有效）。

## 5. 参数到能力的映射建议

下表给出“如果某类子集表现差，优先改什么参数”：

| 现象 | 主要出现在 | 优先调整参数 | 调参方向 |
|---|---|---|---|
| 行为同质化严重，候选被大量去重 | binpack3/4/7/8 | `--oversample-ratio`, `--behavior-repeat-cap`, `--behavior-eval-cap` | 提高 oversample；保持 repeat/eval cap 偏小 |
| 早熟收敛，平台期长 | binpack4/8 | `--restart-ratio`, `--stagnation-ratio-threshold`, `--stagnation-restart-boost`, `--stagnation-llm-boost` | 增强停滞触发后的探索强度 |
| 对精确匹配不敏感，gap 下不去 | binpack5/6 | `--local-topk`, `--local-steps`, `--behavior-signature-points` | 增强后期精修；适度提高签名分辨率 |
| 代间波动大，不稳定 | binpack1/2/6 | `--stability-weight-final`, `--novelty-weight-final`, `--anneal` | 后期提高 stability 权重，适当降低 novelty |
| 大规模下提升慢 | binpack3/4/8 | `--generations`, `--population`, `--islands`, `--llm-seeds` | 增算力预算，先增 population/islands 再增 generations |

## 6. 推荐实验模板（分集优化）

建议按以下顺序做：

1. 固定一套“稳健初始参数”，在 `--orlib-mode per-source` 下跑 8 个子实验。
2. 从 `aggregate_summary.md` 找出最差 2-3 个子集。
3. 仅围绕这些子集做有针对性的参数网格（不要全参数同时扫）。
4. 将调好的策略回测到 `--orlib-mode combined`，验证总体是否同步提升。

## 7. 关于“分集训练后再合并”是否等价

结论：通常不等价，但非常有分析价值。

1. 不等价原因：搜索过程有去重、新颖性、稳定性、停滞重启等动态机制，联合训练与分集训练的搜索轨迹不同。
2. 分集价值：能定位“哪类数据形态”是短板，指导表达式结构和参数设计。
3. 实践建议：报告里同时保留 `combined` 与 `per-source` 两组结果，前者体现全局性能，后者体现可解释性与诊断能力。

## 8. 可直接复现的命令

```bash
conda run --no-capture-output -n 5491project python -u -m funsearch_lite.cli \
  --api ds --dataset orlib --orlib-mode per-source --compare \
  --generations 8 --population 16 --islands 2 --seed 42 \
  --llm-seeds 2 --llm-topk 2 \
  --behavior-repeat-cap 1 --behavior-eval-cap 1 \
  --behavior-repeat-cap-final 2 --behavior-eval-cap-final 3 \
  --novelty-weight-final 0.2 --stability-weight-final 1.0 \
  --restart-ratio 0.18 --stagnation-ratio-threshold 0.40 \
  --stagnation-restart-boost 1.5 --stagnation-llm-boost 0 \
  --anneal
```

运行后重点看：

1. `aggregate_summary.md`：8 个子集各自与总体结果。
2. `subruns/*/metrics.json`：每个子集的细粒度指标与表达式。
3. `subruns/*/checkpoints/eval_events.jsonl`：行为去重、接受率与平台期细节。
