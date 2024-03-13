from pathlib import Path
import PySimpleGUI as sg
import os
import traceback

# sg.theme_previewer()
sg.theme('DarkGreen7')
one_to_ten_radio = sg.Radio('1 MB - 10 MB+', 'size_radios', k='1-10', pad=((60,0),10), default=True)
one_to_hundred_radio = sg.Radio('1 MB - 100 MB+', 'size_radios', k='1-100', pad=(30,10))
one_to_thousand_radio = sg.Radio('1 MB - 1 GB+', 'size_radios', k='1-1000')
layout = [  [sg.T('\nSelect folder:',pad=((30,15),20),s=(40,2)),sg.FolderBrowse(k='input-folder',pad=((0,20),20),s=(15,2))],
            [one_to_ten_radio, one_to_hundred_radio, one_to_thousand_radio],
            [sg.B('Organise Sizewise',pad=(70,0),s=(20,2)), sg.B('Exit',pad=((0,60),20),s=(20,2))]    ]

window=sg.Window('Organise Files Sizewise (1 MB to 10 MB+)', layout, keep_on_top=True,grab_anywhere=True)


def organise_one_to_ten():
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
    elif file_size > 3:
        folder_name = '3-4 MB files'
    elif file_size > 2:
        folder_name = '2-3 MB files'
    elif file_size > 1:
        folder_name = '1-2 MB files'
    else:
        folder_name = '0-1 MB files'

    return folder_name


def organise_one_to_hundred():
    if file_size > 100:
        folder_name = '100 MB+ files'
    elif file_size > 90:
        folder_name = '90-100 MB files'
    elif file_size > 80:
        folder_name = '80-90 MB files'
    elif file_size > 70:
        folder_name = '70-80 MB files'
    elif file_size > 60:
        folder_name = '60-70 MB files'
    elif file_size > 50:
        folder_name = '50-60 MB files'
    elif file_size > 40:
        folder_name = '40-50 MB files'
    elif file_size > 30:
        folder_name = '30-40 MB files'
    elif file_size > 20:
        folder_name = '20-30 MB files'
    elif file_size > 10:
        folder_name = '10-20 MB files'
    else:
        folder_name = '0-10 MB files'

    return folder_name


def organise_one_to_thousand():
    if file_size > 1000:
        folder_name = '1 GB+ files'
    elif file_size > 900:
        folder_name = '900-1000 MB files'
    elif file_size > 800:
        folder_name = '800-900 MB files'
    elif file_size > 700:
        folder_name = '700-800 MB files'
    elif file_size > 600:
        folder_name = '600-700 MB files'
    elif file_size > 500:
        folder_name = '500-600 MB files'
    elif file_size > 400:
        folder_name = '400-500 MB files'
    elif file_size > 300:
        folder_name = '300-400 MB files'
    elif file_size > 200:
        folder_name = '200-300 MB files'
    elif file_size > 100:
        folder_name = '100-200 MB files'
    else:
        folder_name = '0-100 MB files'

    return folder_name
        


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
            if Path.is_file(Path(basepath, file)):
                file_size = os.path.getsize(Path(basepath, file))/(1024*1024) # file_size is 5.0469865798950195
                try:
                    if values['1-10']:
                        folder_name = organise_one_to_ten()
                    elif values['1-100']:
                        folder_name = organise_one_to_hundred()
                    elif values['1-1000']:
                        folder_name = organise_one_to_thousand()

                    new_file_path = Path(basepath, folder_name)
                    if not os.path.exists(new_file_path):
                        os.mkdir(new_file_path)
                    os.rename(Path(basepath, file), Path(new_file_path, file))

                except Exception as e:
                    error_info = traceback.format_exc()
                    sg.popup(f'Got an error while organising {file}:\n{error_info}', keep_on_top=True)
                    print(f'Got an error while organising {file}:\n{error_info}')

        sg.popup('Organising completed.',keep_on_top=True)
