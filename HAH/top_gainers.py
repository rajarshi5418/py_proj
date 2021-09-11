import pandas as pd
from nsepy import get_history
from datetime import date, timedelta
from nifty_stock_list import nifty_next_50,nifty_bank,\
    nifty_metal,nifty,nifty_equity_to_trade,nifty_midcap_100

dict_top_gainers = {}
list_top_gainers = []
for ticker in nifty_metal():
    try:

        print(ticker)
        count = 0
        # print(ticker)
        end_day = date.today()
        start_day = end_day - timedelta(4)

        #Fetch ticker data from nsepy
        df = get_history(symbol=ticker, start=start_day, end=end_day)

        #Data preparation for OHLC Candlesticks
        data=df[['Open', 'High', 'Low', 'Close', 'Volume']]
        # i = len(data)
        profit = round((data.iloc[-1]["Close"])-(data.iloc[1]["Close"]),2
                       )
        profit_per = round((profit/(data.iloc[-1]["Close"]))*100,2)
        # print(profit,profit_per)

        dict_top_gainers['stock']=ticker
        dict_top_gainers['gain/loss']=profit
        dict_top_gainers['gain_loss_per']=profit_per
        # print(dict_top_gainers)
        list_top_gainers.append(dict_top_gainers)
        # print(list_top_gainers)
        dict_top_gainers = {}
    except IndexError as error:
        print("just chill")

df2=pd.DataFrame.from_dict(list_top_gainers)
# print(df2)
# print(df2.sort_values(ascending=False))
# print(df2.loc[df2.gain_loss_per.idxmax()])
print(df2.sort_values(by='gain_loss_per', ascending=False).head(5))
print(df2.sort_values(by='gain_loss_per', ascending=True).head(5))


