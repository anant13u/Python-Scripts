import os
rename_directory = input('Please enter the directory path where you want to rename the files: ')
entries = os.listdir(rename_directory)

txt2replace = input('Please enter the string you want to rename: ')
newtext = input('Please enter the new text: ')

for curr_filename in entries:
    str_check = curr_filename.find(txt2replace) #With this method we check the presence of a substring within another string. 
    # If the substring is present str_check will return the number which denotes the beginning of the substring. 
    # If the substring isn't present, str_check will return -1.
    newfilename = curr_filename.replace(txt2replace,newtext)
    if str_check>=0:
        print(f'The file: {curr_filename} contains {txt2replace} in its name, and will be renamed.')
        os.rename(f'{rename_directory}/{curr_filename}', f'{rename_directory}/{newfilename}')
        print(f'Old file name was: {curr_filename}')
        print(f'New file name is: {newfilename}\n')
    else:
        print(f'The file: {curr_filename} does not contain {txt2replace} in its name. File will not be renamed.\n')

# C:/Users/AU/Desktop/Python/Test
# test1 - Copy (4)