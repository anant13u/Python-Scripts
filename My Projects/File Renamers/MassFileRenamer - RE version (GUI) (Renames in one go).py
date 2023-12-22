import os
import PySimpleGUI as sg
import re

sg.theme("DarkTeal2")

sz= size=(20,2)
layout = [  [sg.Text('Please select the folder where you want to rename the files',size=(30,2), pad=(20,15)), sg.FolderBrowse(key='-IN-',size=(15,2),pad=((70,20),15))],
            [sg.Text('Please enter the string you want to rename',sz,pad=(20,15)),sg.Input('',key='old-string',pad=(10,10),size=(40,2))],
            [sg.Text('Please enter the new text',sz,pad=(20,15)),sg.Input('',key='new-string',size=(40,2),pad=(10,10))],
            [sg.Button('Rename',size=(10,2),pad=((70,20),15)),sg.T(' '*10),sg.Button('Exit',size=(10,2),pad=((20,70),15))]    ]

Window = sg.Window('Mass File Renamer by AU',layout,keep_on_top=True, grab_anywhere=True)

changes_list=[]
while True:
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event=='Rename':
        if values['-IN-']=='':
            sg.popup('Please select a folder to perform operations in.',keep_on_top=True)
        if values['old-string']=='':
            sg.popup('Please enter a string to replace.',keep_on_top=True)
        else:
            basepath = values['-IN-']
            old_string = values['old-string']
            # re.sub()
            escaped_old_string = re.compile(old_string)
            # pattern = re.compile(old_string)
            new_string = values['new-string']
            entries = os.listdir(basepath)
            print(basepath)

            for currfilename in entries:
                x = re.search(old_string,currfilename)
                # str_check = currfilename.find(old_string) #With this method we check the presence of a substring within another string. 
                # newfilename = currfilename.replace(escaped_old_string,new_string)
                if x:
                    # If matches is not empty, it means the escaped_old_string is present in currfilename
                    newfilename = re.sub(old_string,new_string,currfilename)
                    os.rename(os.path.join(basepath, currfilename), os.path.join(basepath, newfilename))
                    changes_list.append(f'Old filename: {currfilename}\n'
                                        f'New filename: {newfilename}')
                final_list='\n\n'.join(changes_list) # Separating all list items with a new line.
            if final_list.find(old_string)>1:
                sg.popup(f'All files containing the text "{old_string}" are now renamed. Please find the list below:\n\n{final_list}',title='List of changed filenames',line_width=100,grab_anywhere=True,keep_on_top=True)
            else:
                sg.popup(f'No files found with {old_string} in their names.',keep_on_top=True,grab_anywhere=True)
            changes_list=[]
            final_list=''
            # break

#     if str>=0:
#         print('The file: ' + entry + ' contains ' + txt2replace + ' in its name, and will be renamed.')
#         os.rename(pth + '/' + entry , pth + '/' + newfilename)
#         print('Old file name was: ' + entry)
#         print('New file name is: ' + newfilename + '\n')
#     else:
#         print('The file: ' + entry + ' does not contain ' + txt2replace + ' in its name. File will not be renamed.\n')


# C:/Users/AU/Desktop/Python/Test
# test1 - Copy (4)
            