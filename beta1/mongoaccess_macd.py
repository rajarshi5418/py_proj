import pymongo
from pandas import DataFrame



client = pymongo.MongoClient()

mydb = client['NIFTY50']
mycol = mydb['SBIN.NS']

df = DataFrame(list(mycol.find({},{'_id':0})))
print(df)

# count = 0
# for i in mycol.find():
#     print(i)
#     count +=1
#
#     print(count)