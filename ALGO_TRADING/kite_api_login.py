from kiteconnect import KiteConnect


# request token generator
# https://kite.zerodha.com/connect/login?v=3&api_key=9ema9zpibktv34kb
# print(dir(KiteTicker))


api_key = '9ema9zpibktv34kb'
api_secret = '7fw11t38vofpizy0azt5zd6fo0nsxj2z'

# remove after access_token generation 1
# request_token = 'lsoPGqVWMk7gX0w54Poz9PFJPsC7of2q'

# remove for access_token generation 1
# 'public_token': 'MCoYgrC0kN2RktxXsbdjCUlOL2UZkXnS'
access_token = 'ANGX7bRi3wVDDlA4Vt8m8wo50Uk2vrHX'

kite = KiteConnect(api_key=api_key)

# remove after access_token generation 2
# data = kite.generate_session(request_token, api_secret= api_secret)

# remove for access_token generation 2
kite.set_access_token(access_token)

print(kite.margins())
