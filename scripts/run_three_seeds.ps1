param(
    [int[]]$Seeds = @(42, 43, 44),
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$CliArgs
)

if (-not $CliArgs -or $CliArgs.Count -eq 0) {
    Write-Host "Usage:"
    Write-Host "  .\scripts\run_three_seeds.ps1 [funsearch_lite.cli args without --seed]"
    Write-Host "Example:"
    Write-Host "  .\scripts\run_three_seeds.ps1 --api ds --dataset orlib --generations 8 --population 16 --islands 2 --llm-seeds 1 --llm-topk 2 --anneal --compare"
    exit 1
}

Set-Location (Join-Path $PSScriptRoot "..")
$env:PYTHONUNBUFFERED = "1"

foreach ($seed in $Seeds) {
    Write-Host ""
    Write-Host "[seed-run] starting seed=$seed"
    conda run --no-capture-output -n 5491project python -u -m funsearch_lite.cli @CliArgs --seed $seed
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[seed-run] failed at seed=$seed"
        exit $LASTEXITCODE
    }
    Write-Host "[seed-run] finished seed=$seed"
}

Write-Host ""
Write-Host "[seed-run] all seeds finished: $($Seeds -join ', ')"
exit 0
