from kiteconnect import KiteConnect
import time
from kiteconnect import KiteTicker


api_key='9ema9zpibktv34kb' # open('api_key.txt','r').read()
access_token='UnPu4SD3toNrHLKBkKLBnDjeZQLTjtm2'#open('access_token.txt','r').read()


kws = KiteTicker(api_key,access_token)
#tokens = [5215745, 633601, 1195009, 779521, 758529, 1256193, 194561, 1837825, 952577, 1723649, 3930881,
# 4451329, 593665, 3431425, 2905857]
# tokens=[53787399,53520391,54123271]
# dict={53787399:'CRUDEOIL18SEPFUT',53520391:'SILVERM18NOVFUT',54123271:'GOLDM18OCTFUT'}

# print(dir(KiteTicker))

tokens= [10545410]
dict={10545410:'NIFTY2160315200CE'}


def on_ticks(ws, ticks):
        ticks=[dict[ticks[0]['instrument_token']],ticks[0]['timestamp'],ticks[0]['last_price'],ticks[0]['volume']]
        print(ticks)
     
def on_connect(ws, response):
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL,tokens)


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect(threaded=True)
count=0
while True:
        count+=1
        if(count%2==0):
                if kws.is_connected():
                        kws.set_mode(kws.MODE_FULL,tokens)
                else:
                        if kws.is_connected():
                                kws.set_mode(kws.MODE_FULL,tokens)
                time.sleep(0.350)


