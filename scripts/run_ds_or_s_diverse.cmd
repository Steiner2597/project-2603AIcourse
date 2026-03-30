@echo off
setlocal
cd /d "%~dp0.."
set PYTHONUNBUFFERED=1
conda run --no-capture-output -n 5491project python -u -m funsearch_lite.cli --api ds --dataset orlib --size small --generations 2 --population 12 --islands 2 --gen-model deepseek-chat --ref-model deepseek-chat --llm-seeds 1 --llm-topk 1 --behavior-repeat-cap 1 --oversample-ratio 0.5 --log-interval 1 %*
endlocal
