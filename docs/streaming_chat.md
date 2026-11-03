# Streaming Chat Example

Kimi-K2 supports token-by-token streaming through the OpenAI-compatible chat endpoint. This page shows a minimal, production-shaped streaming client: it prints deltas as they arrive, handles interruptions, and reports usage when the server provides it.

```python
import json
from openai import OpenAI

endpoint = "http://localhost:8000/v1"   # change to your serving endpoint
api_key = "xxx"
model_name = "moonshotai/Kimi-K2-Instruct"
client = OpenAI(base_url=endpoint, api_key=api_key, timeout=600)

messages = [
    {"role": "system", "content": "You are Kimi, an AI assistant created by Moonshot AI."},
    {"role": "user", "content": "Give me a brief self-introduction."},
]

stream = client.chat.completions.create(
    model=model_name,
    messages=messages,
    temperature=0.6,
    max_tokens=256,
    stream=True,
    stream_options={"include_usage": True},  # request usage stats in the final chunk
)

full_text = ""
usage = None
for chunk in stream:
    if chunk.usage is not None:
        usage = chunk.usage  # last chunk only
    delta = chunk.choices[0].delta if chunk.choices else None
    if delta and delta.content:
        full_text += delta.content
        print(delta.content, end="", flush=True)

print()
if usage:
    print(f"tokens: prompt={usage.prompt_tokens} completion={usage.completion_tokens}")
```

## Notes

- Not every inference engine populates `usage` in streaming mode; guard against `None` as above.
- `timeout` should be generous: long agentic generations can take minutes. Prefer the async client (`AsyncOpenAI`) or per-request `timeout` for interactive apps.
- If you combine streaming with tool calling, collect the tool-call deltas first — see the [Tool Calling Guide](tool_call_guidance.md#tool-calling-in-streaming-mode).
