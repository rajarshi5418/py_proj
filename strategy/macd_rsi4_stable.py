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
        global buy_price
        global sell_price
        global profit

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
                    if len(buy_price) - len(sell_price) == 0:
                        print("BUY")

                        price_buy = dict1.iloc[i + 1]['Close']
                        date_buy = dict1.iloc[i + 1]['Date']
                        buy_price.append(price_buy)
                        print(date_buy,price_buy)



                if Macd > signal and Macd1 < signal1 and rsi>70:
                    if len(buy_price) - len(sell_price) == 1:
                        print("SELL")

                        price_sell = dict1.iloc[i + 1]['Close']
                        date_sell = dict1.iloc[i + 1]['Date']
                        sell_price.append(price_sell)
                        print(date_sell, price_sell)

                        data_dict['buy_date'] = date_buy
                        data_dict['buy_price'] = price_buy
                        data_dict['sell_date'] = date_sell
                        data_dict['sell_price'] = price_sell
                        data_dict['profit'] = round((sell_price[-1] - buy_price[-1]), 2)
                        print(data_dict)


                        mydb = client['macd_rsi_stable']
                        mycol = mydb[stk]
                        data_insert = data_dict.copy()
                        mycol.insert_one(data_insert)



        except IndexError as error:
            print("just chill")
            # print(Macd,signal,Macd1,signal1)



    get_buy_signal()

    def tradebook():
        loss = 0
        profitt = 0

        try:

            for i in range(len(buy_price)):
                # print(sell_price[i],"-",buy_price[i])
                pft = int(sell_price[i]-buy_price[i])
                if pft < 0:
                    loss += 1
                else:
                    profitt += 1
                profit.append(pft)

        except IndexError as error:
            print("just chill")
        print(len(buy_price))
        print(len(sell_price))

        print("loss trades", loss)
        print("profit trades", profitt)

        total = 0
        for i in range(len(profit)):
            total = total + profit[i]
            print("trade", i,"\t", profit[i], end="\t")
            print(total)

    tradebook()