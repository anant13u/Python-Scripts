# Python code to convert video to audio

import PySimpleGUI as sg
from pathlib import Path
import os
import time
import subprocess
import moviepy.editor as mp # Before this the moviepy module needs to be installed using PIP

valid_video_extensions = ['.mp4', '.avi', '.mkv']

sg.theme('darkgreen7')
sg.set_options(font=("Helvetica", 11))

fileBrowseButton = sg.FileBrowse(key='input-video', size=(15,2), pad=((20,40),30))
rotate90radio = sg.Radio('Rotate 90 degrees counter-clockwise', 'rotate_group', k='-rotate90-', p=(100,20))
rotate180radio = sg.Radio('Rotate 180 degrees', 'rotate_group', default=True, k='-rotate180-', p=(100,0))
rotate270radio = sg.Radio('Rotate 90 degrees clockwise', 'rotate_group', k='-rotate270-', p=(100,20))

# Define the layout of the GUI
layout = [  [sg.T('Select Video', key='file_display', size=(25,2), pad=(30,10)), fileBrowseButton],
            [rotate90radio],
            [rotate180radio],
            [rotate270radio],
            [sg.B('Rotate Video', size=(15,2), pad=((70,30),30)), sg.B('Exit', size=(15,2), pad=((30,40),30))]  ]

# Create the PySimpleGUI window
Window = sg.Window('Video Rotator by AU', layout, grab_anywhere=True, keep_on_top=True)


# Main event loop
while True:
    event, values = Window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event=='Rotate Video':
        try:
            inputVideo = values['input-video']
            # print(inputVideo)
            videoName = os.path.splitext(inputVideo)[0]
            videoExtension = os.path.splitext(inputVideo)[1]
            if Path(inputVideo).suffix.lower() not in valid_video_extensions:
                sg.popup_error(f'The selected file has {Path(inputVideo).suffix.lower()} extension. \nPlease select a valid video file (e.g., .mp4, .avi, .mkv)', keep_on_top=True)
                continue
            Window['file_display'].update(inputVideo)
            outputFolder = os.path.dirname(inputVideo)
            # print(outputFolder)
            # print(f'Selected file name is {os.path.basename(inputVideo)}')
            # print(our_clip)
            our_clip = mp.VideoFileClip(inputVideo)
            if values['-rotate90-']:
                rotationValue = 90
                our_clip = our_clip.rotate(90)
            elif values['-rotate180-']:
                rotationValue = 180
                our_clip = our_clip.rotate(180)
            else:
                rotationValue = 270
                our_clip = our_clip.rotate(270)
            our_clip.write_videofile(f'{videoName}_rotated_{rotationValue}{videoExtension}')
            subprocess.Popen(f'explorer {outputFolder}')
        except FileNotFoundError as e:
            sg.popup_error(f'File not found: {e}', keep_on_top=True)
            print(e)
        except Exception as e:
            sg.popup_error(f'Error: {e}',keep_on_top=True)
            print(e)

 

# /home/anant/new
# "C:/Users/AU/Videos/InfraSound - Starlight   Epic Powerful Hybrid Orchestral Music.mp4"
