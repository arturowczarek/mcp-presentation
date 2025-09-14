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