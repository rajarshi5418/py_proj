from nsepy import get_history
from datetime import date,timedelta,datetime
import calendar
import pandas as pd

ticker="SBIN"
dict_week = {}
weekly_data = {}
list_week = []
print(ticker)
end_day = date.today()
start_day = end_day - timedelta(365)

#Fetch ticker data from nsepy
df = get_history(symbol=ticker, start=start_day, end=end_day)

#Data preparation for OHLC Candlesticks
data=df[['Open', 'High', 'Low', 'Close', 'Volume']]
data.reset_index(drop=False, inplace=True)
print(data)

for i in range(len(data)):
    dte = data["Date"][i]
    print(dte)
    op = data['Volume'][i]
    day1 = datetime.weekday(dte)
    print(day1)
    if day1==0:
        start=i
    if day1==4:
        print(data.Date[data.Date == dte].index.tolist())
        j = data.Date[data.Date == dte].index.tolist()
        k=j[0]+1
        print(k)
        data2=pd.DataFrame(data.iloc[start:k])
        print(data2)
        weekly_data['Open']=data2.iloc[0]['Open']
        weekly_data['High']=data2['High'].max()
        weekly_data['Low']=data2['Low'].min()
        weekly_data['Close']=data2.iloc[-1]["Close"]
        print(weekly_data)


