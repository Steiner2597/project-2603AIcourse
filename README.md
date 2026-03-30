# FunSearch-Lite

FunSearch-Lite 是一个紧凑版的 LLM 引导进化搜索系统，用于自动设计在线装箱（Online Bin Packing）启发式函数。

当前实现重点强化了以下算法能力：

- 功能级去重：表达式哈希 + 行为签名哈希。
- 多样性驱动搜索：多岛并行进化 + 周期迁移。
- 成本感知模型协作：可选的生成模型 / 精炼模型双阶段流程。
- 反馈驱动提示：LLM 在每代读取当前岛屿优劣模式，而不是盲目随机提案。
- 防平台机制：停滞检测触发探索增强（随机重启比例与 LLM 候选临时提升）。
- 稀有度新颖性：使用行为出现频次定义 novelty，避免“哈希伪多样性”。
- 同分打破策略：在 score 相同条件下优先行为更稀有、局部扰动更稳定的候选。
- 评估限流：同代同岛对同一行为签名设置上限，避免单一行为吃掉预算。
- 行为签名增强：从“前缀截断轨迹”升级为“全轨迹采样 + bins_used”。

## 0) 创新点与算法设计总览

本项目不是单纯“随机生成表达式”，而是一个带反馈闭环的进化系统：

1. 生成与评估闭环
- LLM 负责提案（proposal）和精炼（refine）。
- 评估器在 OR-Library / synthetic 上给出真实用箱数。
- 搜索器根据 score、novelty、stability 三目标选择幸存者。

2. 进化主干
- 多岛并行 + 周期迁移，提升探索覆盖面。
- 变异 / 交叉 / 随机重启协同，避免早熟收敛。
- 过采样后多样性筛选，再进入下一代。

3. 抗同质化机制
- 表达式哈希去重：阻断重复代码。
- 行为签名去重：阻断功能等价候选反复评估。
- 行为上限限流：同代同岛同签名超过阈值直接丢弃。

4. 停滞自适应机制
- 检测连续若干代 best 不变且平台分占比高。
- 触发探索增强：临时提高 restart 与 llm seeds。

5. 结果可观测与可复现
- 请求级、评估级、代级 checkpoint。
- 自动 summary / baseline 图表。
- 建议按 split + 多 seed 报告 mean/std。

## 1) 安装

```bash
pip install -e .
```

## 2) API 配置（可选）

将 `.env.example` 复制为 `.env`，并填入你的配置。

```bash
copy .env.example .env
```

如果不提供 API Key，仍可运行 demo 模式与模板进化搜索。

若使用课程提供的网关（与 `test_your_api_key.py` 一致），建议配置：

- `OPENAI_API_KEY=<你的 key>`
- `HOST_URL=https://api.bltcy.ai`（或 `https://hk-api.gptbest.vip`）
- `OPENAI_GENERATOR_MODEL=gpt-5-nano`
- `OPENAI_REFINER_MODEL=gpt-5-nano`

## 3) 快速开始

```bash
python run.py --demo
python run.py --api gpt -g 20 -p 40 -i 4
python run.py --api ds -d orlib -s medium
python run.py --demo --compare -g 10 -p 24 -i 3
python -m funsearch_lite.cli --api gpt --compare -g 6 -p 20 -i 2
python -m funsearch_lite.cli --api gpt --host-url https://api.bltcy.ai --gen-model gpt-5-nano --ref-model gpt-5-nano -g 6 -p 20 -i 2
python -m funsearch_lite.cli --api ds --dataset orlib --orlib-mode per-source --compare -g 8 -p 16 -i 2
```

### 3.1 Windows 一键命令（复制一次直接跑）

如果你遇到“看起来卡死、看不到进度”的情况，建议使用下面的一键命令。

更推荐使用仓库内置快捷脚本（最省事，不需要每次敲长命令）：

CMD：

```bat
scripts\run_ds_or_s_diverse.cmd
```

PowerShell：

```powershell
.\scripts\run_ds_or_s_diverse.ps1
```

脚本默认参数等价于一条“DeepSeek + OR-Library small + 抗同质化”命令。
如果要临时追加参数，直接跟在脚本后面即可，例如：

