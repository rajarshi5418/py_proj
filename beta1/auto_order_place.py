
import time
from kiteconnect import KiteTicker
from kiteconnect import KiteConnect

import pymongo
client = pymongo.MongoClient()

mydb = client['niftydb']
mycol = mydb['optionprice']

api_key = '9ema9zpibktv34kb'  # open('api_key.txt','r').read()
access_token = 'ANGX7bRi3wVDDlA4Vt8m8wo50Uk2vrHX'  # open('access_token.txt','r').read()

api_secret = '7fw11t38vofpizy0azt5zd6fo0nsxj2z'
kite = KiteConnect(api_key = api_key)
kite.set_access_token(access_token)


kws = KiteTicker(api_key, access_token)
# tokens = [5215745, 633601, 1195009, 779521, 758529, 1256193, 194561, 1837825, 952577, 1723649, 3930881,
# 4451329, 593665, 3431425, 2905857]
# tokens=[53787399,53520391,54123271]
# dict={53787399:'CRUDEOIL18SEPFUT',53520391:'SILVERM18NOVFUT',54123271:'GOLDM18OCTFUT'}

# print(dir(KiteTicker))

tokens = [256265,]
dict = {256265: 'NIFTY'}



def on_ticks(ws, ticks):

    ticks = ticks[0]['last_price']
    print(ticks)
    # print("nifty price = ", ticks)
    print("hello tick")
    dict1 = kite.positions()
    quantity = dict1['net'][0]['quantity']

    if ticks >= 15300 and quantity==0:

        kite.place_order(exchange= 'NSE',
                         tradingsymbol= 'PNB',
                              order_type= 'MARKET',
                              transaction_type= 'BUY',
                              validity= 'DAY',
                              product= 'CNC',
                              quantity= 1,
                              variety='regular')
        print('order placed')

    if ticks >= 15320 and quantity > 0:

        order = kite.place_order(     exchange= 'NSE',
                              tradingsymbol= 'PNB',
                              order_type= 'MARKET',
                              transaction_type= 'SELL',
                              validity= 'DAY',
                              product= 'CNC',
                              quantity= 1,
                              price= .5,
                              variety='regular')
        print("order squared off")

def on_connect(ws, response):
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL, tokens)


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect(threaded=True)
count = 0
while True:
    count += 1
    if (count % 2 == 0):
        if kws.is_connected():
            kws.set_mode(kws.MODE_FULL, tokens)
            print("hello nifty if")

        else:
            if kws.is_connected():
                kws.set_mode(kws.MODE_FULL, tokens)
                print("hello nifty else")
        time.sleep(0.36)
    # rint("hello nifty")
