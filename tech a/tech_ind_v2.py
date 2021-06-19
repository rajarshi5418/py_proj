import talib as ta
import talib
import pymongo
from pandas import DataFrame
import pandas as pd

client = pymongo.MongoClient()
mydb = client["NIFTY50"]
mycol = mydb["SBIN.NS"]

ohlcv = DataFrame(list(mycol.find({}, {'_id':0})))

dt = ohlcv['Date']
op = ohlcv['open']
hg = ohlcv['high']
lo = ohlcv['low']
cl = ohlcv['Adj Close']
vol = ohlcv['volume']

for i in talib.get_function_groups():
    print(i)

vol_ind = []
for i in talib.get_function_groups()['Volatility Indicators']:
    tal = "ta."+i
    vol_ind.append(tal)
    # ind = talib.i()
print(vol_ind)


for i in vol_ind:
    def VOL_IND(ohlc):
            print(i)
            # res = eval(tal+"("+open+","+high+","+low+","+close+")")
            res = eval(i+"(hg,lo,cl)")
            return pd.DataFrame({'Date':dt,i: res}, index=ohlc.index)
    ind = VOL_IND(ohlcv)
    print(ind)

volm_ind = []
for i in talib.get_function_groups()['Volume Indicators']:
    tal = "ta."+i
    volm_ind.append(tal)
    # ind = talib.i()
print(volm_ind)


for i in volm_ind:
    def VOLM_IND(ohlc):
            print(i)
            # res = eval(tal+"("+open+","+high+","+low+","+close+")")
            if i == 'ta.AD' or i == 'ta.ADOSC':
                res = eval(i+"(hg,lo,cl,vol)")
            elif i == 'ta.OBV':
                res = eval(i+"(cl,vol)")
            return pd.DataFrame({'Date':dt,i: res}, index=ohlc.index)
    ind = VOLM_IND(ohlcv)
    print(ind)

