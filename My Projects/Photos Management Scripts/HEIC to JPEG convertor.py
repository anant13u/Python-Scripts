# Import the required libraries
from pillow_heif import register_heif_opener
from PIL import Image
from pathlib import Path
import FreeSimpleGUI as sg
import os
import traceback

# sg.theme_previewer()
sg.theme('DarkGreen7')
layout = [  [sg.T('Select folder:',pad=((30,15),20),s=(40,2)),sg.FolderBrowse(k='input-folder',pad=((0,20),20),s=(15,2))],
            [sg.B('Convert',pad=(70,0),s=(20,2)), sg.B('Exit',pad=((0,60),20),s=(20,2))]    ]

window=sg.Window('Convert HEIC to JPEG', layout, keep_on_top=True,grab_anywhere=True)

# Register the HEIF opener with the PIL library
register_heif_opener()

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if values['input-folder']=='':
        sg.popup('Please select a folder first.')
    else:
        # Get the base path from the user
        basepath = values['input-folder']
        print(basepath)
        # Extract the current folder name from the base path
        curr_folder = os.path.basename(basepath)
        # Create paths for various folders using the current folder name
        heic_folder_path = os.path.join(basepath, f'HEIC to JPEG ({curr_folder})')
        for file in os.listdir(basepath):
            # Create the full path to the current file
            curr_file_path = os.path.join(basepath, file)
            # Get the size of the file in megabytes
            file_size = os.path.getsize(curr_file_path) / (1024 * 1024)
            # Check if the current path points to a file and if the file has a .heic extension (case-insensitive)
            if Path(curr_file_path).is_file() and Path(curr_file_path).suffix.lower() == '.heic':
                # Create the HEIC folder if it doesn't exist
                if not os.path.exists(heic_folder_path):
                    os.mkdir(heic_folder_path)
                # Open the HEIC image using the Image class from the PIL library
                image = Image.open(curr_file_path)
                # Construct the path for the JPEG output file by replacing '.HEIC' with '.jpg'
                jpeg_path = os.path.join(heic_folder_path, f'{file}'.replace('.HEIC', '.JPG'))
                # Save the opened image as a JPEG file
                image.save(jpeg_path, format='JPEG')

                new_file_path=os.path.join(heic_folder_path,file)
                os.rename(curr_file_path,new_file_path)

        sg.popup('Conversion from HEIC to JPED done.')
