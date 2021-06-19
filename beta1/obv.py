import pandas_datareader.data as pdr
import numpy as np
import datetime

# Download historical data for required stocks
ticker = "AAPL"
ohlcv = pdr.get_data_yahoo(ticker,datetime.date.today()-datetime.timedelta(364),datetime.date.today())
df = ohlcv.copy()

def OBV(DF):
    """function to calculate On Balance Volume"""
    df = DF.copy()
    df['daily_ret'] = df['Adj Close'].pct_change()
    df['direction'] = np.where(df['daily_ret']>=0,1,-1)
    # replacing direction[0] = 0
    io = df.index[0]
    df.loc[io,'direction']= 0

    df['vol_adj'] = df['Volume'] * df['direction']
    df['obv'] = df['vol_adj'].cumsum()
    print(df)
    return df['obv']

OBV(df)