import talib as ta
import pymongo
from pandas import DataFrame
import pandas as pd
from matplotlib.pyplot import plot

client = pymongo.MongoClient()
mydb = client["NIFTY50"]
mycol = mydb["SBIN.NS"]

ohlcv = DataFrame(list(mycol.find({}, {'_id':0})))

def CDLDOJI(ohlc):
    res = ta.CDLDOJI(ohlc.open.values, ohlc.high.values,
                        ohlc.low.values, ohlc.close.values)
    return pd.DataFrame({'Date':dt,'CDLDOJI': res}, index=ohlc.index)
doji = CDLDOJI(ohlcv)

def CDLHAMMER(ohlc):
    res = ta.CDLHAMMER(ohlc.open.values, ohlc.high.values,
                        ohlc.low.values, ohlc.close.values)
    return pd.DataFrame({'Date':ohlc.Date.values ,'CDLHAMMER': res}, index=ohlc.index)
hammer = CDLHAMMER(ohlcv)

pat_list =[hammer, doji]

def PAT_REC():
    for dj in pat_list:
        count = 0
        print(dj)
        ind = dj.columns[1]

        for i in range(len(dj)):
            d = dj['Date'][i]
            k = dj[ind][i]
            if k == 100:
                print(d,ind, k)
                count += 1
        print(count)

PAT_REC()