import os
from pathlib import Path
import PySimpleGUI as sg
from openpyxl import Workbook

sg.theme('Reddit')

filelist=[]

layout = [  [sg.T('Please enter the path from where you want to retrieve the list of files and folders')],
	        [sg.FolderBrowse(key='-basepath-')],
            # [sg.Radio('Full name?','1')],
			[sg.B('Generate List'), sg.B('Exit')]  ]

Window = sg.Window('Generate list of files', layout)

while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif basepath == None or basepath=='':
        sg.popup('Path cannot be blank.')
    elif event == 'Generate List':
        # Window.close()
        for root, dirs, files in os.walk(basepath):
            filelist.append(f'There are {len(dirs)} folders and {len(files)} files in {root}.\n')
            for entry in os.listdir(root):
                filelist.append(entry)
            for dir in dirs:
                filelist.append(f'\nParent Directory: {Path(root,dir)}')
                for entry in os.listdir(Path(root,dir)):
                    filelist.append(entry)
            filelist.append('\n')
        filelist = '\n'.join(filelist)
        sg.popup_scrolled(filelist, title='Filelist')



# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)
