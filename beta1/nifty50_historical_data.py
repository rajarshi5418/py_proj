# storing nifty50 historical data in mongodb

import pandas as pd
import pandas_datareader.data as pdr
import numpy as np
import datetime
import pymongo
from nifty_stock_list import *
from pymongo import MongoClient

client = pymongo.MongoClient()

mydb = client['NIFTY50']


nfty_50 = nifty()

for i in nifty_50:
    print(i)
    mycol = mydb[i]
    ticker = i
    ohlcv = pdr.get_data_yahoo(ticker, datetime.date.today()-datetime.timedelta(3650),datetime.date.today())
    ohlcv = round(ohlcv,2)
    print(ohlcv)


    # for i in range(len(ohlcv)):
    #     dict1 = {}
    #     date1 = ohlcv.index[i]
    #     print(date1)
    #     dict1['Date'] = date1
    #     print(ohlcv.iloc[i])
    #
    #
    #     dict1['high'] = ohlcv.iloc[i]['High']
    #     dict1['low'] = ohlcv.iloc[i]['Low']
    #     dict1['open'] = ohlcv.iloc[i]['Open']
    #     dict1['close'] = ohlcv.iloc[i]['Close']
    #     dict1['Adj Close'] = ohlcv.iloc[i]['Adj Close']
    #     dict1['volume'] = ohlcv.iloc[i]['Volume']
    #
    #     print(dict1 )
    #     # mycol.insert_one(dict1)