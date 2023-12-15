import os
from pathlib import Path
import PySimpleGUI as sg

sg.theme('DarkAmber')
sz= size=(50,3)

layout = [  [sg.Text('Please select the folder where you want to manage the Photos and other media files',s=(65,2), pad=(20,20))], 
            [sg.FolderBrowse('Select Folder',key='-IN-',s=(15,2), pad=((20,40),0)),sg.T('',s=(50,3))],
            [sg.Button('Manage',size=(15,2), pad=(130,20)),sg.Button('Exit',size=(15,2))]   ]

Window = sg.Window('Photos Manager by AU', layout, keep_on_top=True)

def managePhotos():
    # Extract the current folder name from the base path
    curr_folder = os.path.basename(base_path)

    # Create paths for the edited folder and log file.
    edited_folder_path = os.path.join(base_path,f'Edited Photos and Videos ({curr_folder})')
    edit_log_path = os.path.join(edited_folder_path,'Original and Edited Photos and Videos log.txt')

    moved_pairs_list = ['Below is the list of moved pairs of media:\n']
    error_list = ['Below are the errors encountered:\n']

    # Create paths for various folders using the current folder name
    live_folder_path = os.path.join(base_path, f'Probable Live Photos ({curr_folder})')
    misc_folder_path = os.path.join(base_path, f'Miscellaneous ({curr_folder})')
    aae_folder_path = os.path.join(misc_folder_path, f'AAE Files ({curr_folder})')
    png_folder_path = os.path.join(misc_folder_path, f'Screenshots and other PNG Files ({curr_folder})')

    entries = os.listdir(base_path)
    # print(entries)

    for file in entries:
        curr_file_path = os.path.join(base_path,file) # curr_file_path is C:\Users\Anant\Documents\Test Folder\New folder\IMG_1109.MOV
        if Path(curr_file_path).is_file():
            file_size = os.path.getsize(curr_file_path)/(1024*1024) # file_size is 5.0469865798950195
            file_ext = Path(curr_file_path).suffix # file_ext is .MOV
            filename = file.split('.')[0] # filename is IMG_1109

            if file_ext.lower()=='.mov' and file_size<7:
            # if file_ext=='.mov' and 1<file_size<7:
                if not os.path.exists(live_folder_path):
                    os.mkdir(live_folder_path)
                new_file_path=os.path.join(live_folder_path,file) # new_file_path is C:\Users\Anant\Documents\Test Folder\New folder\Probable Live Photos (New folder)\IMG_1109.MOV
                try:
                    os.rename(curr_file_path,new_file_path)
                    # with open(os.path.join(live_folder_path,'Probable Live Photos.txt'),'a+') as curr_log:
                    #     curr_log.write(f'\nMoved file - "{file}". Size: {round(file_size,2)} MB.')
                except Exception as e:
                    new_file_path=os.path.join(live_folder_path,f'{filename} (2){file_ext}') # new_file_path is C:\Users\Anant\Documents\Test Folder\New folder\Probable Live Photos (New folder)\IMG_1109 (2).MOV
                    os.rename(curr_file_path,new_file_path)
                    # with open(os.path.join(live_folder_path,'Probable Live Photos.txt'),'a+') as curr_log:
                    #     curr_log.write(f'\nMoved file - "{filename} (2){file_ext}". Size: {round(file_size,2)} MB.')
                    print(f"An error occurred: {e}")

            elif file_ext.lower()=='.aae':
                if not os.path.exists(aae_folder_path):
                    if not os.path.exists(misc_folder_path):
                        os.mkdir(misc_folder_path)
                    os.mkdir(aae_folder_path)
                new_file_path=os.path.join(aae_folder_path,file)
                try:
                    os.rename(curr_file_path,new_file_path)
                    # with open(os.path.join(aae_folder_path,'AAE Files.txt'),'a+') as curr_log:
                    #     curr_log.write(f'Moved AAE file - {file}.\n')
                except FileExistsError as e:
                    print(f"File '{file}' already exists in the destination. Skipping.")
                except Exception as e:
                    print(f"An error occurred: {e}")

            elif file_ext.lower()=='.png':
            # print(f'{file} is an AAE file.')
                if not os.path.exists(png_folder_path):
                    if not os.path.exists(misc_folder_path):
                        os.mkdir(misc_folder_path)
                    os.mkdir(png_folder_path)
                new_file_path=os.path.join(png_folder_path,file)
                try:
                    os.rename(curr_file_path,new_file_path)
                    # with open(os.path.join(png_folder_path,'PNG Files.txt'),'a+') as curr_log:
                    #     curr_log.write(f'Moved PNG file - {file}.\n')

                except Exception as e:
                    new_file_path=os.path.join(png_folder_path,f'{filename} (2){file_ext}')
                    os.rename(curr_file_path,new_file_path)
                    # with open(os.path.join(png_folder_path,'PNG Files.txt'),'a+') as curr_log:
                    #     curr_log.write(f'Moved PNG file - {filename} (2){file_ext}.\n')
                    print(f"An error occurred: {e}")

            elif 0<file_size<0.7 or file_ext.lower()=='.mp4' or file_ext.lower()=='.gif':
            # elif 0<file_size<1 or (file_ext=='.mp4' and 1<file_size<7):
                # print(f'{file} - file or not status: {Path(curr_file_path).is_file()}')
                if not os.path.exists(misc_folder_path):
                    os.mkdir(misc_folder_path)
                new_file_path=os.path.join(misc_folder_path,file)
                try:
                    os.rename(curr_file_path,new_file_path)
                except Exception as e:
                    new_file_path=os.path.join(misc_folder_path,f'{filename} (2){file_ext}')
                    os.rename(curr_file_path,new_file_path)
                    print(f"An error occurred: {e}")

            elif file.startswith('IMG_E'): # Checking if the entry starts with 'IMG_E'.
                # Create the edited folder if it doesn't exist.
                curr_file_path = os.path.join(base_path,file) # curr_file_path is C:\Users\Anant\Documents\Test Folder\New folder\IMG_1109.MOV
                original_file_name=file.replace('_E','_') # Create the name of the original file and its path.
                original_file_path = os.path.join(base_path,original_file_name)
                if os.path.exists(original_file_path):
                    if not os.path.exists(edited_folder_path):
                        os.mkdir(edited_folder_path)
                    curr_file_new_path=os.path.join(edited_folder_path,file) # Rename the edited file and move it to the edited folder.
                    original_file_new_path=os.path.join(edited_folder_path,original_file_name)
                    try:
                        os.rename(curr_file_path,curr_file_new_path)
                        os.rename(original_file_path, original_file_new_path)
                        # Write a log entry for the moved pair of files.
                        moved_pairs_list.append(f'Moved pair of files - {original_file_name} and {file}.')
                    except Exception as e:
                        # curr_file_new_path=os.path.join(edited_folder_path,f'{filename} (2){file_ext}')
                        # original_file_new_path=os.path.join(edited_folder_path,f"{original_file.split('.')[0]} (2){file_ext}")
                        error_list.append(f'{e}\n')
                        print(f"An error occurred: {e}")


    if os.path.exists(edited_folder_path):
        with open(edit_log_path,'a+') as edit_log:
            edit_log.write("\n".join(moved_pairs_list) + "\n\n\n" + "\n".join(error_list))
    
    sg.popup('All photos and videos from this folder are sorted now.', keep_on_top=True)


while True:
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event=='Manage':
        base_path = values['-IN-']
        if base_path=='':
            sg.popup("Please select a folder.",keep_on_top=True)
        else:
            print(base_path)
            managePhotos()
            # Window['-IN-'].update('')










# F:\Musical World\Music Videos\^ H ^\90's
# H:\Pics\# Timeline #\2022\August 2022\New folder (4)
