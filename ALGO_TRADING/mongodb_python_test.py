from nsepy import get_history as gh
from datetime import date
from datetime import datetime
import pymongo
from pymongo import MongoClient
import pandas as pd
client = pymongo.MongoClient()
import json

mydb = client['niftydb']
mycol = mydb['date']


# nifty = gh(symbol="NIFTY",
#                start=date(2015,5,17),
#                end=date(2021,5,24),
#                index=True )

# nifty_data = pd.DataFrame(nifty)
# idx = nifty_data._data.axes[1]
# print(idx)

# print(nifty_data['Open'])


# nifty_data = pd.DataFrame(nifty)
# print(nifty_data._data.axes[0])


# print(nifty_data._data)
# print(nifty_data._data.axes)


# result = nifty.to_json(orient="table")
# parsed = json.loads(result)
# json.dumps(parsed, indent=4)
#
# print(result)
# with open("sample.json", "w") as outfile:
#     outfile.write(result)
# mycol.insert_many("sample.json")


# result = nifty.to_dict(orient="index")
# print(result)


# d = nifty.set_index().to_dict()
# print(d)

# data = pd.read_csv('sample1.csv')
# Load csv dataset


# data.reset_index(inplace=True)
# data_dict = data.to_dict("records")
# # Insert collection
# mycol.insert_many(data_dict)
# print(mydb.list_collection_names())

# list1 = []

# for x in mycol.find({},{'_id':0,'Open':1,'Date':1}):
#
#     print(x)



# for x in nifty_data.itertuples() :
#     # mycol.insert_one(x)
#     dat = str(x.Index)
#     # print(dat)
#     # print(x.Index,x.Open,x.High, x.Low,x.Close,x.Volume,x.Turnover)
#     data = {'Date': dat,'Open':x.Open,'High':x.High,'Low': x.Low,'Close':x.Close,'Volume':x.Volume,'Turnover':x.Turnover,}
#     # data = {'Date': dat}


    # mycol.insert_one(data)

def printdate():

    list1 = []
    for x in nifty_data.axes:
        list1.append(x)
        print(x)
    len_data = len(list1[0])
    for j in range(len_data):

        k= nifty_data.axes[0][j]
        print(k)


# printdate()
# print(nifty_data._data.axes())


#     # mycol.insert_one(x)

# for x in mycol.find():
#     print((x['Date']),"\t ",(x['Open']))

def remove_duplicate():
    for x in mycol.find():
        count = 0
        y = x['Date']

        for xx in mycol.find():
            z=xx['Date']
            if y==z:
                count+=1

                if count>1:
                    myQuery ={'Date': xx['Date']}
                    mycol.delete_one(myQuery)
# print("")
# remove_duplicate()
for x in mycol.find({"Date": '2021-05-18'}):
    print(x)



