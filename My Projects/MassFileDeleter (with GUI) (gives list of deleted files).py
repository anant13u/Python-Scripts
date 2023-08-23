import os
import PySimpleGUI as sg

sg.theme("DarkTeal2")

sz= size=(30,3)
layout = [  [sg.T()],[sg.Text('Please select the folder where \nyou want to rename the files',sz),sg.T(' '*6), 
                      sg.FolderBrowse(key='-IN-',size=(15,2))],
            [[sg.T()],sg.T(' '*20),sg.Button('Delete',size=(10,2)),sg.T(' '*10),sg.Button('Cancel',size=(10,2))],[sg.T()]   ]

Window = sg.Window('Mass File Renamer by AU',layout,keep_on_top=True)

lst=[]
while True:
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
    elif event=='Delete':
        pth = values['-IN-']
        entries = os.listdir(pth)
        print(pth)

        for entry in entries:
            if entry.startswith('.'):
                os.remove(os.path.join(pth, entry))
                lst.append(f'The file: "{entry}" starts with a period and has been deleted."')
            final_list='\n\n'.join(lst) # Separating all list items with a new line.
        sg.popup(f'All files starting with a period (.) have been deleted. Please find the list below:\n\n{final_list}',title='List of changed filenames')
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