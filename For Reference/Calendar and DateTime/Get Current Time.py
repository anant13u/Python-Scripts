# import datetime
from datetime import datetime

curr_time = datetime.now().time()
print(f'Current time is {curr_time}')
# Current time is 17:04:08.331710

time1 = curr_time.strftime('%H:%M:%S')
print(f'Time in hour:minute:second format = {time1}')
# Time in hour:minute:second format = 17:01:35

time2 = curr_time.strftime('%H %M %S')
print(f'Time in hour-minute-second format = {time2}') # We can use this format in filenames in Windows also.
# Time in hour-minute-second format = 17 01 35

time3 = curr_time.strftime('Hour is %H, Minute is %M, Second is %S')
print(time3)
# Hour is 17, Minute is 01, Second is 35
