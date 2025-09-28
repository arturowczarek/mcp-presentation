import sys
import json
from basic.utils import get_current_price


def call_function(name, arguments):
    if name == "get_current_price":
        return get_current_price(**arguments)
    else:
        raise ValueError("Unknown function")


def tool_call(params):
    func_name = params["name"]
    func_args = params["arguments"]
    result = call_function(func_name, func_args)
    print(json.dumps({
        "result": json.dumps(result)
    }))


def list_tools():
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_price",
                "description": "Get the current price of a cryptocurrency trading pair",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pair": {
                            "type": "string",
                            "description": "The trading pair in format BASE/QUOTE, e.g. BTC/USD, ETH/USD"
                        }
                    },
                    "required": ["pair"],
                    "additionalProperties": False
                }
            }
        }
    ]
    print(json.dumps({
        "result": json.dumps(tools)
    }))


def main():
    """A simple server that listens for JSON-RPC-like commands on stdin and responds on stdout.
    Each command should be a JSON object with "method" and params".

    The server supports two methods:
    1. "tools/call" to call a tool function
    2. "tools/list" to list available tools

    Example command to call list available tools:
    {"method": "tools/list"}
    """
    for line in sys.stdin:
        try:
            command = json.loads(line)
            method = command["method"]
            if method == "tools/call":
                tool_call(command["params"])
            elif method == "tools/list":
                list_tools()
        except Exception as e:
            print(json.dumps({"error": str(e)}))


if __name__ == "__main__":
    main()
