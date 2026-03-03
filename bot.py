import os
from dotenv import load_dotenv
import pybit
from pybit.unified_trading import HTTP

# .envファイルを読み込む
load_dotenv()

api_key = os.getenv("BYBIT_API_KEY")
api_secret = os.getenv("BYBIT_SECRET_KEY")

# Bybitに接続
session = HTTP(
    testnet=False,
    api_key=api_key,
    api_secret=api_secret,
)

# BTCの現在価格を取得
result = session.get_tickers(category="spot", symbol="BTCUSDT")
price = result["result"]["list"][0]["lastPrice"]
print(f"BTCの現在価格: ${price}")
