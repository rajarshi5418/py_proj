import logging
from kiteconnect import KiteConnect
import pandas as pd
import pymongo

client = pymongo.MongoClient()
mydb = client['niftydb']
mycol = mydb['fund']

api_key = '9ema9zpibktv34kb'
api_secret = '7fw11t38vofpizy0azt5zd6fo0nsxj2z'
access_token = 'iECb6vMzkoUFTPKcqKrRqmq1ox6hhowK'
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
# def get_positions():
#     dict1 = kite.positions()
#     dict2 = pd.DataFrame(dict1['net'])
#     print(dict2.transpose())

# get_positions()

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
    mycol.insert_one(data)
    print(fund)

# funds_available()

def get_orders():
    dict4 = kite.orders()
    # print(type(dict4))
    dict5 = pd.DataFrame(dict4)
    print(dict5)
    no_orders = len(dict5)
    for i in range(no_orders):
        print(dict5.iloc[i])
        print("\n next order")

# get_orders()

def get_trades():
    dict4 = kite.trades()
    # print(type(dict4))
    dict5 = pd.DataFrame(dict4)
    print(dict5)
    no_trades = len(dict5)
    for i in range(no_trades):
        print(dict5.iloc[i])
        print("\n next order")

# get_trades()

def get_positions():
    dict6 = kite.positions()
    dict7 = pd.DataFrame(dict6['net'])
    print(dict7)
    no_positions = len(dict7)
    for i in range(no_positions):
        print(dict7.iloc[i])
        print("\n next order")

    dict8 = kite.positions()
    dict9 = pd.DataFrame(dict8['day'])
    print(dict9)
    no_positions = len(dict9)
    for i in range(no_positions):
        print(dict9.iloc[i])
        print("\n next order")


# get_positions()


def get_trades():
    dict4 = kite.trades()
    print(type(dict4[0]))
    total_trades = len(dict4[0])
    print(dict4[0])
    dict5 = pd.DataFrame(dict4)
    # print(dict5)
    # no_trades = len(dict5)
    # for i in range(no_trades):
    #     print(dict5.iloc[i])
    #     mycol.insert_one(dict5.iloc[i])
    #     print("\n next order")
    for i in range(total_trades):
        mycol.insert_one(dict4[i])

# get_trades()

# get_positions()

# get_orders()
#
# get_trades()

def get_positions_mongodb():
    dict6 = kite.positions()
    print(dict6['net'])
    pos_list = dict6['net']

    print(dict6['net'][0])
    print(dict6['net'][1])
    for i in range(len(pos_list)):
        mycol.insert_one(dict6['net'][i])


# get_positions_mongodb()

for i in mycol.find():
    print(i)