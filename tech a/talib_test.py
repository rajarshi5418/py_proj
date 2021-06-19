from talib import abstract
import pymongo
from pandas import DataFrame
client = pymongo.MongoClient()
mydb = client["NIFTY50"]
mycol = mydb['SBIN.NS']

ohlcv = DataFrame(list(mycol.find({},{'_id':0})))
print(ohlcv)

rsi = abstract.RSI(ohlcv)
print(rsi)

crow = abstract.CDL2CROWS(ohlcv)
print(crow)

doji = abstract.CDLDOJI(ohlcv)
print(doji)