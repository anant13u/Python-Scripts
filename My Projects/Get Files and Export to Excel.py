import os
from pathlib import Path
import PySimpleGUI as sg

sg.theme('Reddit')

filelist=[]

layout = [  [sg.T('Please enter the path from where you want to retrieve the list of files and folders')],
	        [sg.FolderBrowse(key='-basepath-')],
			[sg.B('Generate List'), sg.B('Exit')]  ]

Window = sg.Window('Generate list of files', layout)

while True:
    event, values = Window.read()
    basepath = values['-basepath-']
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif basepath == None or basepath=='':
        sg.popup('Path cannot be blank.')
    elif event == 'Generate List':
        # Window.close()
        for root, dirs, files in os.walk(basepath):
            filelist.append(f'There are {len(dirs)} folders and {len(files)} files in {root}.\n')
            for dir in dirs:
                filelist.append(f'\nDirectory: {dir}.\n')
                for file in os.listdir(Path(root,dir)):
                    filelist.append(file)
                # filelist.append('\n')
        filelist = '\n'.join(filelist)
        sg.popup_scrolled(filelist, title='Filelist')



# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)
