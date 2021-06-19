import pymongo

client = pymongo.MongoClient()

mydb = client['RSI']

# print(mydb.list_collection_names())

# for x in mycol.find():
#     print(x)

for x in mydb.list_collection_names():
    mycol = mydb[x]
    print(x)
    total_profit = 0
    loss_trd = 0
    profi_trd = 0
    for y in mycol.find({},{'_id':0,'profit':1,}):

        total_profit += y['profit']
        # print(y['profit'])
        if y['profit'] > 0:
            profi_trd += 1
        elif y['profit'] < 0:
            loss_trd +=1
    print("total trades", profi_trd+loss_trd)
    print("number of profit trades ",profi_trd)
    print("number of loss trades ", loss_trd)
    print("total profit",round(total_profit,2))


for x in mydb.list_collection_names():
    mycol = mydb[x]
    print(" ")
    print(x)
    total_profit = []
    loss_trd = []
    loss_trd1 = 0
    profi_trd = []
    profi_trd1 = 0
    t_buy_price =[]
    t_sell_price = []
    for y in mycol.find({},{'_id':0, 'buy_price':1, 'sell_price':1, 'profit':1}):
        t_buy_price.append(y['buy_price'])
        t_sell_price.append(y['sell_price'])
        total_profit.append(y['profit'])


        if y['profit'] > 0:
            profi_trd1 += 1
        elif y['profit'] < 0:
            loss_trd1 +=1
    print("buy total", sum(t_buy_price ))
    print("sell total", sum(t_sell_price ))
    print('profit', (sum(t_sell_price )-sum(t_buy_price )))
    print('profit %', (((sum(t_sell_price )-sum(t_buy_price ))/sum(t_buy_price ))*100))
    print("number of profit trades ",profi_trd1)
    print("number of loss trades ", loss_trd1)
    print("total profit",sum(total_profit))

