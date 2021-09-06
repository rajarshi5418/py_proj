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

dte = data.Date[0]
day1 = datetime.weekday(dte)
k=4-day1
print(k)

for i in range(k+1,len(data),5):

    data2=pd.DataFrame(data.iloc[i:i+5])
    print(data2)
    weekly_data['Open']=data2.iloc[0]['Open']
    weekly_data['High']=data2['High'].max()
    weekly_data['Low']=data2['Low'].min()
    weekly_data['Close']=data2.iloc[-1]["Close"]
    print(weekly_data)

