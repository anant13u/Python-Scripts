# pip install wmi

import wmi

connection = wmi.WMI()

for os in connection.win32_operatingsystem():
    print(os.caption)
