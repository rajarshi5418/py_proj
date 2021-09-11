from nsepy import get_history
from datetime import date, timedelta
from nifty_stock_list import nifty_next_50,nifty_bank,\
    nifty_metal,nifty,nifty_equity_to_trade,nifty_midcap_100

dict_uptrend = {}
list_uptrend = []
for ticker in nifty_bank():
    count = 0
    # print(ticker)
    end_day = date.today()
    start_day = end_day - timedelta(365)

    #Fetch ticker data from nsepy
    df = get_history(symbol=ticker, start=start_day, end=end_day)

    #Data preparation for OHLC Candlesticks
    data=df[['Open', 'High', 'Low', 'Close', 'Volume']]
    for i in range(1,len(data)):

        j=i+1
        # print(i)
        # print(j)
        # print(data.iloc[-i]["Close"])
        # print(data.iloc[-j]["Close"])
        if((data.iloc[-i]["Close"])>(data.iloc[-i-1]["Close"])):
            # print("uptrend")
            count=count+1

        else:
            # print("no of consecutive days of uptrend", count)
            # print('no trend')
            if count > 3:
                dict_uptrend["stock"] = ticker
                dict_uptrend["days_uptrend"] = count
                print(dict_uptrend)
                list_uptrend.append(dict_uptrend)
                # print(list_uptrend)
            break