import os
# import time

# curr_path = input('Enter the path where you want to perform the checks: ')
# print(curr_path)

# print(f'{os.listdir(curr_path)}\n')

# print(*os.listdir(curr_path),sep='\n')

path = 'D:\Python\Git & GitHub'

[print(os.path.join(root,file)) for root, dirs, files in os.walk(path) for file in files] # List comprehension is used.

# time.sleep(2)
