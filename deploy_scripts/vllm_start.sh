#!/usr/bin/env bash
# vLLM single-node example
# Usage: MODEL_PATH=/models/kimi-k2 PORT=8000 ./deploy_scripts/vllm_start.sh

MODEL_PATH=${MODEL_PATH:-/models/kimi-k2}
PORT=${PORT:-8000}
NUM_GPU=${NUM_GPU:-1}
TOOL_FLAGS=""

if [ "${ENABLE_TOOL_CALLS:-0}" -eq 1 ]; then
  TOOL_FLAGS="--enable-auto-tool-choice --tool-call-parser kimi_k2"
fi

if [ ! -d "$MODEL_PATH" ]; then
  echo "Model path not found: $MODEL_PATH"
  exit 1
fi

# Example vLLM launch (adjust args to your setup)
python -m vllm.entrypoint \ 
  --model $MODEL_PATH \ 
  --port $PORT \ 
  --num-gpus $NUM_GPU $TOOL_FLAGS
