from nsepy import get_history
from datetime import date, timedelta
from nifty_stock_list import nifty,nifty_bank,nifty_next_50,\
    nifty_midcap_100,nifty_midcap_50,nifty_auto,nifty_energy,\
    nifty_financial_service,nifty_metal,nifty_it,nifty_healthcare,\
    nifty_oil_and_gas,nifty_equity_to_trade

# lst = [nifty(),nifty_bank(),nifty_next_50(),nifty_midcap_100()]

for ticker in nifty():
    print(ticker)
    end_day = date.today()
    start_day = end_day - timedelta(365)

    #Fetch ticker data from nsepy
    df = get_history(symbol=ticker, start=start_day, end=end_day)

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
