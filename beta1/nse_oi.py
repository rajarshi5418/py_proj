from nsepy import get_history
import nsepy as nsepy
from datetime import date,timedelta

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
for i in range(15000, 15200, 50):
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
        # print(nifty_opt)

        for i in range(len(nifty_opt)):

            # print(opt,stk,end=" ")
            # print(nifty_opt.index[i],end=' ')
            # print(nifty_opt['Open Interest'][i])
            oi=nifty_opt['Open Interest'][i]
            # print(oi)

        if opt == "CE":
            oi_ce[stk] = oi
            # print(oi_ce)
        elif opt == "PE":
            oi_pe[stk] = oi
            # print(oi_pe)

print(oi_pe)
print(oi_ce)

dict2 = {'CE': oi_ce}
print(dict2)

dict3 = {'PE': oi_ce}
print(dict3)

dict4 = {'CE':oi_ce,'PE':oi_pe }
print(dict4)

list1 = [dict2, dict3]
print(list1)
today_date1 = str(today_date)
print(today_date1)

oi_dict = {today_date1 : list1}
print(oi_dict)

oi_dict1 = {today_date1 : dict4}
print(oi_dict1)

print(oi_dict1['2021-06-03']['CE'][15050])
