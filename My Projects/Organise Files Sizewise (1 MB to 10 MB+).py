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
                    folder_name = '10 MB+ files'
                elif file_size > 9:
                    folder_name = '9-10 MB files'
                elif file_size > 8:
                    folder_name = '8-9 MB files'
                elif file_size > 7:
                    folder_name = '7-8 MB files'
                elif file_size > 6:
                    folder_name = '6-7 MB files'
                elif file_size > 5:
                    folder_name = '5-6 MB files'
                elif file_size > 4:
                    folder_name = '4-5 MB files'
                else:
                    folder_name = '0-4 MB files'

                new_file_path = Path(basepath, folder_name)
                if not os.path.exists(new_file_path):
                    os.mkdir(new_file_path)
                os.rename(Path(basepath, file), Path(new_file_path, file))

            except Exception as e:
                error_info = traceback.format_exc()
                sg.popup(f'Got an error while organising {file}:\n{error_info}', keep_on_top=True)
                print(f'Got an error while organising {file}:\n{error_info}')

        sg.popup('Organising completed.',keep_on_top=True)
