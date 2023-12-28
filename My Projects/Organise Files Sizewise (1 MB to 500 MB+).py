from pathlib import Path
import PySimpleGUI as sg
import os
import traceback

# sg.theme_previewer()
sg.theme('DarkGreen7')
layout = [  [sg.T('\nSelect folder:',pad=((30,15),20),s=(40,2)),sg.FolderBrowse(k='input-folder',pad=((0,20),20),s=(15,2))],
            [sg.B('Organise Sizewise',pad=(70,0),s=(20,2)), sg.B('Exit',pad=((0,60),20),s=(20,2))]    ]

window=sg.Window('Organise Files Sizewise', layout, keep_on_top=True,grab_anywhere=True)

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
            file_size = os.path.getsize(Path(basepath, file))/(1024*1024) # file_size is 5.0469865798950195
            try:
                if file_size > 500:
                    new_file_path = Path(basepath, '500 MB+ files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 400:
                    new_file_path = Path(basepath, '400-500 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 300:
                    new_file_path = Path(basepath, '300-400 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 200:
                    new_file_path = Path(basepath, '200-300 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 100:
                    new_file_path = Path(basepath, '100-200 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                else:
                    new_file_path = Path(basepath, '0-100 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))

            except Exception as e:
                error_info = traceback.format_exc()
                sg.popup(f'Got an error while organising {file}:\n{error_info}', keep_on_top=True)
                print(f'Got an error while organising {file}:\n{error_info}')

        sg.popup('Organising completed.',keep_on_top=True)