```bat
scripts\run_ds_or_s_diverse.cmd --generations 4 --population 16
```

```powershell
.\scripts\run_ds_or_s_diverse.ps1 --generations 4 --population 16
```

CMD（推荐）

```bat
cd /d D:\SE\workspace\cs5491project\funsearch-1 && set PYTHONUNBUFFERED=1 && conda run --no-capture-output -n 5491project python -u -m funsearch_lite.cli --api ds --dataset orlib --size small --generations 2 --population 12 --islands 2 --gen-model deepseek-chat --ref-model deepseek-chat --llm-seeds 1 --llm-topk 1 --log-interval 1
```

用这个命令，目标时长大约 25-40 分钟（通常接近半小时）：

conda run --no-capture-output -n 5491project python -u -m funsearch_lite.cli --api ds --dataset orlib --size small --generations 2 --population 10 --islands 2 --gen-model deepseek-chat --ref-model deepseek-chat --llm-seeds 1 --llm-topk 1 --behavior-repeat-cap 1 --oversample-ratio 0.35 --restart-interval 1 --restart-ratio 0.15 --local-topk 2 --local-steps 2 --log-interval 1

如果你机器偏慢，想更稳落在 30 分钟内，把 generations 改成 1。

PowerShell

```powershell
Set-Location "D:\SE\workspace\cs5491project\funsearch-1"; $env:PYTHONUNBUFFERED="1"; conda run --no-capture-output -n 5491project python -u -m funsearch_lite.cli --api ds --dataset orlib --size small --generations 2 --population 12 --islands 2 --gen-model deepseek-chat --ref-model deepseek-chat --llm-seeds 1 --llm-topk 1 --log-interval 1
```

说明：

- 以上命令不包含安装步骤，仅用于直接运行实验。
- 如未安装项目，请先执行一次 `pip install -e .`（仅首次需要）。
- 关键点是 `conda run --no-capture-output`，否则 Conda 会缓存输出，导致长时间看不到日志。
- 运行时会看到 `[search]`、`[llm]`、`[gen x/y]` 日志，便于判断程序处于正常执行。
- 想跑约 5 分钟实验，可把 `--size small --generations 2 --population 12` 改为 `--size medium --generations 8 --population 24`。
- 若出现行为同质化偏高，可加：`--behavior-repeat-cap 1 --oversample-ratio 0.5`。

## 4) 输出结果

每次运行会在 `runs/` 下生成一个结果目录，目录名格式为（时间精确到秒）：

- OR-Library：`yymmddHHMMSS_or_<provider>`（不再包含 size）
- Synthetic：`yymmddHHMMSS_syn_<size>_<provider>`
- 例如：`260324121105_or_ds`
- `provider`: `ds` / `gpt` / `none`

并包含以下文件：

- `metrics.json`：进化轨迹和汇总指标（含 FF/BF 基线、gap ratio）。
- `best_expression.txt`：当前最优启发式表达式。
- `curve.png`：每代 gap ratio 最优值与平均值曲线图。
- `comparison_table.md` / `comparison_table.csv`：FF / BF / 本方法对比表（ratio 指标按百分比 `%` 展示；含 vs BF/FF 的百分点差与相对提升）。
- `status.json`：运行状态（`running` / `failed` / `completed`）。
- `checkpoints/`：检查点目录。
- `checkpoints/init_progress.json`：初始化种群阶段进度（即使尚未发起 LLM 请求也会更新）。
- `checkpoints/requests.jsonl`：每次 LLM 请求的开始/结束/错误事件。
- `checkpoints/eval_events.jsonl`：每次候选评估事件（包含 `generation/island/population_slot/attempt/source`）。
- `checkpoints/gen_XXXX.json`：每一代的指标快照。
- `checkpoints/local_search.json`：Top-K 局部搜索后处理日志。
- `checkpoints/binpack*.json`：OR-Library 的 8 个测试集分别一个文件，包含汇总与基线。
- `baseline_compare.png`：FF/BF/Ours 基线对比图。
- `binpacks/binpack*/report.json`：按文件分组的实例明细与基线对比（OR-Library）。

当使用 `--dataset orlib --orlib-mode per-source` 时，会生成一个父目录：

