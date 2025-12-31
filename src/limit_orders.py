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

# ---------- BINANCE CLIENT (FUTURES TESTNET / DEMO) ----------
client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_URL = "https://testnet.binancefuture.com"

# ---------- LIMIT ORDER ----------
def place_limit_order(symbol, side, quantity, price):
    notional = quantity * price

    # Binance Futures min notional check
    if notional < 100:
        print(f"ERROR: Order notional {notional:.2f} USDT is below minimum 100 USDT")
        return None

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        logging.info(f"Limit Order Placed: {order}")
        return order

    except Exception as e:
        logging.error(f"Limit Order Error: {e}")
        print("Error:", e)
        return None

# ---------- CLI ----------
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python src/limit_orders.py BTCUSDT SELL 0.002 90000")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    quantity = float(sys.argv[3])
    price = float(sys.argv[4])

    result = place_limit_order(symbol, side, quantity, price)

    if result:
        print("Limit Order Placed Successfully")
        print(result)
