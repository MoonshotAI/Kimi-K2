#!/usr/bin/env bash
# TensorRT-LLM mpirun example
# Usage: MODEL_DIR=/path/to/K2 mpirun -n <worldsize> ./deploy_scripts/trtllm_start.sh

MODEL_DIR=${MODEL_DIR:-/path/to/K2}
MPI_PROCS=${MPI_PROCS:-4}
TOOL_FLAGS=""

if [ "${ENABLE_TOOL_CALLS:-0}" -eq 1 ]; then
  TOOL_FLAGS="--enable-auto-tool-choice --tool-call-parser kimi_k2"
fi

if [ ! -d "$MODEL_DIR" ]; then
  echo "Model directory not found: $MODEL_DIR"
  exit 1
fi

mpirun -n ${MPI_PROCS} python trtllm/serve.py --model_dir "$MODEL_DIR" $TOOL_FLAGS