- `yymmddHHMMSS_or_parts_<provider>/`
- `subruns/`：8 个子实验目录（每个对应一个 `binpackX`）。
- `aggregate_summary.json`：8 个子实验合并后的机器可读总报告。
- `aggregate_summary.md`：8 个测试集各自结果 + 总体汇总（实例数加权）。
- `aggregate_summary.csv`：便于课程报告/表格工具二次分析。

### 4.1 评分与指标定义

- `bins_used`：某实例实际使用的箱子数量。
- `optimal_bins`：OR-Library 给出的最优箱数（synthetic 没有该字段）。
- `gap`：`bins_used - optimal_bins`。
- `gap_ratio`：$ (bins\_used - optimal\_bins) / optimal\_bins $，主评分指标，越小越好。
- `avg_gap_ratio`：对所有有最优解的实例取 `gap_ratio` 均值。
- `avg_bins_used`：若无最优解（仅 synthetic）时退化使用的主指标。
- 基线：FF / BF 会用同一组实例计算 `avg_gap_ratio` 和 `avg_bins_used`，写入 `metrics.json` 与 per-binpack 报告。

可用汇总脚本一键生成统计结果：

```bash
python -m funsearch_lite.summarize --run-dir runs/260324121105_or_ds
```

或汇总最新一次运行：

```bash
python -m funsearch_lite.summarize
```

输出文件：

- `summary.json`：机器可读汇总。
- `summary.md`：按 generation/island 的可读表格。

说明：每次实验结束后会自动生成 `summary.json` 和 `summary.md`，通常无需手动执行汇总脚本。

OR-Library 数据集：

- `--orlib-mode combined`（默认）：8 个文件（binpack1-8）联合搜索与统一打分。
- `--orlib-mode per-source`：自动拆分为 8 个子实验，分别训练并输出合并总报告。
- 每个文件含 20 个实例，评分按“平均相对最优解的 gap ratio”（越低越好）。
- `--size` 对 OR-Library 将被忽略，只对 synthetic 起作用。
- FF / BF 基线在每次实验中自动计算。

## 5) 参数说明（完整）

以下参数对应命令：`python -m funsearch_lite.cli [参数]`

| 参数 | 默认值 | 说明 | 常用建议 |
|---|---:|---|---|
| `--api, -a` | `none` | 模型提供方，`none/gpt/ds` | 用 DeepSeek 时设 `ds` |
| `--demo` | `false` | 强制无 API 模式（忽略 `--api`） | 排查本地逻辑时开启 |
| `--dataset, -d` | `synthetic` | 数据集类型，`synthetic/orlib` | 正式实验建议 `orlib` |
| `--orlib-mode` | `combined` | OR-Library 运行方式，`combined/per-source` | 需要分集优化时用 `per-source` |
| `--size, -s` | `small` | 数据规模，`small/medium/large` | 快测 `small`，正式对比 `large` |
| `--generations, -g` | `30` | 进化代数（>=1） | 1-2 快测，8-20 正式 |
| `--population, -p` | `48` | 每岛种群规模（>=8） | 12-24 课程实验常用 |
| `--islands, -i` | `4` | 岛屿数量（>=1） | 2-4 较稳妥 |
| `--seed` | `42` | 随机种子 | 保持可复现固定值 |
| `--compare` | `false` | 生成 FF/BF/Ours 对比表 | 报告实验建议开启 |
| `--host-url` | 空 | 网关地址（会自动补 `/v1`） | 只在自定义网关时设置 |
| `--gen-model` | 环境变量或内置默认 | 生成模型名覆盖 | DeepSeek 建议 `deepseek-chat` |
| `--ref-model` | 环境变量或内置默认 | 精炼模型名覆盖 | 通常与生成模型一致 |
| `--llm-seeds` | `4` | 每阶段 LLM 候选数（>=0） | 卡预算可设 `1` |
| `--llm-topk` | `3` | 发给 refiner 的 Top-K（>=1） | 小实验设 `1` 即可 |
| `--log-interval` | `1` | 每 N 代打印日志（>=1） | 建议保留 `1` |
| `--quiet` | `false` | 关闭进度日志 | 长跑调试不建议开 |
| `--behavior-repeat-cap` | `2` | 单岛内同行为签名最大重复数（>=1） | 抗同质化可设 `1` |
| `--behavior-eval-cap` | `3` | 同代同岛同行为签名可接受上限（>=1） | `small` 常用 `1-2` |
| `--behavior-signature-points` | `120` | 行为签名采样点数（20-400） | `small` 建议 `160-220` |
| `--oversample-ratio` | `0.35` | 过采样比例（0.0-1.0） | 抗同质化建议 `0.3-0.6` |
| `--restart-interval` | `1` | 每 N 代触发一次随机重启注入 | 通常保持 `1` |
| `--restart-ratio` | `0.15` | 每次重启注入比例（0.0-0.8） | `0.15-0.25` |
| `--stagnation-window` | `2` | 停滞检测窗口（>=2） | 常用 `2` |
| `--stagnation-score-anchor` | `1567.0` | 平台锚点分数（small 常用） | `small` 用 `1567` |
| `--stagnation-ratio-threshold` | `0.35` | 平台占比阈值，超过则触发增强 | `0.3-0.4` |
| `--stagnation-restart-boost` | `1.8` | 停滞时 restart 比例乘子 | `1.5-2.2` |
| `--stagnation-llm-boost` | `1` | 停滞时额外 LLM 候选数 | `0-2` |
| `--local-topk` | `2` | 局部搜索使用的 top-k 精英表达式数 | 2-5 常用 |
| `--local-steps` | `2` | 每个精英表达式的微扰步数 | 2-8 常用 |

