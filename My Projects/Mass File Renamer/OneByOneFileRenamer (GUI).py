import os
import PySimpleGUI as sg
from pathlib import Path

sg.theme("DarkTeal2")

sz= size=(20,2)
layout = [  [sg.Text('Please select the folder where you want to rename the files', pad=(20,15)), sg.FolderBrowse(key='-IN-',size=(15,2),pad=(20,15))],
            [sg.Text("Current File's Name",pad=(20,15)),sg.T('',key='old-filename',pad=((65,0),15))],
            [sg.Text('Please enter the new name',pad=(20,15)),sg.Input('',key='new-filename',size=(40,1),pad=(20,15))],
            [sg.Button('Rename',size=(10,2),pad=((130,20),15)),sg.T(' '*10),sg.Button('Exit',size=(10,2),pad=((20,70),15))]    ]

Window = sg.Window('Mass File Renamer by AU',layout,keep_on_top=True)

def file_rename():
    Window['old-filename'].update(filename)
    Window['new-filename'].update(filename)
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        exit()
    # else:
    new_name = values['new-filename']
    if new_name!=filename:
        if not Path(new_name).suffix == Path(filename).suffix:
            sg.popup('Extension of file can not be changed.',keep_on_top=True)
            file_rename()
        else:
            # print(Path(new_name).suffix)
            old_path = os.path.join(basepath, filename)
            new_path = os.path.join(basepath, new_name)
            os.rename(old_path, new_path)

changes_list=[]
while True:
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event=='Rename':
        if values['-IN-']=='':
            sg.popup('Please select a folder to perform operations in.',keep_on_top=True)
        else:
            basepath = values['-IN-']
            for filename in os.listdir(basepath):
                file_rename()
            next_step = sg.popup_yes_no('Rename Completion',modal=True)
            if next_step == 'Yes':
                

                # os.rename(os.path.join(basepath, filename), os.path.join(basepath, newfilename))

            # for currfilename in entries:
            #     str_check = currfilename.find(old_string) #With this method we check the presence of a substring within another string. 
            #     # If the substring is present the method will return the number which denotes the beginning of the substring. 
            #     # If the substring isn't present, the method will return -1.
            #     newfilename = currfilename.replace(old_string,new_string)
            #     if str_check>=0:
            #         os.rename(os.path.join(basepath, currfilename), os.path.join(basepath, newfilename))
            #         changes_list.append(f'Old filename: {currfilename}.\n'
            #                             f'New filename: {newfilename}')
            #     final_list='\n\n'.join(changes_list) # Separating all list items with a new line.
            # if final_list.find(old_string)>1:
            #     sg.popup(f'All files containing the text "{old_string}" are now renamed. Please find the list below:\n\n{final_list}',title='List of changed filenames',line_width=100,grab_anywhere=True,keep_on_top=True)
            # else:
            #     sg.popup(f'No files found with {old_string} in their names.',keep_on_top=True,grab_anywhere=True)
            # changes_list=[]
            # final_list=''
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