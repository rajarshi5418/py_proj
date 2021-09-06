from nsepy import get_history
from datetime import date, timedelta
ticker = "5PAISA"
end_day = date.today()
start_day = end_day - timedelta(365)

    #Fetch ticker data from nsepy
df = get_history(symbol=ticker, start=start_day, end=end_day, index=True)

#Data preparation for OHLC Candlesticks
data=df[['Open', 'High', 'Low', 'Close', 'Volume']]
print(data)
data.index.name = 'Date'

close = data["Close"]
print(close.max())
max = close.max()

low_date = data[data["Close"] == max].index.values
print(low_date)
time_diff = date.today()-low_date
print(time_diff)