# import datetime
from datetime import datetime

curr_datetime = datetime.now()
print(curr_datetime)
# 2024-01-21 05:42:01.091955

date_time1 = curr_datetime.strftime('%d/%m/%Y %H:%M:%S')
print(f'Date & Time in date/month/year hour:minute:second format = {date_time1}')
# Date & Time in date/month/year hour:minute:second format = 21/01/2024 05:42:01

date_time1 = curr_datetime.strftime('%d-%m-%Y %H-%M-%S')
print(f'Date in date-month-year hour-minute-second format = {date_time1}') # We can use this format in filenames in Windows also.
# Date in date-month-year hour-minute-second format = 21-01-2024 05-42-01

date5 = curr_datetime.strftime('Month is %m, Date is %d, Year is %Y. Hour is %H, Minute is %M, Second is %S')
print(date5)
# Month is 01, Date is 21, Year is 2024. Hour is 05, Minute is 42, Second is 01
