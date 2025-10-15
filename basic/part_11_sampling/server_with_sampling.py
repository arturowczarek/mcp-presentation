from datetime import datetime
import random

from fastmcp import FastMCP, Context
from mcp.types import TextContent
from pydantic import Field

mcp = FastMCP("finance")


@mcp.tool()
async def get_current_price(
        ctx: Context,
        pair_not_normalized: str = Field(description="The trading pair.", title="Currency pair")) -> dict:
    """Get the current price of a trading pair"""
    normalized_pair: TextContent = await ctx.sample(
        f"""The user wants to get the current price of a trading pair. It has passed the pair as '{pair_not_normalized}'. Turn it into the format BASE/QUOTE, e.g. BTC/USD, ETH/USD. If the input is invalid, return 'BTC/USD'. Return only the converted currency pair. Nothing else""", )
    base, quote = normalized_pair.text.split("/")

    price = round(random.uniform(10000, 60000), 2) if base == "BTC" else round(random.uniform(100, 5000), 2)

    return {
        "pair": normalized_pair.text,
        "base": base,
        "quote": quote,
        "price": price,
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    mcp.run(transport='stdio')
