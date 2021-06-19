from nsepy import get_history
import nsepy as nsepy
from datetime import date,timedelta
import pandas as pd
import xlwings as xw

today_date = date.today()-timedelta(days=1)
print(today_date)

expiry = sorted(nsepy.get_expiry_date(year=date.today().year, month=date.today().month))
print(expiry)

for i in expiry:
    if i >= today_date:
        expiry_option = i
        break
print(expiry_option)

option = ['CE','PE']

# generating strike price
strike = []
for i in range(14000, 16000, 50):
    strike.append(i)
print(strike)

oi_ce = {}
oi_pe = {}

for opt in option:
    for stk in strike:

        nifty_opt = get_history(symbol="NIFTY",
                                start=today_date,
                                end=today_date,
                                index=True,
                                option_type=opt,
                                strike_price=stk,
                                expiry_date=expiry_option)

        for i in range(len(nifty_opt)):
            oi=nifty_opt['Open Interest'][i]

        if opt == "CE":
            oi_ce[stk] = oi
            # print(oi_ce)
        elif opt == "PE":
            oi_pe[stk] = oi
            # print(oi_pe)

print(oi_pe)
print(oi_ce)

df = pd.DataFrame(list(oi_ce.items()),columns = ['strike_price','open_interest_ce'])
df1 = pd.DataFrame(list(oi_pe.items()),columns = ['strike_price','open_interest_pe'])

book = xw.Book("dict1.xlsx")
wsData = book.sheets['Sheet3']
wsData.cells.clear_contents()
wsData.range('A1').value =df
wsData.range('D1').value =df1

dict2 = {'CE': oi_ce}
dict3 = {'PE': oi_ce}
dict4 = {'CE':oi_ce,'PE':oi_pe }

today_date1 = str(today_date)
oi_dict1 = {today_date1 : dict4}
print(oi_dict1)

# print(oi_dict1['2021-06-03']['CE'][15050])
