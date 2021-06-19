
import pandas_datareader.data as pdr
import numpy as np
import datetime
import pymongo
from nifty_stock_list import *

client = pymongo.MongoClient()
mydb = client['RSI']

nfty_50 = nifty()

for i in nifty_50:
    print(i)
    mycol = mydb[i]
    ticker = i
    ohlcv = pdr.get_data_yahoo(ticker, datetime.date.today()-datetime.timedelta(960),datetime.date.today())

    def RSI(DF,n):
        "function to calculate RSI"
        df = DF.copy()
        df['delta']=df['Adj Close'] - df['Adj Close'].shift(1)
        df['gain']=np.where(df['delta']>=0,df['delta'],0)
        df['loss']=np.where(df['delta']<0,abs(df['delta']),0)
        # print(df['delta'])
        avg_gain = []
        avg_loss = []
        gain = df['gain'].tolist()
        # print(gain)
        loss = df['loss'].tolist()
        for i in range(len(df)):
            if i < n:
                avg_gain.append(np.NaN)
                avg_loss.append(np.NaN)
            elif i == n:
                avg_gain.append(df['gain'].rolling(n).mean().tolist()[n])
                avg_loss.append(df['loss'].rolling(n).mean().tolist()[n])
            elif i > n:
                avg_gain.append(((n-1)*avg_gain[i-1] + gain[i])/n)
                avg_loss.append(((n-1)*avg_loss[i-1] + loss[i])/n)
        df['avg_gain']=np.array(avg_gain)
        df['avg_loss']=np.array(avg_loss)
        df['RS'] = df['avg_gain']/df['avg_loss']
        df['RSI'] = 100 - (100/(1+df['RS']))
        print(df)
        # RSI.dff = df.iloc[:, [5,-1]]
        RSI.dff = df.copy()

        # print(RSI.dff)
        return df['RSI']

    RSI(ohlcv,14)

    def get_buy_signal():

        sell_price = []
        buy_price = []

        RSI(ohlcv,14)
        dict1 = RSI.dff
        print(dict1)

        data_dict = {}
        metadata_dict = {}
        trd = 1

        try:
            for i in range(len(dict1)):
                trade = trd
                rsi = dict1.iloc[i]['RSI']
                # print("rsi",i,rsi)
                rsi1 = dict1.iloc[i+1]['RSI']
                # print("rsi1",i+1,rsi1)

                if rsi > 30 and rsi1 < 30:

                    if len(buy_price) - len(sell_price) == 0:
                        print("BUY")
                        price_buy = dict1.iloc[i + 1]['Adj Close']
                        date_buy = dict1.index[i + 1]
                        print(date_buy)
                        print(price_buy)

                        buy_price.append(dict1.iat[(i + 1), 0])
                        data_dict['buy_date'] = date_buy
                        data_dict['buy_price'] = price_buy


                if rsi < 70 and rsi1 > 70:
                    if len(buy_price)-len(sell_price)==1:
                        print("SELL")
                        price_sell = dict1.iloc[i + 1]['Adj Close']
                        date_sell = dict1.index[i + 1]
                        print(date_sell)

                        sell_price.append(dict1.iat[(i + 1), 0])
                        data_dict['sell_date'] = date_sell
                        data_dict['sell_price'] = price_sell

                        print(price_buy)
                        print(price_sell)
                        print(price_sell-price_buy)

                        data_dict['profit'] = (price_sell - price_buy)
                        print(data_dict)
                        # data_insert = data_dict.copy()
                        # mycol.insert_one(data_insert)
                        # metadata_dict[trd] = data_dict
                        # trd += 1

                    # print(metadata_dict)

        except IndexError as error:
            print("just chill")
            # print(Macd,signal,Macd1,signal1)

            # print(data1)

    # get_buy_signal()

    def remove_duplicate():
        for x in mycol.find():
            count = 0
            y = x['buy_date']

            for xx in mycol.find():
                z=xx['buy_date']
                if y==z:
                    count+=1

                    if count>1:
                        myQuery ={'buy_date': xx['buy_date']}
                        mycol.delete_one(myQuery)

    remove_duplicate()
# print("")
# remove_duplicate()
#     for x in mycol.find():
#         print(x)
