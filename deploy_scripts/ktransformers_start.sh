#!/usr/bin/env bash
# KTransformers server example
# Usage: MODEL_DIR=/path/to/K2 ./deploy_scripts/ktransformers_start.sh

MODEL_DIR=${MODEL_DIR:-/path/to/K2}
CACHE_LENS=${CACHE_LENS:-30000}
TOOL_FLAGS=""

# Enable tool-calls if requested by setting ENABLE_TOOL_CALLS=1
if [ "${ENABLE_TOOL_CALLS:-0}" -eq 1 ]; then
  TOOL_FLAGS="--enable-auto-tool-choice --tool-call-parser kimi_k2"
fi

if [ ! -d "$MODEL_DIR" ]; then
  echo "Model directory not found: $MODEL_DIR"
  exit 1
fi

python ktransformers/server/main.py --model_path "$MODEL_DIR" --gguf_path "$MODEL_DIR" --cache_lens "$CACHE_LENS" $TOOL_FLAGS

# To enable AMX optimization, set --optimize_config_path to the provided yaml
# Example:
# python ktransformers/server/main.py --model_path "$MODEL_DIR" --gguf_path "$MODEL_DIR" --cache_lens "$CACHE_LENS" --optimize_config_path ktransformers/optimize/optimize_rules/DeepSeek-V3-Chat-fp8-linear-ggml-experts-serve-amx.yaml
