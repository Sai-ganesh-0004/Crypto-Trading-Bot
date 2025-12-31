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

def place_oco_order(symbol, side, quantity, take_profit, stop_loss):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="TAKE_PROFIT_MARKET",
            stopPrice=take_profit,
            closePosition=True
        )

        stop = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP_MARKET",
            stopPrice=stop_loss,
            closePosition=True
        )

        logging.info(f"OCO Orders Placed: TP={order}, SL={stop}")
        print("OCO Orders Placed Successfully")
    except Exception as e:
        logging.error(f"OCO Error: {e}")
        print("Error:", e)
