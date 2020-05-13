from yahooquery import Ticker
import yahooquery
import json
from currency_converter import CurrencyConverter

c = CurrencyConverter()

# aapl.history(period='', start='', end='', interval='')
# Period options = 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
# Interval options = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

# tickers = Ticker('D05.SI C6L.SI')
# hist = tickers.history(period='1d', start='', end='', interval='')
# print(hist)

# def get_stock1():
#     while True:
#         stk_search = input("Stock to search: ")
#         yflink = r"https://sg.finance.yahoo.com/lookup?s=" + stk_search
#         if stock:
#             break


def get_stock():
    while True:
        stk = input("Enter stock: ")
        stock_tick = Ticker(stk)
        stk_price = stock_tick.price
        try:
            stk_name = stk_price[stk]["longName"]
            stk_short = "[" + stk_price[stk]["shortName"] + "]"
            if stk_name:
                print("Selected stock:", stk_short, stk_name)
                confirm_stock = input("Confirm? (Y/N) ")
                if confirm_stock.lower() == "y":
                    return stk, stock_tick, stk_short
                else:
                    continue
            else:
                print("Please enter a valid stock symbol.")
        except:
            print("Please enter a valid stock symbol.")


def get_quantity():
    while True:
        qty = input("Quanity: ")
        try:
            quantity = int(qty)
            break
        except ValueError:
            print("This is not an integer.")
    return quantity


def get_price():
    while True:
        prc = input("Price: ")
        try:
            price = float(prc)
            break
        except ValueError:
            print("This is not a float value.")
    return price


def add_stock():
    stock_count = get_quantity()
    stock_price = get_price()

# {
#     "C6L.SI": {
#         "currency": "SGD",
#         "currencySymbol": "$",
#         "exchange": "SES",
#         "exchangeDataDelayedBy": 0,
#         "exchangeName": "SES",
#         "fromCurrency": null,
#         "lastMarket": null,
#         "longName": "Singapore Airlines Limited",
#         "marketCap": 7417884672,
#         "marketState": "CLOSED",
#         "maxAge": 1,
#         "priceHint": 4,
#         "quoteType": "EQUITY",
#         "regularMarketChange": 0.009999752,
#         "regularMarketChangePercent": 0.0022726709,
#         "regularMarketDayHigh": 4.6,
#         "regularMarketDayLow": 4.22,
#         "regularMarketOpen": 4.55,
#         "regularMarketPreviousClose": 4.4,
#         "regularMarketPrice": 4.41,
#         "regularMarketSource": "DELAYED",
#         "regularMarketTime": "2020-05-08 17:15:27",
#         "regularMarketVolume": 27158100,
#         "shortName": "SIA",
#         "symbol": "C6L.SI",
#         "toCurrency": null,
#         "underlyingSymbol": null
#     }
# }


stk_in, stk_tkr, stk_acr = get_stock()
stk_qty = get_quantity()
stk_price = get_price()


stk_info = stk_tkr.price
currency, cur_price = stk_info[stk_in]["currency"], stk_info[stk_in]["regularMarketPrice"]
act_price = c.convert(cur_price, currency, "SGD")
parsed = json.dumps(stk_info, sort_keys=True, indent=4)
contract_value = stk_qty * stk_price

print("You bought", stk_qty, "shares of", stk_acr, "for $" + stk_price, "per share.")


poems_cashmgmt_fee = 0.28 * 0.01
poems_cashplus_fee = 0.08 * 0.01
poems_clearing_fee = 0.0325 * 0.01
sgx_trading_fee = 0.0075 * 0.01
sgx_settlement_fee = 0.35