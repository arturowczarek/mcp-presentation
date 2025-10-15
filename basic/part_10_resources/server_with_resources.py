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

@mcp.prompt()
def price_prompt(pair: str = Field(description="A trading pair BASE/QUOTE")) -> str:
    """A prompt to ask for the current price of a trading pair"""
    return f"What is the current price of {pair}?"

@mcp.resource("forex://trading_pairs")
def trading_pairs() -> list[str]:
    """A resource listing available trading pairs"""
    return ["BTC/USD", "ETH/USD", "LTC/USD", "XRP/USD"]


@mcp.resource("forex://historical_prices/{base}/{quote}?days={days}")
def historical_prices(
        base: str = Field(description="Base currency of the trading pair"),
        quote: str = Field(description="Quote currency of the trading pair"),
        days: int = Field(default=7, description="Number of days to fetch history for")
) -> list[dict]:
    """A resource returning historical prices for a trading pair"""
    return [
        {
            "date": (datetime.now().date()).isoformat(),
            "pair": f"{base}/{quote}",
            "price": round(random.uniform(10000, 60000), 2) if base == "BTC" else round(random.uniform(100, 5000), 2)
        }
        for _ in range(days)
    ]


if __name__ == "__main__":
    mcp.run(transport='stdio')