参数组合模板：

- 快速验证（1-2 分钟）：

```bash
python -m funsearch_lite.cli --api ds --dataset orlib --size small --generations 1 --population 8 --islands 2 --llm-seeds 1 --llm-topk 1
```

- 抗同质化配置（推荐）：

```bash
python -m funsearch_lite.cli --api ds --dataset orlib --size small --generations 2 --population 12 --islands 2 --llm-seeds 1 --llm-topk 1 --behavior-repeat-cap 1 --oversample-ratio 0.5
```

## 6) 核心思路

在在线装箱场景中，每个到达物品都要在当前可放置的箱子中选一个。候选启发式会对每个可行箱子打分，并选择分数最高的箱子放入。

分数函数由安全算术表达式构成，可使用如下特征：

- `item`、`remaining`、`after`（放入后剩余容量）
- `fill`（当前装载率）
- `mean_remaining`、`stdev_remaining`
- `exact_fit`（是否恰好装满，0/1）

优化目标：OR-Library 以平均相对最优解的 `avg_gap_ratio` 为主目标（越低越好）；若实例缺少最优解（仅 synthetic），则退化为最小化 `avg_bins_used`。

### 6.1 搜索目标与排序规则

候选排序使用分层目标：

1. 主目标：`score` = `avg_gap_ratio`（有最优解时使用）；若缺少最优解，回退为 `avg_bins_used`。
2. 次目标：`novelty`（行为稀有度，越少见越高）。
3. 次目标：`stability`（局部扰动后分数变化越小越高）。

搜索使用上述分层排序，并对 `novelty/stability` 采用退火权重，减少“同分候选全挤在一个行为簇”的问题。

### 6.2 LLM 介入机制

LLM 每代都做两件事：

1. Proposal：生成新表达式候选。
2. Refine：基于当前 top-k 精英表达式进行改写优化。

提示词会注入当前代反馈信息（好样本、差样本、主导行为占比），形成自我优化闭环。

### 6.3 去重与限流机制

评估前后有三层过滤：

1. `dedup_expr_hit`：表达式哈希重复。
2. `dedup_behavior_hit`：行为签名命中缓存。
3. `dedup_behavior_overuse`：同代同岛同签名超上限。

这三层共同减少冗余评估与同质化。

### 6.4 建议实验协议（课程报告）

1. 按 split 分开跑：`small` 与 `large` 独立实验。
2. 每个 split 跑 3 个 seed（如 42/43/44）。
3. 同一 split 内除 seed 外参数保持一致。
4. 统一报告：best、mean±std、相对 BF/FF 的归一化指标。
