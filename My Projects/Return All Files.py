import os
# from os.path import getsize, join
import time

def display_all_files():
    path = input('\n Please enter the path from where you want to retrieve the list of files and folders: \n\n ')
    filelist = []
    total_files_size = 0

    for root, dirs, files in os.walk(path):
        print(f'\n There are {len(files)} files in {root}')
        for file in files:
            current_file = os.path.join(root,file)
            current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)
            total_files_size += current_file_size # Adding the current file's size to the variable total_files_size to print at the end.
            filelist.append(f'\n {file}\n (Size of file is {current_file_size} MB)')
        print('\n'.join(filelist))
    if total_files_size > 999: # If total file size is more than 999 MB it will be displayed in GB.
        print(f'\n The combined size of all files in this folder is {round(total_files_size/1024,2)} GB.\n')
    else:
        print(f'\n The combined size of all files in this folder is {round(total_files_size,2)} MB.\n')
    ans = input(' Do you want to check another folder after this: (Y/N)')
    if ans in ('Y', 'y'):
        display_all_files()
    else:
        print('\n Goodbye!\n')
        time.sleep(1.5)

display_all_files()

# C:\Users\AU\Videos
# E:\Torrents\Introduction to Git and GitHub for Python Developers
# /media/anant/Development
# /media/anant/Development/Notes
