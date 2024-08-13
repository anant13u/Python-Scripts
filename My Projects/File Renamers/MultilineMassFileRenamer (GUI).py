import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime

rename_log = []

sg.theme('DarkGrey13')

selectFolderText = sg.Text('Select Folder', s=(80), pad=((290,20),10))
folderBrowse = sg.FolderBrowse(key='-basepath-', s=(15,2), pad=(30,10))

layout = [  [selectFolderText, folderBrowse],
            [sg.B('Generate List',s=(15,2),pad=((350,120),10)), sg.B('Rename Files',s=(15,2),pad=(10,10)), sg.B('Exit', s=(15,2), pad=(120,10))],
            [sg.Multiline('',key='file_list',s=(80,13),pad=(50,20), font=("Bahnschrift", 21))],
            [sg.T('Script Creator: Anant Upadhyay')]  ]

Window = sg.Window('Generate list of files and rename', layout, keep_on_top=True, grab_anywhere=True)


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
            print(f"Error renaming {curr_name} to {new_name}: {e}")
            sg.popup_error(f"Error renaming {curr_name} to {new_name}: {e}", keep_on_top=True)


# Main event loop
while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif values['-basepath-']=='':
        sg.popup('Please select a folder to perform operations in.', keep_on_top=True)
    elif event == 'Generate List':
        # Generate and display list of files in the selected folder
        print(basepath)
        curr_names = os.listdir(basepath)
        # Window['file_list'].update('\n'.join(curr_names), visible=True)
        Window['file_list'].update('\n'.join(curr_names))
    elif event == 'Rename Files':
        if values['file_list'] == '':
            sg.popup('Please generate the file list first.', keep_on_top=True)
        else:
            # Get new names from GUI and create rename_dict
            new_names = values['file_list'].split('\n')
            rename_dict = dict(zip(curr_names, new_names))

            # Populate rename_log with renaming information
            for curr_name, new_name in rename_dict.items():
                if curr_name != new_name:
                    rename_log.append(f'{curr_name}\n{new_name}\n')
            if len(rename_log) == 0: # Check if there are files to be renamed
                sg.popup('No files to be renamed.', keep_on_top=True)
            elif len(rename_log) == 1: # Check if there is exactly one file to be renamed
                # Display a popup with the first renaming operation and ask for final confirmation
                if sg.popup_yes_no(f'Please check new names before renaming:\n{rename_log[0]}', title='Final Check', keep_on_top=True, line_width=200) == 'Yes':
                    rename_files()
            # If there are multiple files to be renamed, join them with newline for better readability
            elif len(rename_log) > 1:
                rename_log = '\n'.join(rename_log)
                popup_layout = [   [sg.Multiline(f'Please check new names before renaming:\n{rename_log}', s=(60,20))],
                                    [sg.B('Yes'), sg.B('No')]  ]
                popup_window = sg.Window('Final Check', popup_layout, keep_on_top=True)
                # Ask for final confirmation before proceeding with renaming
                while True:
                    popup_event, popup_values = popup_window.read()
                    if popup_event in (sg.WINDOW_CLOSED, 'No'):
                        break
                    elif popup_event == 'Yes':
                        rename_files()
                        break
                popup_window.close()
            # Reset rename_log and update GUI
            rename_log = []
            curr_names = os.listdir(basepath)

            Window['file_list'].update('\n'.join(curr_names))



# filelist = '\n'.join(filelist)
            
# current_file_size = round(os.path.getsize(current_file)/(1024*1024), 2)

# Window.disappear()
# Window.reappear()
        

# sg.Multiline('', key='file_list', s=(55,13), p=(50,20), font=("Bahnschrift", 23), visible=False, wrap_lines=False, horizontal_scroll = True)
