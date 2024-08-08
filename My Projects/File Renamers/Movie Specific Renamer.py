import os
from pathlib import Path
import PySimpleGUI as sg
import traceback

# sg.theme_previewer()
sg.theme('DarkGreen7')

rename_button = sg.B('Rename Movies as\nper Folder Name', k='-rename_movies-', pad=((110,40),0), s=(20,3))
layout = [  [sg.T('Select folder:', pad=((50,70),20), s=(40,2)),sg.FolderBrowse(k='input-folder', pad=((0,20),30), s=(15,2))],
            [rename_button, sg.B('Exit', pad=(40,30), s=(15,3))]  ]

window=sg.Window('Rename Movies and Subtitles as per parent folder', layout, keep_on_top=True, grab_anywhere=True)

while True:
    event, values = window.read()
    basepath = values['input-folder']
    print(basepath)
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if values['input-folder']=='':
        sg.popup('Please select a folder first.', keep_on_top=True)
    elif event=='-rename_movies-':
        # Traverse through the directory tree using os.walk
        for root, directories, files in os.walk(basepath):
            for curr_dir in directories:
                # Iterate through files in each directory
                for file in os.listdir(Path(root, curr_dir)):
                    file_ext = Path(file).suffix.lower()
                    file_size = os.path.getsize(Path(root,curr_dir, file))/(1024*1024) # file_size is 5.0469865798950195
                    # Check conditions for renaming:
                    # - Ensure the file's base name is not the same as its parent directory (avoid unnecessary renaming).
                    # - File size should be greater than 50 MB if extension is '.mp4', '.mkv' or '.avi'.
                    # - Or the file is a subtitle file ('.srt').
                    # splitext is used to split the extension from a pathname.
                    if os.path.splitext(file)[0] != curr_dir and ((file_size>50 and file_ext in ('.mp4','.mkv','.avi')) or file_ext=='.srt'):
                        try:
                            new_filename = file.replace(os.path.splitext(file)[0], curr_dir)
                            os.rename(Path(root,curr_dir,file),Path(root,curr_dir, new_filename))
                        except Exception as e:
                            error_info = traceback.format_exc()
                            sg.popup(f'Got an error while renaming {file}:\n{error_info}', keep_on_top=True)
                            print(f'Got an error while renaming {file}:\n{error_info}')


# Adding functionality to create folder for files without folder and move them inside.
