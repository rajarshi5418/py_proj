from kiteconnect import KiteConnect
from kite_api_login import login

# api_secret = '7fw11t38vofpizy0azt5zd6fo0nsxj2z'
#
# access_token = 'Xto61BnuPdOSM6WzbYEMJPB615kP6Uet'
#
# kite = KiteConnect(api_key = '9ema9zpibktv34kb')
# kite.set_access_token(access_token)
login(KiteConnect)
# kite = login.kite()
order =kite.margins()
i = 0
# for od in order:
#     print(od[i])
#     i+=1

print(order['equity']['net'])
print(order['equity']['available']['cash'])
key = dict.fromkeys(order['equity'])
print(key)
key = dict.fromkeys(order['equity']['available'])
print(key)
print(order)