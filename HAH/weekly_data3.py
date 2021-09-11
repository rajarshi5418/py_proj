from nsepy import get_history
from datetime import date,timedelta,datetime
import calendar
import pandas as pd

ticker="SBIN"
dict_week = {}
weekly_data = {}
list_weekly = []

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
    try:
        dte = data["Date"][i]
        print(dte)
        day1 = datetime.weekday(data["Date"][i])
        print(day1)
        if i==0:
            start=i
        elif datetime.weekday(data["Date"][i])==1 and datetime.weekday(data["Date"][i-1])!=0:
            start=i
        elif datetime.weekday(data["Date"][i])==1 and datetime.weekday(data["Date"][i-1])==0:
            start = i-1
    except KeyError:
        print("error1")

    try:
        if i==len(data)-1:
            end = i
            print(data.Date[data.Date == dte].index.tolist())
            j = data.Date[data.Date == dte].index.tolist()
            k = j[0] + 1
            print(k)
            data2 = pd.DataFrame(data.iloc[start:end+1])
            print(data2)
            weekly_data['Open'] = data2.iloc[0]['Open']
            weekly_data['High'] = data2['High'].max()
            weekly_data['Low'] = data2['Low'].min()
            weekly_data['Close'] = data2.iloc[-1]["Close"]
            print(weekly_data)
            list_weekly.append(weekly_data)
            weekly_data = {}

        elif datetime.weekday(data["Date"][i])==3 and datetime.weekday(data["Date"][i+1])==4:
            end = i+1
            print(data.Date[data.Date == dte].index.tolist())
            j = data.Date[data.Date == dte].index.tolist()
            k = j[0] + 1
            print(k)
            data2 = pd.DataFrame(data.iloc[start:end+1])
            print(data2)
            weekly_data['Open'] = data2.iloc[0]['Open']
            weekly_data['High'] = data2['High'].max()
            weekly_data['Low'] = data2['Low'].min()
            weekly_data['Close'] = data2.iloc[-1]["Close"]
            print(weekly_data)
            list_weekly.append(weekly_data)
            weekly_data = {}


        elif datetime.weekday(data["Date"][i]) == 3 and (datetime.weekday(data["Date"][i+1])!=4 or data[i]==data[-1]):
            end = i

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
            list_weekly.append(weekly_data)
            weekly_data = {}
    except KeyError:
        print("error2")
print(list_weekly)

print(pd.DataFrame.from_dict(list_weekly))
