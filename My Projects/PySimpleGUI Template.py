import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime

sg.theme('Reddit')


selectFolderText = sg.Text('Select Folder',s=(30,2),pad=((40,20),10))
folderBrowse = sg.FolderBrowse(key='-basepath-',s=(15,2),pad=(40,10))

layout = [  [selectFolderText, folderBrowse],
            [sg.B('Generate List',s=(15,2),pad=(30,10)), sg.B('Exit',s=(15,2),pad=(70,10))]  ]

Window = sg.Window('Generate list of files', layout)

while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['-basepath-']=='':
        sg.popup('Please select a folder to perform operations in.')
    elif event == 'Generate List':
        print(basepath)




# filelist = '\n'.join(filelist)
            
# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)

# Window.disappear()
# Window.reappear()
        


