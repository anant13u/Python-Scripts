import os
from pathlib import Path
import PySimpleGUI as sg
import subprocess


# List of file extensions representing temporary files
temp_extensions = ['.tmp', '.temp', '.bak', '.cache', '.log']

selectFolderText = sg.Text('Select Folder',s=(30,2),pad=((40,20),10))
folderBrowse = sg.FolderBrowse(key='-basepath-',s=(15,2),pad=(40,10))

layout = [  [selectFolderText, folderBrowse],
            [sg.B('Clean Temp Files',s=(15,2),pad=(30,10)), sg.B('Exit',s=(15,2),pad=(70,10))]  ]

Window = sg.Window('Generate list of files', layout)

while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['-basepath-']=='':
        sg.popup('Please select a folder to perform operations in.')
    elif event == 'Clean Temp Files':
        for root, dirs, files in os.walk(basepath):
            for file in files:
                file_ext = Path(root, file).suffix
                if file_ext in temp_extensions:
                    print(f'{Path(root, file)} is a temp file.')
        subprocess.Popen(['explorer.exe', basepath])
        # print(basepath)
        