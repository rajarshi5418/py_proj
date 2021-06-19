
import pymongo
from nifty_stock_list import *

client = pymongo.MongoClient()
mydb = client['RSI']

nfty_50 = nifty()

for i in nifty_50:
    print(i)
    mycol = mydb[i]

    def remove_duplicate():
        for x in mycol.find():
            count = 0
            y = x['buy_date']

            for xx in mycol.find():
                z=xx['buy_date']
                if y==z:
                    count+=1

                    if count>1:
                        myQuery ={'buy_date': xx['buy_date']}
                        mycol.delete_one(myQuery)

    remove_duplicate()

