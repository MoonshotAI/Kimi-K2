# PowerShell wrapper for KTransformers server
param(
  [string]$ModelDir = $env:MODEL_DIR,
  [int]$CacheLens = 30000,
  [switch]$EnableToolCalls
)

if (-not $ModelDir) { Write-Error "ModelDir not set. Set MODEL_DIR env var or pass -ModelDir."; exit 1 }
if (-not (Test-Path $ModelDir)) { Write-Error "Model directory not found: $ModelDir"; exit 1 }

$toolFlags = ""
if ($EnableToolCalls) { $toolFlags = "--enable-auto-tool-choice --tool-call-parser kimi_k2" }

python ktransformers/server/main.py --model_path "$ModelDir" --gguf_path "$ModelDir" --cache_lens $CacheLens $toolFlags
