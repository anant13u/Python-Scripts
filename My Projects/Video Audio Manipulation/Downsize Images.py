import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime
import subprocess

sg.theme('Reddit')
# sg.theme_previewer()

selectImagesText = sg.Text('Select Images', s=(30,2), pad=((40,20),20))
filesBrowse = sg.FilesBrowse(key='-basepath-', s=(15,2), pad=(40,10))

layout = [  [selectImagesText, filesBrowse],
            [sg.B('Downsize', s=(15,2), pad=(70,20)), sg.B('Exit', s=(15,2), pad=(50,10))]  ]

Window = sg.Window('Downsize Images', layout)

while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['-basepath-']=='':
        sg.popup('Please select a folder to perform operations in.')
    elif event == 'Generate List':
        subprocess.Popen(['explorer.exe', basepath]) # Below 2 lines give the same result.
        # subprocess.run(['explorer', basepath])
        # subprocess.Popen(['explorer', basepath])
        print(basepath)




# filelist = '\n'.join(filelist)
            
# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)

# Window.disappear()
# Window.reappear()
        


