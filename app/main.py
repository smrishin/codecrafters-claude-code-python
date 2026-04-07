import argparse
import os
import json
import copy

from typing import Optional

from openai import OpenAI
from app.tools.utils import TOOLS
from dotenv import load_dotenv

load_dotenv()

is_local = os.getenv("local", "false") == "true"


model = "z-ai/glm-4.5-air:free" if is_local else "anthropic/claude-haiku-4.5"

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")

def run_conversation(client: OpenAI, initial_prompt: str) -> None:
    '''Run conversion/agent loop with AI Model'''
    conversation_log = [{"role": "user", "content": initial_prompt}]
    tool_definitions = [t["definition"] for t in TOOLS.values()]

    while True:
        chat = client.chat.completions.create(
            model=model,
            messages=conversation_log,
            tools=tool_definitions
        )

        response = chat.choices[0].message

        message_dict = {
            'role': response.role,
            'content': response.content,
            'tool_calls': copy.deepcopy(response.tool_calls) if response.tool_calls else []
        }

        conversation_log.append(message_dict)

        if not message_dict.get("tool_calls", []):
            print(response.content)
            break

        for tool_call in response.tool_calls:
            tool_result = execute_tools(tool_call)
            conversation_log.append(tool_result)

def execute_tools(tool_call: dict) -> Optional(dict):
    """Execute a tool call and return the result of a message"""

    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)

    if function_name not in TOOLS:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Unknown function {function_name}"
        }

    result = TOOLS[function_name]["handler"](**function_args)
    
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()
    
    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    run_conversation(client, args.p)


if __name__ == "__main__":
    main()
