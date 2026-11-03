# FAQ & Troubleshooting

## Deployment

**Q: What is the minimum hardware to run Kimi-K2 locally?**
A: The FP8 checkpoint with a 128K context requires at least 16 GPUs (e.g., H200 or H20) per serving instance, using TP or DP+EP. For single-GPU or CPU-oriented experiments, look at the KTransformers path in the [deployment guide](deploy_guidance.md) with quantized weights.

**Q: Which vLLM version do I need?**
A: vLLM v0.10.0rc1 or later — earlier releases do not recognize the `kimi_k2` model type and tool-call parser.

**Q: My framework does not recognize `kimi_k2`.**
A: As a temporary workaround, set `"model_type": "deepseek_v3"` in `config.json`. Kimi-K2 reuses the DeepSeekV3 architecture, but you will lose Kimi-specific optimizations and may need to parse tool calls manually (see the [tool calling guide](tool_call_guidance.md#manually-parsing-tool-calls)).

**Q: Tool calls are not parsed / come back as plain text.**
A: Make sure the server was started with the tool-call parser enabled:

- vLLM: `--enable-auto-tool-choice --tool-call-parser kimi_k2`
- SGLang: `--tool-call-parser kimi_k2`

## Usage

**Q: What temperature should I use?**
A: The recommended sampling temperature for Kimi-K2-Instruct is `0.6`. When calling the Anthropic-compatible API, note that it rescales temperature internally (`real = requested × 0.6`).

**Q: The model loops calling tools forever.**
A: Always bound your agent loop with a max-iteration guard, and feed tool errors back into the conversation so the model can recover. The examples in the [tool calling guide](tool_call_guidance.md) show both patterns.

**Q: Streaming responses never end / the client times out.**
A: Raise the client timeout (long agentic generations can exceed 10 minutes), and check the server logs for stalled requests. See the [streaming example](streaming_chat.md).

## Repository

**Q: How do I cite Kimi K2?**
A: See the BibTeX entry in the [README](../README.md#7-citation) — the full report is on [arXiv:2507.20534](https://arxiv.org/abs/2507.20534).

**Q: What does the Modified MIT License change?**
A: Everything MIT, plus: commercial products/services exceeding 100M MAU or $20M monthly revenue must prominently display "Kimi K2" in the UI. Read the [LICENSE](../LICENSE).
