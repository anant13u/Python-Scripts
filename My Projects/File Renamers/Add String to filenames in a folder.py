import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime
import subprocess

sg.theme('Reddit')
# sg.theme_previewer()

selectFolderText = sg.Text('Select Folder',s=(30,2),pad=((40,20),20))
folderBrowse = sg.FolderBrowse(key='-basepath-',s=(15,2),pad=(40,10))

layout = [  [selectFolderText, folderBrowse],
            [sg.T('String', pad=((40,100),30)), sg.I(k='joiner-string', s=40)],
            [sg.B('Add string at the beginning',s=(15,2),pad=(55,30)), sg.B('Add string at the end',s=(15,2),pad=(55,30)), sg.B('Exit',s=(15,2),pad=(70,10))]  ]

Window = sg.Window('Generate list of files', layout)

while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    joinerString = values['joiner-string']
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['-basepath-']=='':
        sg.popup('Please select a folder to perform operations in.')
    elif event == 'Add string at the beginning':
        # basepath = Path(values['-basepath-'])
        # joinerString = values['joiner-string']
        # subprocess.Popen(['explorer.exe', basepath]) # Below 2 lines give the same result.
        # subprocess.run(['explorer', basepath])
        # subprocess.Popen(['explorer', basepath])
        print(basepath)
        for entry in os.listdir(basepath):
            curr_name = Path(basepath, entry)
            print(f'{joinerString}{entry}')
            print(os.path.splitext(entry)[0])
    elif event == 'Add string at the end':
        for entry in os.listdir(basepath):
            justFilename = os.path.splitext(entry)[0]
            fileExt = os.path.splitext(entry)[1]
            # currName = Path(basepath, entry)
            print(f'{justFilename}{joinerString}{fileExt}')




# filelist = '\n'.join(filelist)
            
# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)

# Window.disappear()
# Window.reappear()
        


