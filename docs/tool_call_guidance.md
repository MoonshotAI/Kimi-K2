## Tool Calling
To enable the tool calling feature, you may need to set certain tool calling parser options when starting the service. See [deploy_guidance](./deploy_guidance.md) for details.
In Kimi-K2, a tool calling process includes:
- Passing function descriptions to Kimi-K2
- Kimi-K2 decides to make a function call and returns the necessary information for the function call to the user
- The user performs the function call, collects the call results, and passes the function call results to Kimi-K2
- Kimi-K2 continues to generate content based on the function call results until the model believes it has obtained sufficient information to respond to the user

### Preparing Tools
Suppose we have a function `get_weather` that can query the weather conditions in real-time. 
This function accepts a city name as a parameter and returns the weather conditions. We need to prepare a structured description for it so that Kimi-K2 can understand its functionality.

```python
def get_weather(city):
    return {"weather": "Sunny"}

# Collect the tool descriptions in tools
tools = [{
    "type": "function",
    "function": {        
        "name": "get_weather", 
        "description": "Get weather information. Call this tool when the user needs to get weather information", 
         "parameters": {
              "type": "object",
              "required": ["city"], 
              "properties": { 
                  "city": { 
                      "type": "string", 
                      "description": "City name", 
                }
            }
        }
    }
}]

# Tool name->object mapping for easy calling later
tool_map = {
    "get_weather": get_weather
}
```
### Chat with tools
We use `openai.OpenAI` to send messages to Kimi-K2 along with tool descriptions. Kimi-K2 will autonomously decide whether to use and how to use the provided tools. 
If Kimi-K2 believes a tool call is needed, it will return a result with `finish_reason='tool_calls'`. At this point, the returned result includes the tool call information. 
After calling tools with the provided information, we then need to append the tool call results to the chat history and continue calling Kimi-K2. 
Kimi-K2 may need to call tools multiple times until the model believes the current results can answer the user's question. We should check `finish_reason` until it is not `tool_calls`.

The results obtained by the user after calling the tools should be added to `messages` with `role='tool'`.

```python
import json
from openai import OpenAI
model_name='moonshotai/Kimi-K2-Instruct'
client = OpenAI(base_url=endpoint, 
                        api_key='xxx')

messages = [
{"role": "user", "content": "What's the weather like in Beijing today? Let's check using the tool."}
]
finish_reason = None
while finish_reason is None or finish_reason == "tool_calls":
    completion = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.3,
        tools=tools, 
        tool_choice="auto",
    )
    choice = completion.choices[0]
    finish_reason = choice.finish_reason
    # Note: The finish_reason when tool calls end may vary across different engines, so this condition check needs to be adjusted accordingly
    if finish_reason == "tool_calls": 
        messages.append(choice.message)
        for tool_call in choice.message.tool_calls: 
            tool_call_name = tool_call.function.name
            tool_call_arguments = json.loads(tool_call.function.arguments) 
            tool_function = tool_map[tool_call_name] 
            tool_result = tool_function(**tool_call_arguments)
            print("tool_result", tool_result)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call_name,
                "content": json.dumps(tool_result), 
            })
print('-' * 100)
print(choice.message.content)
```
### Tool Calling in Streaming Mode
Tool calling can also be used in streaming mode. In this case, we need to collect the tool call information returned in the stream until we have a complete tool call. Please refer to the code below:

