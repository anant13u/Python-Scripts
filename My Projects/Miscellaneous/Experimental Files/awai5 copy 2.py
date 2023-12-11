import csv

our_file = input('Enter the entire filepath for the csv file you wish to read: ')
our_file = our_file.replace('"','')

open_file = open(our_file,'r')

content = csv.reader(open_file,delimiter=',')

for each in content:
    print(each)

open_file.close()
"D:\Python\For Reference\File Operations (OS Pathlib Glob etc)\File Operations - Test Folder\PocketExpense_data_20150813.csv"
# "D:\Python\For Reference\File Operations (OS Pathlib Glob etc)\File Operations - Test Folder\PocketExpense_data_20150813.csv"