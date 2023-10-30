import os
import PySimpleGUI as sg
from pathlib import Path

sg.theme('Dark Teal 2')
sg.set_options(font=('Calibri',11)) # https://stackoverflow.com/a/67155752/18791688

rename_layout = [ [sg.FolderBrowse('Select Folder',key='input_folder'),sg.T()],
                # [sg.T('Select the directory where you want to rename the files:'),
                #   [sg.T(key='folder_name')],
                  [sg.T('Enter the text you want to replace: '), sg.I(key='old_string')],
                  [sg.T('Enter the new text you want to enter: '), sg.I(key='new_string')],
                  [sg.B('Replace Text'),sg.B('Swap Values'), sg.B('Exit')] ]
                
rename_window = sg.Window('Rename Files', rename_layout)

while True:
    event, values = rename_window.read()
    # rename_window['folder_name'].update('input_folder')
    curr_path = Path(values['input_folder'])
    # print(curr_path)
    new_string = values['new_string']
    old_string = values['old_string']
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['input_folder'] == '':
        sg.popup('Please select a directory first.')#,auto_close_duration=1)
        # rename_window['input_folder'].update(curr_path)
    elif event in 'Swap Values':
        rename_window['old_string'].update(new_string)
        rename_window['new_string'].update(old_string)
    else:
        for root, dirs, files in os.walk(curr_path):
            for file in files:
                if old_string in file and Path.joinpath(Path(root),file).is_file():
                    new_filename = file.replace(old_string, new_string)
                    Path.joinpath(Path(root),file).rename(Path.joinpath(Path(root),new_filename))
        
    # break

# curr_path = Path(input('\nPlease enter the directory where you want to rename the files: \n'))
