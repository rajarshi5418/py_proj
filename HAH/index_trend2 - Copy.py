from nsepy import get_history as gh
from datetime import date
from nifty_index_list import nifty_index
count = 0
nfty_indx = ['NIFTY INFRA','NIFTY SMLCAP 100','NIFTY SMLCAP 50','NIFTY SMLCAP 250','NIFTY MIDSML 400','NIFTY MEDIA','NIFTY REALTY',
             'NIFTY PHARMA','NIFTY METAL','NIFTY IT','NIFTY OIL AND GAS','NIFTY AUTO','NIFTY ENERGY','NIFTY CONSUMER DURABLES',
             'NIFTY BANK','NIFTY FMCG',"NIFTY MIDCAP 50","NIFTY MIDCAP 100",'NIFTY COMMODITIES','NIFTY CONSUMPTION','NIFTY CPSE','NIFTY INFRA','NIFTY SERV SECTOR']
for i in nfty_indx:
    print(count+1,i)
    nifty = gh(symbol=i,
               start=date(2021,9,6),
               end=date(2021,9,9),
               index=True )
    count=count+1
    print(nifty)
    # print((nifty.iloc[-1][Close]-nifty.iloc[-2][Close])/nifty.iloc[-2][Close])
    print(((nifty.iloc[-1]['Close']-nifty.iloc[-2]['Close'])/nifty.iloc[-2]['Close'])*100)

