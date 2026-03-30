@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0.."

if "%~1"=="" (
    echo Usage:
    echo   scripts\run_three_seeds.cmd [funsearch_lite.cli args without --seed]
    echo Example:
    echo   scripts\run_three_seeds.cmd --api ds --dataset orlib --generations 8 --population 16 --islands 2 --llm-seeds 1 --llm-topk 2 --anneal --compare
    exit /b 1
)

set PYTHONUNBUFFERED=1

for %%S in (42 43 44) do (
    echo.
    echo [seed-run] starting seed=%%S
    conda run --no-capture-output -n 5491project python -u -m funsearch_lite.cli %* --seed %%S
    if errorlevel 1 (
        echo [seed-run] failed at seed=%%S
        exit /b !errorlevel!
    )
    echo [seed-run] finished seed=%%S
)

echo.
echo [seed-run] all seeds finished: 42, 43, 44
exit /b 0
