import os

import pandas as pd
import random
from datetime import datetime


def dict_to_table(dict: dict) -> pd.DataFrame:
    return pd.DataFrame(list(dict.items()), columns=["Key", "Value"])


def get_current_price(pair: str) -> dict:
    print(f"Fetching current price for {pair}...")
    base, quote = pair.split("/")

    price = round(random.uniform(10000, 60000), 2) if base == "BTC" else round(random.uniform(100, 5000), 2)

    return {
        "pair": pair,
        "base": base,
        "quote": quote,
        "price": price,
        "timestamp": datetime.now().isoformat()
    }


def print_mcp_config(server_script: str, name: str):
    import json
    import os
    import shutil

    pwd = os.getcwd()
    which_uv = shutil.which("uv")

    print(json.dumps({
        "mcpServers": {
            name: {
                "command": which_uv,
                "args": [
                    "--directory",
                    pwd,
                    "run",
                    server_script
                ]
            }
        }
    }, indent=4))


pwd = os.getcwd()


def print_mcp_config_npx(name: str, package: str, args: list):
    import json
    print(json.dumps({
        "mcpServers": {
            name: {
                "command": "npx",
                "args": [
                            "-y",
                            package
                        ] + args
            }
        }
    }, indent=4))
