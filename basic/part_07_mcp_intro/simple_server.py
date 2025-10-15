from datetime import datetime
import random

from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("finance")

@mcp.tool()
def get_current_price(
        pair: str = Field(description="The trading pair in format BASE/QUOTE, e.g. BTC/USD, ETH/USD")) -> dict:
    """Get the current price of a trading pair"""
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



if __name__ == "__main__":
    mcp.run(transport='stdio')