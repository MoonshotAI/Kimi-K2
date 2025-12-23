Deployment scripts and checklist for Kimi-K2

This folder contains example start scripts and a checklist to activate Kimi-K2 on common inference backends.

Files:
- `ktransformers_start.sh` — KTransformers server example
- `ktransformers_start.ps1` — PowerShell wrapper for KTransformers
- `vllm_start.sh` — vLLM single-node / TP example
- `sglang_start.sh` — SGLang example (TP / DP+EP)
- `trtllm_start.sh` — TensorRT-LLM mpirun example

Quick checklist before running any script:
1. Place model weights in the desired path (`MODEL_PATH` / `MODEL_DIR`).
2. Ensure the target runtime is installed (vLLM, sglang, ktransformers, TensorRT-LLM).
3. Install dependencies (CUDA, drivers, mpirun/ssh for multi-node).
4. For tool calling enablement set `ENABLE_TOOL_CALLS=1` or pass the equivalent flags; scripts accept `ENABLE_TOOL_CALLS` to add `--enable-auto-tool-choice --tool-call-parser kimi_k2`.
5. Adjust parallelism parameters to fit your GPU count and topology.

How to use (examples):

Linux / WSL / bash:

```bash
export MODEL_DIR=/models/kimi-k2
export ENABLE_TOOL_CALLS=1
export KIMI_API_KEY=your_key_here   # DO NOT COMMIT or paste keys
./deploy_scripts/ktransformers_start.sh
```

PowerShell (Windows):

```powershell
$env:MODEL_DIR = 'C:\models\kimi-k2'
$env:ENABLE_TOOL_CALLS = '1'
$env:KIMI_API_KEY = 'your_key_here'  # set in session only
.\deploy_scripts\ktransformers_start.ps1 -EnableToolCalls
```

Notes:
- The scripts assume the runtime entrypoint exists (e.g., `ktransformers/server/main.py`). If your local checkout places entrypoints elsewhere, update paths accordingly.
- Always keep API keys out of committed files. Use environment variables, secrets managers, or OS keyrings.
- If you want, provide infra details (GPU type/count, single vs multi-node, model path) and I will finalize these scripts with exact parameters and a run-ready checklist.
