#!/usr/bin/env bash
# SGLang example (TP / DP+EP)
# Usage: MODEL_DIR=/path/to/K2 ./deploy_scripts/sglang_start.sh

MODEL_DIR=${MODEL_DIR:-/path/to/K2}
TOOL_FLAGS=""

if [ "${ENABLE_TOOL_CALLS:-0}" -eq 1 ]; then
  TOOL_FLAGS="--enable-auto-tool-choice --tool-call-parser kimi_k2"
fi

if [ ! -d "$MODEL_DIR" ]; then
  echo "Model directory not found: $MODEL_DIR"
  exit 1
fi

# Adjust sglang launcher flags for your cluster
python -m sglang.server --model_dir "$MODEL_DIR" $TOOL_FLAGS
