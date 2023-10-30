import os
import time


cwd = os.getcwd()
print(cwd)
contents = os.listdir()

begin_time = time.time()
for c in contents:
    print(c)
end_time = time.time()
print(f'Time taken when printing all filenames one by one is {end_time-begin_time} seconds\n')

filelist = []
begin_time2 = time.time()
for c in contents:
    filelist.append(c)
print(*filelist)
end_time2 = time.time()
print(f'Time taken when adding filenames to a list and then displaying the list at the end is {end_time2-begin_time2} seconds\n')

begin_time3 = time.time()
[print(file) for file in contents]
end_time3 = time.time()
print(f'Time taken when printing the filenames directly using list comprehension is {end_time3-begin_time3} seconds\n')

print(f'{os.path.getsize(cwd)/1024} MB')