```python
messages = [
    {"role": "user", "content": "What's the weather like in Beijing today? Let's check using the tool."}
]
finish_reason = None
msg = ''
while finish_reason is None or finish_reason == "tool_calls":
    completion = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.3,
        tools=tools,
        tool_choice="auto",
        stream=True 
    )
    tool_calls = []
    for chunk in completion:
        delta = chunk.choices[0].delta
        if delta.content:
            msg += delta.content
        if delta.tool_calls:
            for tool_call_chunk in delta.tool_calls:
                if tool_call_chunk.index is not None:
                    # Extend the tool_calls list
                    while len(tool_calls) <= tool_call_chunk.index:
                        tool_calls.append({
                            "id": "",
                            "type": "function",
                            "function": {
                                "name": "",
                                "arguments": ""
                            }
                        })

                    tc = tool_calls[tool_call_chunk.index]

                    if tool_call_chunk.id:
                        tc["id"] += tool_call_chunk.id
                    if tool_call_chunk.function.name:
                        tc["function"]["name"] += tool_call_chunk.function.name
                    if tool_call_chunk.function.arguments:
                        tc["function"]["arguments"] += tool_call_chunk.function.arguments

        finish_reason = chunk.choices[0].finish_reason
    # Note: The finish_reason when tool calls end may vary across different engines, so this condition check needs to be adjusted accordingly
    if finish_reason == "tool_calls":
        for tool_call in tool_calls:
            tool_call_name = tool_call['function']['name']
            tool_call_arguments = json.loads(tool_call['function']['arguments'])
            tool_function = tool_map[tool_call_name] 
            tool_result = tool_function(tool_call_arguments)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call['id'],
                "name": tool_call_name,
                "content": json.dumps(tool_result),
            })
        # The text generated by the tool call is not the final version, reset msg
        msg = ''

    print(msg)
```
### Manually Parsing Tool Calls
The tool call requests generated by Kimi-K2 can also be parsed manually, which is especially useful when the service you are using does not provide a tool-call parser. 
The tool call requests generated by Kimi-K2 are wrapped by `<|tool_calls_section_begin|>` and `<|tool_calls_section_end|>`, 
with each tool call wrapped by `<|tool_call_begin|>` and `<|tool_call_end|>`. The tool ID and arguments are separated by `<|tool_call_argument_begin|>`. 
The format of the tool ID is `functions.{func_name}:{idx}`, from which we can parse the function name.

Based on the above rules, we can directly post a request to the completions interface and manually parse tool calls.

```python
import requests
from transformers import AutoTokenizer
messages = [
    {"role": "user", "content": "What's the weather like in Beijing today? Let's check using the tool."}
]
msg = ''
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
while True:
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        tools=tools,
        add_generation_prompt=True,
    )
    payload = {
        "model": model_name,
        "prompt": text,
        "max_tokens": 512
    }
    response = requests.post(
        f"{endpoint}/completions",
        headers={"Content-Type": "application/json"},
        json=payload,
        stream=False,
    )
    raw_out = response.json()

    raw_output = raw_out["choices"][0]["text"]
    tool_calls = extract_tool_call_info(raw_output)
    if len(tool_calls) == 0:
        # No tool calls
        msg = raw_output
        break
    else:
        for tool_call in tool_calls:
            tool_call_name = tool_call['function']['name']
            tool_call_arguments = json.loads(tool_call['function']['arguments'])
            tool_function = tool_map[tool_call_name]
            tool_result = tool_function(**tool_call_arguments)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call['id'],
                "name": tool_call_name,
                "content": json.dumps(tool_result), 
            })
print('-' * 100)          
print(msg)
```
Here, `extract_tool_call_info` parses the model output and returns the model call information. A simple implementation would be:
```python
def extract_tool_call_info(tool_call_rsp: str):
    if '<|tool_calls_section_begin|>' not in tool_call_rsp:
        # No tool calls
        return []
    import re
    pattern = r"<\|tool_calls_section_begin\|>(.*?)<\|tool_calls_section_end\|>"
    
    tool_calls_sections = re.findall(pattern, tool_call_rsp, re.DOTALL)
    
    # Extract multiple tool calls
    func_call_pattern = r"<\|tool_call_begin\|>\s*(?P<tool_call_id>[\w\.]+:\d+)\s*<\|tool_call_argument_begin\|>\s*(?P<function_arguments>.*?)\s*<\|tool_call_end\|>"
    tool_calls = []
    for match in re.findall(func_call_pattern, tool_calls_sections[0], re.DOTALL):
        function_id, function_args = match
        # function_id: functions.get_weather:0
        function_name = function_id.split('.')[1].split(':')[0]
        tool_calls.append(
            {
                "id": function_id,
                "type": "function",
                "function": {
                    "name": function_name,
                    "arguments": function_args
                }
            }
        )  
    return tool_calls
```
