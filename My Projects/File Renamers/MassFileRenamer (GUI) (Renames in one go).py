import os
import PySimpleGUI as sg

sg.theme('DarkGrey13')

sz= size=(20, 2)

col1 = sg.Column([[sg.Multiline('', k='files-list', s=(40,15), p=(20,20), font=("Bahnschrift", 23))]], p=0)

generateButton = sg.Button('Generate List', s=(13,2), p=((70,20),30))
renameButton = sg.Button('Rename', s=(13,2), p=(30,30))
col2 = sg.Column([[sg.Text('Select Folder', s=(30,2), p=(20,(35,15))), sg.FolderBrowse(key='-IN-', s=(15,2), p=((40,20),10))], 
            [sg.Text('Please enter the string you want to rename', sz, p=(20,15)), sg.Input('', key='old-string', p=((30,50),10), s=(40,2))], 
            [sg.Text('Please enter the new text', sz, p=(20,15)), sg.Input('', key='new-string', s=(40,2), p=((30,50),10))], 
            [generateButton, renameButton, sg.Button('Exit', s=(13,2), p=(20,15))]])

layout = [[col1, sg.VerticalSeparator(), col2]]

Window = sg.Window('Mass File Renamer by AU', layout, keep_on_top=True, grab_anywhere=True)

changes_list=[]
while True:
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event=='Generate List':
        if values['-IN-']=='':
            sg.popup('Please select a folder to perform operations in.', keep_on_top=True)
        else:
            basepath = values['-IN-']
            entries = os.listdir(basepath)
            Window['files-list'].update('\n'.join(entries))
            # Window['files-list'].update('sdfsdfdfs')
    elif event=='Rename':
        if values['-IN-']=='':
            sg.popup('Please select a folder to perform operations in.', keep_on_top=True)
        elif values['old-string']=='':
            sg.popup('Please enter a string to replace.', keep_on_top=True)
        else:
            basepath = values['-IN-']
            old_string = values['old-string']
            new_string = values['new-string']
            entries = os.listdir(basepath)
            print(basepath)

            for currfilename in entries:
                str_check = currfilename.find(old_string) #With this method we check the presence of a substring within another string. 
                # If the substring is present the method will return the number which denotes the beginning of the substring. 
                # If the substring isn't present, the method will return -1.
                newfilename = currfilename.replace(old_string, new_string)
                if str_check>=0:
                    try:
                        os.rename(os.path.join(basepath, currfilename), os.path.join(basepath, newfilename))
                    except PermissionError as e:
                        print(f'Permission Error: {e}')
                        sg.popup(f'Permission Error: {e}', keep_on_top=True)
                    # Handle the specific case where a file already exists at the destination path
                    except FileExistsError as e:
                        # Print an error message to the console indicating the file already exists
                        print(f'File already exists Error: {e}')
                        sg.popup(f'File already exists Error: {e}', keep_on_top=True)
                    changes_list.append(f'Old filename: {currfilename}\n'
                                        f'New filename: {newfilename}')
                final_list='\n\n'.join(changes_list) # Separating all list items with a new line.
            # if final_list.find(old_string)>1:
            #     sg.popup(f'All files containing the text "{old_string}" are now renamed. Please find the list below:\n\n{final_list}', title='List of changed filenames', line_width=100, grab_anywhere=True, keep_on_top=True)
            # else:
            #     sg.popup(f'No files found with {old_string} in their names.', keep_on_top=True, grab_anywhere=True)
            changes_list=[]
            final_list=''
            entries = os.listdir(basepath)
            Window['files-list'].update('\n'.join(entries))
            # break

#     if str>=0:
#         print('The file: ' + entry + ' contains ' + txt2replace + ' in its name, and will be renamed.')
#         os.rename(pth + '/' + entry , pth + '/' + newfilename)
#         print('Old file name was: ' + entry)
#         print('New file name is: ' + newfilename + '\n')
#     else:
#         print('The file: ' + entry + ' does not contain ' + txt2replace + ' in its name. File will not be renamed.\n')


# C:/Users/AU/Desktop/Python/Test
# test1 - Copy (4)
            