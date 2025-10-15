from datetime import datetime
import random

from fastmcp import FastMCP, Context
from fastmcp.server.elicitation import AcceptedElicitation
from mcp.types import TextContent
from pydantic import Field

mcp = FastMCP("finance")


@mcp.tool()
async def get_current_price(
        ctx: Context,
        currency: str = Field(description="The currency for which the price is returned", title="Currency")) -> dict:
    """Get the current price of a currency in your home currency"""
    result: AcceptedElicitation[str] = await ctx.elicit(
        message="What is your home currency? (e.g. USD, EUR, GBP)",
        response_type=str
    )
    base: str = result.data

    price = round(random.uniform(10000, 60000), 2) if base == "BTC" else round(random.uniform(100, 5000), 2)

    return {
        "pair": f"{currency}/{base}",
        "base": base,
        "quote": currency,
        "price": price,
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    mcp.run(transport='stdio')
