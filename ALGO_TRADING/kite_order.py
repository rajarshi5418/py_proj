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

