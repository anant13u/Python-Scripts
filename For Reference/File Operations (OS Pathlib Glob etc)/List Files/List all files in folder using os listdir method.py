import os
import time

curr_path = input('Enter the path where you want to perform the checks: ')
print(curr_path)

# Printing the list of files in the current directory.
print(f'{os.listdir(curr_path)}\n')

# Unpacking the list and printing each element in a new line.
print(*os.listdir(curr_path),sep='\n')

time.sleep(2)
