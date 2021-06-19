import pandas_datareader.data as pdr
import datetime
from macd import *
from nifty_stock_list import *

nfty_50 = nifty()

print(nfty_50)


for i in nifty_50:
    print(i)
    ticker = i
    ohlcv = pdr.get_data_yahoo(ticker, datetime.date.today()-datetime.timedelta(960),datetime.date.today())
    print(ohlcv)
    macd(ohlcv, 12, 26, 9)
    get_buy_signal()



