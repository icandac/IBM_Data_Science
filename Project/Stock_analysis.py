from typing_extensions import runtime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# plt.ion()

apple = yf.Ticker("AAPL")

apple_info=apple.info
# apple_info

apple_share_price_data = apple.history(period="max")
# apple_share_price_data.head()
# apple_share_price_data["Volume"][0]

print(apple_share_price_data)

apple_share_price_data.reset_index(inplace=True)
# apple_share_price_data.plot(x="Date", y="Open")

plt.plot(apple_share_price_data["Date"], apple_share_price_data["Open"])

print(apple.dividends)

apple.dividends.plot()

# plt.show()