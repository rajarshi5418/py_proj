# =============================================================================
# Import OHLCV data and calculate RSI technical indicators
# Author : Mayank Rasu

# Please report bug/issues in the Q&A section
# =============================================================================

# Import necesary libraries
import pandas as pd
import pandas_datareader.data as pdr
import numpy as np
import datetime

# Download historical data for required stocks
ticker = "HDFCBANK.NS"
ohlcv = pdr.get_data_yahoo(ticker,datetime.date.today()-datetime.timedelta(900),datetime.date.today())


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
    RSI.dff = df.iloc[:, [5,-1]]
    # RSI.dff = df.copy()

    # print(RSI.dff)
    return df['RSI']

RSI(ohlcv,14)

# print(RSI.dff.iloc[1])

sell_price = []
buy_price = []
profit = []

def get_buy_signal():
    RSI(ohlcv,14)
    dict1 = RSI.dff
    print(dict1)

    try:
        for i in range(len(dict1)):
            rsi = dict1.iloc[i]['RSI']
            # print("rsi",i,rsi)
            rsi1 = dict1.iloc[i+1]['RSI']
            # print("rsi1",i+1,rsi1)

            if rsi > 30 and rsi1 < 30:
                if len(buy_price) - len(sell_price) == 0:
                    print("BUY")
                    print(dict1.iloc[i+1])
                    buy_price.append(dict1.iat[(i + 1), 0])
                    print(buy_price)


            if rsi < 70 and rsi1 > 70:
                if len(buy_price)-len(sell_price) == 1:
                    print("SELL")
                    print(dict1.iloc[i+1])
                    sell_price.append(dict1.iat[(i + 1), 0])
                    print(sell_price)

    except IndexError as error:
        print("just chill")
        # print(Macd,signal,Macd1,signal1)

        # print(data1)

get_buy_signal()

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