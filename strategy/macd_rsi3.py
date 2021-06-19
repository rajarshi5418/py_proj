from nifty_stock_list import *
import talib
import pandas_datareader.data as pdr
from talib import abstract
import pymongo
import datetime
from pandas import DataFrame
import pandas as pd
from colorama import Fore


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
        sell_price = []
        buy_price = []
        profit = []

        dict1 = data.copy()
        target = 0
        stoploss = 0

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
                    print(Fore.GREEN, "BUY", end="")
                    print(Fore.WHITE)
                    price_buy = dict1.iloc[i + 1]['Close']
                    date_buy = dict1.iloc[i + 1]['Date']
                    print(date_buy)
                    buy_price.append(dict1.iat[(i + 1), 1])
                    print(buy_price[-1])
                    data_dict['buy_date'] = date_buy
                    data_dict['buy_price'] = price_buy

                    target = buy_price[-1] + (buy_price[-1] * .05)
                    print(target)
                    stoploss = buy_price[-1] - (buy_price[-1] * .05)
                    print(stoploss)
                    i += 1

                if len(buy_price) > 0:
                    price = dict1.iloc[i]['Close']
                    if price >= target or price <= stoploss:
                        sell_price = []
                        print(Fore.RED, "SELL", end="")
                        print(Fore.WHITE)
                        price_sell = dict1.iloc[i]['Close']
                        date_sell = dict1.iloc[i + 1]['Date']
                        print(date_sell)

                        sell_price.append(dict1.iat[(i), 1])
                        print(sell_price)

                        data_dict['sell_date'] = date_sell
                        data_dict['sell_price'] = price_sell
                        data_dict['profit'] = round((sell_price[0] - buy_price[0]), 2)
                        print(data_dict['profit'])
                        buy_price = []
                        print("\n")
                        # print(data_dict)
                        mydb = client['macd_rsi2']
                        mycol = mydb[stk]
                        data_insert = data_dict.copy()
                        mycol.insert_one(data_insert)
                    #     metadata_dict[trd]=data_dict
                    #     trd +=1
                    #
                    # print(metadata_dict)

        except IndexError as error:
            print("just chill")
            # print(Macd,signal,Macd1,signal1)


    get_buy_signal()