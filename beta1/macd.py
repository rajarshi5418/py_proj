import pandas_datareader.data as pdr

import datetime

nfty_50 = ["SBIN.NS"]

for i in nfty_50:
    print(i)
    ticker = i
    ohlcv = pdr.get_data_yahoo(ticker, datetime.date.today()-datetime.timedelta(900),datetime.date.today())
    print(ohlcv)

    def macd(DF, a, b, c):
        df = ohlcv.copy()

        df["MA_Fast"] = df["Adj Close"].ewm(span=a, min_periods=a).mean()
        df["MA_Slow"] = df["Adj Close"].ewm(span=b, min_periods=b).mean()
        df["MACD"] = df["MA_Fast"]-df["MA_Slow"]
        df["Signal"] = df["MACD"].ewm(span=c, min_periods=c).mean()
        df.dropna(inplace=True)
        # print(df.iloc[ : ,[5,8,9]])
        df = df.round(decimals=2)
        macd.dff = df.iloc[:, [5, 8, 9]]
        print(macd.dff)
        return DF

    def get_buy_signal():
        global sell_price
        global buy_price
        global profit

        sell_price = []
        buy_price = []

        profit = []


        macd(ohlcv, 12, 26, 9)
        dict1 = macd.dff

        data_dict = {}
        metadata_dict = {}
        trd = 1
        try:
            for i in range(len(dict1)):
                trade = trd
                Macd = dict1.iloc[i]['MACD']
                signal = dict1.iloc[i]['Signal']

                Macd1 = dict1.iloc[i+1]['MACD']
                signal1 = dict1.iloc[i+1]['Signal']

                if Macd < signal and Macd1 > signal1:
                    buy_price = []
                    print("BUY")
                    price_buy = dict1.iloc[i+1]['Adj Close']
                    date_buy = dict1.index[i + 1]
                    print(date_buy)
                    buy_price.append(dict1.iat[(i + 1), 0])
                    print(buy_price)
                    data_dict['buy_date'] = date_buy
                    data_dict['buy_price'] = price_buy


                if Macd > signal and Macd1 < signal1:
                    if len(buy_price)>0:
                        sell_price = []
                        print("SELL")
                        price_sell = dict1.iloc[i+1]['Adj Close']
                        dt = dict1.iloc[i+1]
                        date_sell = dict1.index[i+1]
                        print(date_sell)

                        sell_price.append(dict1.iat[(i + 1), 0])
                        data_dict['sell_date'] = date_sell
                        data_dict['sell_price'] = price_sell
                        data_dict['profit'] = round((sell_price[0]-buy_price[0]),2)
                        metadata_dict[trd]=data_dict
                        trd +=1

                    print(metadata_dict)

        except IndexError as error:
            print("just chill")
            # print(Macd,signal,Macd1,signal1)


    get_buy_signal()
