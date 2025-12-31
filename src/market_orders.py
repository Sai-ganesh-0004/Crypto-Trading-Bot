import sys
import logging
import os
from binance import Client
from dotenv import load_dotenv

# ---------- LOAD ENV ----------
load_dotenv()


API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    print("ERROR: API keys not found. Check your .env file.")
    sys.exit(1)

# ---------- LOGGING ----------
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------- BINANCE CLIENT (FUTURES TESTNET) ----------
client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_URL = "https://testnet.binancefuture.com"

# ---------- MARKET ORDER ----------
def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"Market Order Placed: {order}")
        return order
    except Exception as e:
        logging.error(f"Market Order Error: {e}")
        print("Error:", e)
        return None

# ---------- CLI ----------
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python src/market_orders.py BTCUSDT BUY 0.001")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    quantity = float(sys.argv[3])

    result = place_market_order(symbol, side, quantity)

    if result:
        print("Market Order Successful")
        print(result)
