import yfinance as yf
import pandas
import numpy
import matplotlib
import bs4
import json
import yahoofinancials
from yahooquery import Ticker
from datetime import datetime as dt

now = dt.now()
print(now)


stock_tick = Ticker("Z74.SI")
# stock_tick = Ticker("SJDJSDKSJDA")
test = stock_tick.price
parsed = json.dumps(test, sort_keys=True, indent=4)
print(parsed)
test2 = test["Z74.SI"]["longName"]
print(test2)
print(type(test2))

# data = yf.download("C6L.SI", start="2017-01-01", end="2020-05-08")
# print(type(data))
# print(data)


# parsed = json.dumps(microsoft, sort_keys=True, indent=4)
# print(parsed)

# tsla_df = yf.download('tsla',
#                       start='2020-05-01',
#                       end='2020-05-03',
#                       progress=False,
#                       interval='30m')
#
# print(tsla_df)
# print(tsla_df.dtypes)

# yahoo_financials = yahoofinancials.YahooFinancials('TSLA')
# data = yahoo_financials.get_historical_price_data(start_date='2020-05-01',
#                                                   end_date='2020-06-01',
#                                                   time_interval='daily')
# parsed = json.dumps(data, sort_keys=True, indent=4)
# print(parsed)



# tker = Ticker('D05.SI')
# hist = tker.history(period='1d', interval='15m')
# print(hist)


# aapl.history(period='', start='', end='', interval='')
# Period options = 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
# Interval options = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo