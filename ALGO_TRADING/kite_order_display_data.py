import logging
from kiteconnect import KiteConnect
import pandas as pd

api_key = '9ema9zpibktv34kb'
api_secret = '7fw11t38vofpizy0azt5zd6fo0nsxj2z'
access_token = 'ANGX7bRi3wVDDlA4Vt8m8wo50Uk2vrHX'
kite = KiteConnect(api_key = api_key)
kite.set_access_token(access_token)


# kite.place_order(     exchange= 'NSE',
#                       tradingsymbol= 'PNB',
#                       order_type= 'LIMIT', 
#                       transaction_type= 'BUY', 
#                       validity= 'DAY', 
#                       product= 'CNC', 
#                       quantity= 1, 
#                       price= 35.5,
#                       trigger_price=35,
#                       squareoff=2,
#                       stoploss=1,
#                       variety='regular')

# order = kite.place_order(     exchange= 'NSE',
#                       tradingsymbol= 'PNB',
#                       order_type= 'MARKET',
#                       transaction_type= 'SELL',
#                       validity= 'DAY',
#                       product= 'CNC',
#                       quantity= 1,
#                       price= .5,
#                       variety='regular')
def get_positions():
    dict1 = kite.positions()
    dict2 = pd.DataFrame(dict1['net'])
    print(dict2.transpose())

get_positions()

# print(dict1['net'][0]['tradingsymbol'])
# dict1 = kite.positions()
# for i in dict1['day'][0]:
#     print(i,"\t=",dict1['net'][0][i])
#     # print(i)

def funds_available():
    dict3 = kite.margins()
    cash = dict3['equity']['available']['cash']
    collateral = dict3['equity']['available']['collateral']
    total_fund = cash+collateral
    data = {'cash': cash, 'collateral': collateral, 'total_fund': total_fund}
    fund = pd.DataFrame.from_dict(data, orient='index')
    print(fund)

funds_available()

# dict4 = pd.DataFrame(dict3)
# print(dict4)
# print(dict4['equity'].iloc[1])
# print(dict4['equity'].iloc[2]['cash'])


# enabled
# net
# available
# utilised

# for j in dict4.index:
#     print(j)


