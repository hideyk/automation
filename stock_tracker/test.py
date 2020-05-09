import yfinance as yf
import pandas
import numpy
import matplotlib
import bs4


msft = yf.Ticker("MSFT")
# print(msft.info)

hist = msft.history(period="max")
# print(hist)

# print(msft.actions)
# print(msft.financials)
# print(msft.quarterly_financials)
# print(msft.major_holders)
# print(msft.institutional_holders)
# print(msft.sustainability)            # Shows bunch of metrics for sustainability
# print(msft.recommendations)           # Shows recommendations from recognized firms

data = yf.download("goog", start="2017-01-01", end="2017-02-01")
print(type(data))
# print(data)
