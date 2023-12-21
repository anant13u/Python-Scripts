from rarfile import RarFile
from pathlib import Path
import PySimpleGUI as sg
import os
import traceback

# sg.theme_previewer()
sg.theme('DarkGreen7')
layout = [  [sg.T('\nSelect folder:',pad=((30,15),20),s=(40,2)),sg.FolderBrowse(k='input-folder',pad=((0,20),20),s=(15,2))],
            [sg.B('Extract',pad=(70,0),s=(15,2)), sg.B('Exit',pad=((0,60),20),s=(15,2))]    ]

window=sg.Window('Extract RAR Files', layout, keep_on_top=True,grab_anywhere=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if values['input-folder']=='':
        sg.popup('Please select a folder first.')
    else:
        basepath = values['input-folder']
        print(basepath)
        for file in os.listdir(basepath):
            if Path(file).suffix.lower()=='.rar':
                try:
                    print(file)
                    our_rar = RarFile(Path(basepath,file), 'r')
                    rar_extract_path = Path(basepath,os.path.splitext(file)[0])
                    print(f'rar_extract_path is {rar_extract_path}')
                    if not os.path.exists(rar_extract_path):
                        os.mkdir(rar_extract_path)
                    our_rar.extractall(rar_extract_path)
                    os.rename(Path(basepath, file), Path(rar_extract_path, file))
                except Exception as e:
                    error_info = traceback.format_exc()
                    sg.popup(f'Got an error while extracting {file}:\n{error_info}', keep_on_top=True)
                    print(f'Got an error while extracting {file}:\n{error_info}')

        sg.popup('Extraction completed.',keep_on_top=True)
