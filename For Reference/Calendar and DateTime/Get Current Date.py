# import datetime
from datetime import date

curr_date = date.today()
print(curr_date)
# 2022-05-07

date1 = curr_date.strftime('%d/%m/%Y')
print(f'Date in date/month/year format = {date1}')
# Date in date/month/year format = 07/05/2022

date2 = curr_date.strftime('%B %d, %Y')
print('Date in month day, year format =', date2)
# Date in month day, year format = May 07, 2022

date3 = curr_date.strftime('%b-%d-%Y')
print('Date in month-date-year format =', date3)
# Date in month-date-year format = May-07-2022

date4 = curr_date.strftime('Month is %m, Date is %d, Year is %Y')
print(date4)
# Month is 05, Date is 07, Year is 2022
