import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime
import subprocess

sg.theme('Reddit')
# sg.theme_previewer()

selectFolderText = sg.Text('Select Folder',s=(30,2),pad=((40,20),30))
folderBrowse = sg.FolderBrowse(key='-basepath-',s=(15,2),pad=(40,10))

layout = [  [selectFolderText, folderBrowse],
            [sg.T('String', pad=((40,100),20)), sg.I(k='joiner-string', s=40, enable_events=True)],
            [sg.T('filename.mp4',k='begin-textbox', s=(30,2), p=((85,0),20)), sg.T('filename.mp4', k='end-textbox', s=(20,2))],
            [sg.B('Add string at the beginning',s=(22,2),pad=((50,30),20)), sg.B('Add string at the end',s=(22,2),pad=(20,20))],
            [sg.B('Exit',s=(15,2),pad=(190,30))]  ]

Window = sg.Window('Generate list of files', layout, keep_on_top=True)

while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    joinerString = values['joiner-string']
    Window['begin-textbox'].update(f'{joinerString}filename.mp4')
    Window['end-textbox'].update(f'filename{joinerString}.mp4')
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['-basepath-']=='':
        sg.popup('Please select a folder to perform operations in.')
    elif event == 'Add string at the beginning':
        print(basepath)
        for entry in os.listdir(basepath):
            os.rename(Path(basepath, entry), Path(basepath, f'{joinerString}{entry}'))
        # subprocess.Popen(['explorer.exe', basepath]) # Below 2 lines give the same result.
        # subprocess.run(['explorer', basepath])
        # subprocess.Popen(['explorer', basepath])
    elif event == 'Add string at the end':
        for entry in os.listdir(basepath):
            justFilename = os.path.splitext(entry)[0]
            fileExt = os.path.splitext(entry)[1]
            os.rename(Path(basepath, entry), Path(basepath, f'{justFilename}{joinerString}{fileExt}'))
        # subprocess.Popen(['explorer.exe', basepath]) # Below 2 lines give the same result.




# filelist = '\n'.join(filelist)
            
# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)

# Window.disappear()
# Window.reappear()
        


