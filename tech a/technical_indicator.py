import talib as ta
import pymongo
from pandas import DataFrame
import pandas as pd
from matplotlib.pyplot import plot

client = pymongo.MongoClient()
mydb = client["NIFTY50"]
mycol = mydb["SBIN.NS"]

ohlcv = DataFrame(list(mycol.find({}, {'_id':0})))
print(ohlcv['Date'])

dt = ohlcv['Date']
op = ohlcv['open']
hg = ohlcv['high']
lo = ohlcv['low']
cl = ohlcv['Adj Close']
vol = ohlcv['volume']

print(vol)

vol_ind = []
for i in ta.get_function_groups()['Volatility Indicators']:
    vol_ind.append(i)
    print(vol_ind)



# for i in range(len(vol_ind)):
#     k = "ta."+vol_ind[i]
#     print(k)
#     ind = k(vol)
#     print(ind)

def CDLDOJI(ohlc):
    res = ta.CDLDOJI(ohlc.open.values, ohlc.high.values,
                        ohlc.low.values, ohlc.close.values)
    return pd.DataFrame({'Date':dt,'CDLDOJI': res}, index=ohlc.index)
dj = CDLDOJI(ohlcv)
print(dj)

count = 0
for i in range(len(dj)):
    d= dj['Date'][i]
    k= dj['CDLDOJI'][i]
    if k == 100:
        # print(d,k)
        count +=1
print(count)

"""
adx = ta.NATR(hg,lo,cl,timeperiod = 14)
print(adx)

adx = ta.ADX(hg,lo,cl,timeperiod = 14)
print(adx)

rsi = ta.RSI(cl,timeperiod = 14)
print(rsi)

atr = ta.ATR(hg,lo,cl,timeperiod = 14)
print(type(adx))


# doji = ta.stream_CDLDOJI(op,hg,lo,cl)
# print(doji)
"""

def ATR(ohlc):
    atr = ta.ATR(ohlc.high.values,
                        ohlc.low.values, ohlc.close.values)
    return pd.DataFrame({'Date':dt,'ATR': atr}, index=ohlc.index)
atr = ATR(ohlcv)
print(atr)

def RSI(ohlc):
    df = ta.RSI(ohlc.close.values)
    return pd.DataFrame({'Date':dt,'ATR': df}, index=ohlc.index)
rsi = RSI(ohlcv)
print(rsi)