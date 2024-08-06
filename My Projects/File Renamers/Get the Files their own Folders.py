import os
from pathlib import Path
import PySimpleGUI as sg
import traceback

# sg.theme_previewer()
sg.theme('DarkGreen7')

create_folders_button = sg.B('Get the Files\ntheir own Folders', k='-create_folders-', s=(18,3), p=((125,20),40))
layout = [  [sg.T('Select folder:', pad=(70,20), s=(40,2)),sg.FolderBrowse(k='input-folder', pad=((0,20),30), s=(15,2))],
            [create_folders_button, sg.B('Exit', pad=(40,40), s=(18,3))]  ]

window=sg.Window('Rename Movies and Subtitles as per parent folder', layout, keep_on_top=True,grab_anywhere=True)

while True:
    event, values = window.read()
    basepath = values['input-folder']
    print(basepath)
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if values['input-folder']=='':
        sg.popup('Please select a folder first.', keep_on_top=True)
    elif event=='-create_folders-':
        for item in os.listdir(basepath):
            file_ext = Path(item).suffix
            item_folder_path = Path(basepath, item.replace(file_ext, ''))
            if Path(basepath, item).is_file() and not os.path.exists(item_folder_path):
                try:
                    os.mkdir(item_folder_path)
                    os.rename(Path(basepath, item), Path(item_folder_path, item))
                except Exception as e:
                    sg.popup(f'Got an error:\n{e}', keep_on_top=True)
                    print(f'Got an error:\n{e}')
        sg.popup('Files moved to their newly created folders.',keep_on_top=True)


# Adding functionality to create folder for files without folder and move them inside.
