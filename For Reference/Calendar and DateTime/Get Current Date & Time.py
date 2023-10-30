# import datetime
from datetime import datetime

curr_datetime = datetime.now()
print(curr_datetime)
# 2022-05-07 16:49:15.823345

date_time1 = curr_datetime.strftime('%d/%m/%Y %H:%M:%S')
print('Date & Time in date/month/year hour:minute:second format =', date_time1)
# Date in date/month/year format = 07/05/2022 16:49:15

date_time1 = curr_datetime.strftime('%d-%m-%Y %H-%M-%S')
print('Date in date-month-year hour-minute-second format =', date_time1) # We can use this format in filenames in Windows also.

date5 = curr_datetime.strftime('Month is %m, Date is %d, Year is %Y. Hour is %H, Minute is %M, Second is %S')
print(date5)
# Month is 05, Date is 07, Year is 2022. Hour is 16, Minute is 50, Second is 31