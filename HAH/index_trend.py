from nsepy import get_history as gh
from datetime import date
from nifty_index_list import nifty_index
count = 0
for i in nifty_index():
    print(count+1,i)
    nifty = gh(symbol=i,
               start=date(2021,5,6),
               end=date(2021,5,8),
               index=True )
    count=count+1
    print(nifty)
