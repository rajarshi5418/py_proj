from nsepy import get_history
from datetime import date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nsepy
from matplotlib import style
style.use('fivethirtyeight')

#TICKER NAME
ticker = "SBIN"
#TIME PERIOD, 15 days in this case
end_day = date.today()
start_day = end_day - timedelta(200)

#Fetch ticker data from nsepy
df = get_history(symbol=ticker, start=start_day, end=end_day)
data=df[['Open', 'High', 'Low', 'Close', 'Volume']]
data['15d']= np.round(data['Close'].rolling(window=15).mean(),2)
data['40d']= np.round(data['Close'].rolling(window=40).mean(),2)


data[['Close','15d','40d']].plot(grid=True, figsize=(30,30))
# plt.show()

data['15d-40d']=data['15d']-data['40d']
x=30
data['Stance']=np.where(data['15d-40d']>x,1,0)
data['Stance']=np.where(data['15d-40d']<x,-1,data['Stance'])
# print(data['Stance'].value_counts())
data['Stance'].value_counts()
data['Stance'].plot(lw=2,ylim=[-1.1,1.1])
plt.show()

data['Stock_Returns']=np.log(data['Close']/data['Close'].shift(1))
data['SMAC_Strategy']=data['Stock_Returns']*data['Stance'].shift(1)
data[['Stock_Returns','SMAC_Strategy']].plot(grid=True,figsize=(10,6))
plt.show()


# check for SettingWithCopyWarning. https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy