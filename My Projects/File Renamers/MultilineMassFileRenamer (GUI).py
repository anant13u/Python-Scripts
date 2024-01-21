import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime

rename_log = []

sg.theme('Reddit')

selectFolderText = sg.Text('Select Folder',s=(30,2),pad=((60,20),10))
folderBrowse = sg.FolderBrowse(key='-basepath-',s=(15,2),pad=(40,10))

layout = [  [selectFolderText, folderBrowse],
            [sg.B('Generate List',s=(15,2),pad=(80,10)), sg.B('Rename Files',s=(15,2),pad=(80,10)), sg.B('Exit',s=(15,2),pad=(70,10))],
            [sg.Multiline('',key='file_list',s=(70,30),pad=(50,20))]  ]

Window = sg.Window('Generate list of files', layout, keep_on_top=True, grab_anywhere=True)


# Function to rename files based on rename_dict
def rename_files():
    for curr_name, new_name in rename_dict.items():
        curr_path = Path(basepath, curr_name)
        new_path = Path(basepath, new_name)
        try:
            if curr_path.suffix != new_path.suffix and curr_path.is_file():
                sg.popup(f"Extension for {curr_name} can't be changed.", keep_on_top=True)
            elif curr_path != new_path:
                os.rename(curr_path, new_path)
        except Exception as e:
            sg.popup_error(f"Error renaming {curr_name} to {new_name}: {e}")

    # Reset rename_log and update GUI
    rename_log.clear()
    Window['file_list'].update('')


# Main event loop
while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['-basepath-']=='':
        sg.popup('Please select a folder to perform operations in.')
    elif event == 'Generate List':
        # Generate and display list of files in the selected folder
        print(basepath)
        curr_names = os.listdir(basepath)
        Window['file_list'].update('\n'.join(curr_names))
    elif event == 'Rename Files':
        if values['file_list'] == '':
            sg.popup('Please fetch the file list first.')
        else:
            # Get new names from GUI and create rename_dict
            new_names = values['file_list'].split('\n')
            rename_dict = dict(zip(curr_names, new_names))

            # Populate rename_log with renaming information
            for curr_name, new_name in rename_dict.items():
                if curr_name != new_name:
                    rename_log.append(f'{curr_name} -> {new_name}')
            # Check if there are files to be renamed
            if len(rename_log) == 0:
                sg.popup('No files to be renamed.', keep_on_top=True)
            else:
                # If there are multiple files to be renamed, join them with newline for better readability
                if len(rename_log) > 1:
                    rename_log = '\n'.join(rename_log)
                # Ask for final confirmation before proceeding with renaming
                if sg.popup_yes_no(f'Please check new names before renaming:\n{rename_log[0]}', title='Final Check', keep_on_top=True) == 'Yes':
                    rename_files()

            
           
        




# filelist = '\n'.join(filelist)
            
# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)

# Window.disappear()
# Window.reappear()
        


