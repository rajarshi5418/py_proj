import talib as ta
import pymongo
from pandas import DataFrame
import pandas as pd
from matplotlib.pyplot import plot

client = pymongo.MongoClient()
mydb = client["NIFTY50"]
mycol = mydb["SBIN.NS"]

ohlcv = DataFrame(list(mycol.find({}, {'_id': 0})))

dt = ohlcv['Date']
op = ohlcv['open']
hg = ohlcv['high']
lo = ohlcv['low']
cl = ohlcv['Adj Close']
vol = ohlcv['volume']


def CDLDOJI(ohlc):
    res = ta.CDLDOJI(ohlc.open.values, ohlc.high.values,
                     ohlc.low.values, ohlc.close.values)
    return pd.DataFrame({'Date': dt, 'CDLDOJI': res}, index=ohlc.index)


doji = CDLDOJI(ohlcv)


# print(doji)

# count = 0
# for i in range(len(dj)):
#     d= dj['Date'][i]
#     k= dj['CDLDOJI'][i]
#     if k == 100:
#         # print(d,k)
#         count +=1
# print(count)

def CDLHAMMER(ohlc):
    res = ta.CDLHAMMER(ohlc.open.values, ohlc.high.values,
                       ohlc.low.values, ohlc.close.values)
    return pd.DataFrame({'Date': ohlc.Date.values, 'CDLHAMMER': res}, index=ohlc.index)


hammer = CDLHAMMER(ohlcv)
# print(hammer)


# for i in range(len(dj)):
#     d= dj['Date'][i]
#     k= dj['CDLHAMMER'][i]
#     if k == 100:
#         # print(d,k)
#         count +=1


# def PAT_REC():
#     count =0
#     dj = CDLHAMMER(ohlcv)
#     for i in range(len(dj)):
#         d = dj['Date'][i]
#         k = dj['CDLHAMMER'][i]
#         if k == 100:
#             print(d,"HAMMER", k)
#             count += 1
#     print(count)
#
# PAT_REC()


pat_list = [hammer, doji]


def PAT_REC():
    count = 0
    for dj in pat_list:
        print(dj)
        ind = dj.columns[1]

        for i in range(len(dj)):
            d = dj['Date'][i]
            k = dj[ind][i]
            if k == 100:
                print(d, ind, k)
                count += 1
        print(count)


PAT_REC()