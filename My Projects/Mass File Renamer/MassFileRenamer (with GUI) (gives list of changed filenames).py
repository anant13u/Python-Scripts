import os
import PySimpleGUI as sg

sg.theme("DarkTeal2")

sz= size=(30,3)
layout = [  [sg.T()],[sg.Text('Please select the folder where \nyou want to rename the files',sz),sg.T(' '*6), 
                      sg.FolderBrowse(key='-IN-',size=(15,2))],
            [sg.Text('Please enter the string you \nwant to rename',sz),sg.Input('',sz)],
            [sg.Text('Please enter the new text',sz),sg.Input('',sz)],
            [[sg.T()],sg.T(' '*20),sg.Button('Rename',size=(10,2)),sg.T(' '*10),sg.Button('Cancel',size=(10,2))],[sg.T()]   ]

Window = sg.Window('Mass File Renamer by AU',layout,keep_on_top=True)

lst=[]
while True:
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
    elif event=='Rename':
        pth = values['-IN-']
        txt2replace = values[0]
        newtext = values[1]
        entries = os.listdir(pth)
        print(pth)

        for entry in entries:
            str_check = entry.find(txt2replace) #With this method we check the presence of a substring within another string. 
            # If the substring is present the method will return the number which denotes the beginning of the substring. 
            # If the substring isn't present, the method will return -1.
            newfilename = entry.replace(txt2replace,newtext)
            if str_check>=0:
                os.rename(f'{pth}/{entry}', f'{pth}/{newfilename}')
                lst.append(f'The file: "{entry}" contains "{txt2replace}" in its name, and has been renamed to "{newfilename}"')
            final_list='\n\n'.join(lst) # Separating all list items with a new line.
        sg.popup(f'All files containing the text "{txt2replace}" are now renamed. Please find the list below:\n\n{final_list}',title='List of changed filenames')
        break

#     if str>=0:
#         print('The file: ' + entry + ' contains ' + txt2replace + ' in its name, and will be renamed.')
#         os.rename(pth + '/' + entry , pth + '/' + newfilename)
#         print('Old file name was: ' + entry)
#         print('New file name is: ' + newfilename + '\n')
#     else:
#         print('The file: ' + entry + ' does not contain ' + txt2replace + ' in its name. File will not be renamed.\n')


# C:/Users/AU/Desktop/Python/Test
# test1 - Copy (4)