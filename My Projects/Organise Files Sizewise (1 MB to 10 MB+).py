from pathlib import Path
import PySimpleGUI as sg
import os
import traceback

# sg.theme_previewer()
sg.theme('DarkGreen7')
layout = [  [sg.T('\nSelect folder:',pad=((30,15),20),s=(40,2)),sg.FolderBrowse(k='input-folder',pad=((0,20),20),s=(15,2))],
            [sg.B('Organise Sizewise',pad=(70,0),s=(20,2)), sg.B('Exit',pad=((0,60),20),s=(20,2))]    ]

window=sg.Window('Organise Files Sizewise (1 MB to 10 MB+)', layout, keep_on_top=True,grab_anywhere=True)

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
                if file_size > 10:
                    new_file_path = Path(basepath, '10 MB+ files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 9:
                    new_file_path = Path(basepath, '9-10 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 8:
                    new_file_path = Path(basepath, '8-9 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 7:
                    new_file_path = Path(basepath, '7-8 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 6:
                    new_file_path = Path(basepath, '6-7 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 5:
                    new_file_path = Path(basepath, '5-6 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                elif file_size > 4:
                    new_file_path = Path(basepath, '4-5 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))
                else:
                    new_file_path = Path(basepath, '0-4 MB files')
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))

            except Exception as e:
                error_info = traceback.format_exc()
                sg.popup(f'Got an error while organising {file}:\n{error_info}', keep_on_top=True)
                print(f'Got an error while organising {file}:\n{error_info}')

        sg.popup('Organising completed.',keep_on_top=True)
