**# FunSearch-Lite**



[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)



***\*FunSearch-Lite\**** is an evolutionary search system guided by Large Language Models (LLMs) for automated discovery and optimization of algorithmic heuristics. This project is a streamlined implementation of Google DeepMind's [FunSearch](https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/), specifically designed for AI course projects and research prototyping.



***\*FunSearch-Lite\**** 是一个基于大语言模型(LLM)的进化搜索系统，用于自动发现和优化算法启发式函数。本项目是对 Google DeepMind [FunSearch](https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) 论文的精简实现，专为 CS5491 AI 课程项目设计 (City University of Hong Kong, Spring 2026)。



\---



**## 🚀 Key Innovations | 核心创新**



**### 1. Functional Deduplication | 功能级去重 (Sample-Efficient)**

\- ***\*Two-Stage Filtering\****: Code hash + behavior signature to detect functionally equivalent code.

\- ***\*Impact\****: Reduces redundant evaluations by 20-40%, saving LLM API calls.



**### 2. Multi-Model Collaboration | 多模型协作 (Cost-Aware)**

\- ***\*Generator Model\****: Use cost-effective models (e.g., DeepSeek-Chat, GPT-3.5) for bulk candidate generation.

\- ***\*Refiner Model\****: Use powerful models (e.g., GPT-4) to optimize Top-K candidates.

\- ***\*Impact\****: Reduces API costs by ~87% while maintaining search quality.



**### 3. Diversity-Driven Search | 多样性驱动搜索 (Novelty-Oriented)**

\- ***\*Island Model\****: Multiple independent sub-populations with periodic migration.

\- ***\*Behavior Signature Diversity\****: Preserve candidates with novel decision patterns.

\- ***\*Impact\****: Avoids premature convergence to local optima.



**### 4. Standard Benchmark Support | 标准基准支持**

\- ***\*OR-Library\****: Built-in support for OR-Library Bin Packing instances (Falkenauer u* and t*).

\- ***\*Comparability\****: Directly compare results with academic literature.



**### 5. Search Trajectory Observability | 搜索可观测性**

\- ***\*Real-time Progress\****: `tqdm` integration showing generation progress and ETA.

\- ***\*Metric Tracking\****: Best/average scores per generation and failure taxonomy.

\- ***\*Visualization\****: Automated generation of evolution curves and failure distribution charts.



\---

**## 🛠️ Quick Start | 快速开始**



**### Installation | 安装**

Python 3.12.12



conda虚拟环境env：5491project



\```bash

\# Install in editable mode

pip install -e .



\# Or install dependencies manually

pip install pydantic pyyaml typer matplotlib openai tqdm

\```

**### Run Experiments | 运行实验**



***\*Recommended: Using the** **`run.py`** **wrapper\****



\```bash

\# 1. Set up API Key (once)

echo "DEEPSEEK_API_KEY=sk-xxx" > .env

echo "OPENAI_API_KEY=sk-xxx" >> .env



\# 2. Launch with one command

python run.py --api ds       # Use DeepSeek

python run.py --api gpt       # Use ChatGPT

python run.py --api ds -d orlib  # OR-Library dataset

python run.py --api gpt -d orlib -s large

python run.py --demo               # Demo mode (No API Key required)

python run.py --api gpt -g 3 -p 3 -y  # Quick test (~5 mins)

\```