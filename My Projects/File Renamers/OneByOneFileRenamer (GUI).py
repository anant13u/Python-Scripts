import os
import PySimpleGUI as sg
from pathlib import Path

sg.theme("DarkTeal2")

sz= size=(20,2)

def mains():
    folderBrowseText = sg.Text('Please select the folder where you want to rename the files:',size=(30,2), pad=(20,(30,10)))
    folderBrowseButton = sg.FolderBrowse(key='-IN-',size=(15,2),pad=((30,20),10))
    layout = [  [folderBrowseText, folderBrowseButton],
                [sg.B('Proceed',key='proceed-button',size=(10,2),pad=(90,30)), sg.B('Exit',size=(10,2),pad=(0,15))] ]

    Window = sg.Window('Mass File Renamer by AU', layout, keep_on_top=True, grab_anywhere=True)
    
    while True:
        event, values = Window.read()
        basepath = values['-IN-']
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            exit()
        elif event=='proceed-button':
            if values['-IN-']=='':
                sg.popup('Please select a folder to perform operations in.',keep_on_top=True)
            else:
                Window.close()
                for filename in os.listdir(basepath):
                    file_rename(basepath, filename)
                mains()


def file_rename(basepath, filename):
    renameButton = sg.B('Rename', size=(10,2), k='rename-button', pad=(60,20))
    rename_layout = [   [sg.T("Current File's Name:",pad=(20,17)),sg.T(filename, key='old-filename',pad=((65,0),15))],
                        [sg.T('Please enter the new name:',pad=(20,20)),sg.I(filename, key='new-filename',size=(45,1),pad=(20,15))],
                        [renameButton, sg.B('Change Folder', size=(13,2)), sg.B('Exit',size=(10,2),pad=(60,20))] ]
    rename_window = sg.Window('Renaming Window', rename_layout, keep_on_top=True, grab_anywhere=True)

    rename_event, rename_values = rename_window.read()

    if rename_event in (sg.WINDOW_CLOSED, 'Exit'):
        exit()
    elif rename_event == 'Change Folder':
        rename_window.close()
        mains()
    elif rename_event == 'rename-button':
        new_name = rename_values['new-filename']
        if new_name!=filename:
            if not Path(new_name).suffix == Path(filename).suffix and Path(basepath, filename).is_file():
                sg.popup('Extension of file can not be changed.',keep_on_top=True)
                rename_window.close()
                file_rename(basepath, filename)
            else:
                old_path = os.path.join(basepath, filename)
                new_path = os.path.join(basepath, new_name)
                os.rename(old_path, new_path)

    rename_window.close()


mains()
                


# C:/Users/AU/Desktop/Python/Test
# test1 - Copy (4)