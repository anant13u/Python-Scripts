import os
pth = input('Please enter the directory path where you want to rename the files: ')
fname = input('Please enter the file name which you want to rename: ')+'.txt'

txt2replace = input('Please enter the string you want to rename: ')
newtext = input('Please enter the new text: ')
str_find_test = fname.find('test')
if str_find_test>= 0:
    print('The file name contains "test"')
    newfname = f'{pth}/{fname.replace(txt2replace, newtext)}'
    os.rename(f"{pth}/{fname}", newfname)
else:
    print('The file name does not contain "test". File will not be renamed.')


# C:/Users/AU/Desktop/Python/Test
# test1 - Copy (4)