from pathlib import Path
import PySimpleGUI as sg
from PIL import Image
from pathlib import Path
import os

entries_list = []

# sg.theme_previewer()
sg.theme('DarkGreen7')
layout = [  [sg.T('Select folder:',pad=((30,15),20),s=(40,2)),sg.FolderBrowse(k='input-folder',pad=((0,20),20),s=(15,2))],
            [sg.B('Convert',pad=(70,0),s=(15,2)), sg.B('Exit',pad=((0,60),20),s=(15,2))]    ]

window=sg.Window('Convert PNG to JPEG', layout, keep_on_top=True,grab_anywhere=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if values['input-folder']=='':
        sg.popup('Please select a folder first.')
    else:
        basepath = values['input-folder']
        print(basepath)
        for curr_image_name in os.listdir(basepath):
            if Path(curr_image_name).suffix.lower()=='.png':
                curr_image_path = os.path.join(basepath,curr_image_name)
                try:
                    img = Image.open(curr_image_path)
                    # Convert to RGB mode if it's not in RGB mode
                    if img.mode != 'RGB':
                        # Convert the image to 'RGB' mode to ensure compatibility with JPEG
                        img = img.convert('RGB')
                    # jpg_path = os.path.join(basepath,image.replace('.PNG','.JPG'))
                    jpg_path = Path(basepath,curr_image_name.replace('.PNG','.JPG'))
                    img.save(jpg_path, 'JPEG')
                    os.remove(curr_image_path)
                except Exception as e:
                    sg.popup(f'Got an error while converting {curr_image_name}:\n{e}')
                    print(f'Got an error while converting {curr_image_name}:\n{e}')

                # moved_pngs_path=Path(basepath,'Moved Original PNG Files')
                # if not os.path.exists(moved_pngs_path):
                #     os.mkdir(moved_pngs_path)
                # os.rename(curr_image_path,os.path.join(moved_pngs_path,curr_image_name))

        sg.popup('Conversion completed.',keep_on_top=True)
        
