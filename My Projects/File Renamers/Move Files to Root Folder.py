import os
from pathlib import Path
import PySimpleGUI as sg
import traceback
import shutil

# sg.theme_previewer()
sg.theme('DarkGreen7')

move_button = sg.B('Move Files to Root Folder', k='move-files', p=(70,0), s=(23,3))
layout = [  [sg.T('Select folder:', p=(40,20), s=(40,2)), sg.FolderBrowse(k='input-folder', p=((0,20),30), s=(15,2))], 
            [move_button, sg.B('Exit', p=(40,30), s=(20,3))]  ]

window = sg.Window('Move Files to Root Folder', layout, keep_on_top=True, grab_anywhere=True)

while True:
    event, values = window.read()
    basepath = values['input-folder']
    print(basepath)
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if values['input-folder']=='':
        sg.popup('Please select a folder first.', keep_on_top=True)
    elif event=='move-files':
        # Traverse through the directory tree using os.walk
        for root, directories, files in os.walk(basepath):
            for curr_dir in directories:
                # Iterate through files in each directory
                for file in os.listdir(Path(root, curr_dir)):
                    file_curr_path = Path(root, curr_dir, file)
                    file_dest_path = Path(root, file)
                    try:
                        shutil.move(file_curr_path, file_dest_path)
                    except Exception as e:
                        error_info = traceback.format_exc()
                        sg.popup(f'Got an error while renaming {file}:\n{error_info}', keep_on_top=True)
                        # Print the error details to the console for logging or debugging
                        print(f'Got an error while renaming {file}:\n{error_info}')
        sg.popup('All files have been moved to the root folder.', keep_on_top=True)
                        