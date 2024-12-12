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
    # Check if the 'move-files' event is triggered
    elif event=='move-files':
        # Traverse through the directory tree starting from the basepath using os.walk
        for root, directories, files in os.walk(basepath):
                # Iterate through each subdirectory in the current root directory
            for curr_dir in directories:
                # Iterate over each file in the current directory of the root folder
                for file in os.listdir(Path(root, curr_dir)):
                    # Construct the full path of the current file
                    file_curr_path = Path(root, curr_dir, file)
                    # Construct the destination path in the root folder for the file
                    file_dest_path = Path(root, file)
                    # Attempt to move the file from the current path to the destination path
                    try:
                        shutil.move(file_curr_path, file_dest_path)
                    # Handle any exception that might occur during the file move operation
                    except Exception as e:
                        # Capture detailed traceback information for debugging
                        error_info = traceback.format_exc()
                        # Display an error popup to the user with the traceback details
                        sg.popup(f'Got an error while renaming {file}:\n{error_info}', keep_on_top=True)
                        # Print the error details to the console for logging or debugging
                        print(f'Got an error while renaming {file}:\n{error_info}')
        # Display a popup message to inform the user that all files have been successfully moved to the root folder
        sg.popup('All files have been moved to the root folder.', keep_on_top=True)
                        