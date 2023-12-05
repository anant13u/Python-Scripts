import os
import PySimpleGUI as sg
from pathlib import Path

sg.theme("DarkTeal2")

sz= size=(20,2)

def mains():
    layout = [  [sg.Text('Please select the folder where you want to rename the files',size=(45,2), pad=(20,(30,10))), sg.FolderBrowse(key='-IN-',size=(15,2),pad=((30,20),10))],
                [sg.Text("Current File's Name:",pad=(20,17)),sg.T('',key='old-filename',pad=((65,0),15))],
                [sg.Text('Please enter the new name:',pad=(20,20)),sg.Input('',key='new-filename',size=(45,1),pad=(20,15))],
                [sg.B('Get Files List',size=(13,2),pad=(50,20)),sg.B('Begin',key='rename-button',size=(10,2),pad=(30,20)),sg.B('Exit',size=(10,2),pad=((50,70),15))]    ]

    Window = sg.Window('Mass File Renamer by AU',layout,keep_on_top=True)
    
    while True:
        event, values = Window.read()
        basepath = values['-IN-']
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event == 'Get Files List':
            if values['-IN-']=='':
                sg.popup('Please select a folder to perform operations in.',keep_on_top=True)
            else:
                sg.popup_scrolled('\n'.join(os.listdir(basepath)),title='List of Files')
        elif event=='rename-button':
            if values['-IN-']=='':
                sg.popup('Please select a folder to perform operations in.',keep_on_top=True)
            else:
                # basepath = values['-IN-']
                open(basepath,'r')
                for filename in os.listdir(basepath):
                    file_rename(Window, basepath, filename)
                Window.close()
                whats_next()

def file_rename(Window, basepath, filename):
    Window['old-filename'].update(filename)
    Window['new-filename'].update(filename)
    Window['rename-button'].update('Rename')
    # Window['-IN-'].update('Change Folder')
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        exit()
    elif event == 'Get Files List':
        # if values['-IN-']=='':
        #     sg.popup('Please select a folder to perform operations in.',keep_on_top=True)
        # else:
        sg.popup_scrolled('\n'.join(os.listdir(basepath)),title='List of Files')
        file_rename(Window, basepath, filename)
    new_name = values['new-filename']
    if new_name!=filename:
        if not Path(new_name).suffix == Path(filename).suffix:
            sg.popup('Extension of file can not be changed.',keep_on_top=True)
            file_rename(Window, basepath, filename)
        else:
            # print(Path(new_name).suffix)
            old_path = os.path.join(basepath, filename)
            new_path = os.path.join(basepath, new_name)
            os.rename(old_path, new_path)
    

# changes_list=[]


def whats_next():
    next_step = sg.popup_yes_no('Renaming is complete with this folder, do you want to rename files from another folder?',title='Renaming Completed!',keep_on_top=True,modal=True)
    if next_step == 'Yes':
        mains()
        print('Renaming done!')
    # else:
    #     print('Bye')

mains()
                


# C:/Users/AU/Desktop/Python/Test
# test1 - Copy (4)