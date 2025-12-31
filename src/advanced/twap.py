import time
import logging
from binance import Client

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_SECRET_KEY"

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"

def twap_order(symbol, side, total_qty, parts, delay):
    qty_per_order = total_qty / parts

    for i in range(parts):
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=qty_per_order
            )
            logging.info(f"TWAP Order {i+1}: {order}")
            print(f"Executed TWAP part {i+1}")
            time.sleep(delay)
        except Exception as e:
            logging.error(f"TWAP Error: {e}")
            break
