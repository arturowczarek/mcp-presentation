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


def main():
    """A simple server that listens for JSON-RPC-like commands on stdin and responds on stdout.
    Each command should be a JSON object with "method" and params".

    Example command to call a tool:"
    {"method": "tools/call", "params": {"name": "get_current_price", "arguments": {"pair": "BTC/USD"}}}
    The server will respond with a JSON object containing the result
    Example response:
    {"result": "{\"pair\": \"BTC/USD\", \"base\": \"BTC\", \"quote\": \"USD\", \"price\": 45000.0, \"timestamp\": \"2023-10-01T12:00:00\"}"}
    (the result is a JSON string, not the object itself)
    """
    for line in sys.stdin:
        try:
            command = json.loads(line)
            method = command["method"]
            if method == "tools/call":
                tool_call(command["params"])
        except Exception as e:
            print(json.dumps({"error": str(e)}))


if __name__ == "__main__":
    main()
