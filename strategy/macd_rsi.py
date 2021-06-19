from nifty_stock_list import *
import talib
import pandas_datareader.data as pdr
from talib import abstract
import pymongo
import datetime
from pandas import DataFrame
import pandas as pd


nfty_50 = nifty()

client = pymongo.MongoClient()
mydb = client['NIFTY50']

for stk in nfty_50:
    print(stk)
    mycol = mydb[stk]
    ohlcv = DataFrame(list(mycol.find({}, {'_id': 0})))
    # print(ohlcv)

    cl = ohlcv['Adj Close']
    dt = ohlcv['Date']
    macd = abstract.MACD(ohlcv)
    rsi = abstract.RSI(ohlcv)
    macd['Date'] = dt
    macd['Close'] = cl
    macd['rsi'] = rsi
    data = pd.DataFrame({'Date':dt, 'Close':cl, 'macd':macd['macd'], 'signal':macd['macdsignal'],'rsi':rsi}, index=ohlcv.index)
    # macd = pd.DataFrame({'Date':dt, 'Close':cl}, index=ohlcv.index)
    print(stk)
    print(data)




    def get_buy_signal():
        global sell_price
        global buy_price
        global profit

        sell_price = []
        buy_price = []
        profit = []

        dict1 = data
        data_dict = {}
        metadata_dict = {}
        trd = 1
        try:
            for i in range(len(dict1)):
                trade = trd
                Macd = dict1.iloc[i]['macd']
                signal = dict1.iloc[i]['signal']
                rsi = dict1.iloc[i]['rsi']

                Macd1 = dict1.iloc[i + 1]['macd']
                signal1 = dict1.iloc[i + 1]['signal']

                if Macd < signal and Macd1 > signal1 and rsi<30:
                    buy_price = []
                    print("BUY")
                    price_buy = dict1.iloc[i + 1]['Close']
                    date_buy = dict1.iloc[i + 1]['Date']
                    print(date_buy)
                    buy_price.append(dict1.iat[(i + 1), 1])
                    print(buy_price)
                    data_dict['buy_date'] = date_buy
                    data_dict['buy_price'] = price_buy

                if Macd > signal and Macd1 < signal1 and rsi>70:
                    if len(buy_price) > 0:
                        sell_price = []
                        print("SELL")
                        price_sell = dict1.iloc[i + 1]['Close']
                        dt = dict1.iloc[i + 1]
                        date_sell = dict1.iloc[i + 1]['Date']
                        print(date_sell)

                        sell_price.append(dict1.iat[(i + 1), 1])
                        print(sell_price)
                        data_dict['sell_date'] = date_sell
                        data_dict['sell_price'] = price_sell
                        data_dict['profit'] = round((sell_price[0] - buy_price[0]), 2)
                        print(data_dict)
                        # try:
                        #     mycol.insert_one(data_dict)
                        #
                        # except pymongo.errors.DuplicateKeyError:
                        #     pass
                        data_dict1 = data_dict.copy()
                        mydb = client["MACD_RSI"]
                        mycol = mydb[stk]
                        mycol.insert_one(data_dict1)
                        metadata_dict[trd] = data_dict
                        trd += 1

                    # print(metadata_dict)

        except IndexError as error:

            print("just chill")
    get_buy_signal()