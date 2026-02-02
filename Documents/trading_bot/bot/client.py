import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise RuntimeError("API keys not found. Check .env file")

    return Client(api_key, api_secret, testnet=True)
