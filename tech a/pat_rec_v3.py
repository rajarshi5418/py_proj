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

pat_rec = []
cnt = 0
for i in talib.get_function_groups()['Pattern Recognition']:
    tal = "ta."+i
    pat_rec.append(tal)
    # ind = talib.i()
    cnt +=1
print(pat_rec)
print(cnt)

# ta.CDL2CROWS()

count = 0
for i in pat_rec:
    def VOL_IND(ohlc):
            # print(i)
            # res = eval(tal+"("+open+","+high+","+low+","+close+")")
            res = eval(i+"(op,hg,lo,cl)")
            return pd.DataFrame({'Date':dt,i: res}, index=ohlc.index)
    count += 1
    ind = VOL_IND(ohlcv)

    intp = ind.iloc[-1][i]
    # print(intp)
    if intp != 0:
        print(i,intp)


print(count)



