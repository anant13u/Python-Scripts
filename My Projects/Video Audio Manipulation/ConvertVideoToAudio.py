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

# Define the layout of the GUI
layout = [  [sg.FileBrowse('Select Video',key='input-video',pad=(30,20)), sg.B('Convert to Audio'), sg.B('Exit',pad=(30,20))],
            [sg.T(key='file_display', pad=10)]  ]

# Create the PySimpleGUI window
Window = sg.Window('Video -> Audio by AU', layout, grab_anywhere=True, keep_on_top=True)


# Main event loop
while True:
    event, values = Window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event=='Convert to Audio':
        try:
            inputVideo = values['input-video']
            if Path(inputVideo).suffix.lower() not in valid_video_extensions:
                sg.popup_error(f'The selected file has {Path(inputVideo).suffix.lower()} extension. \nPlease select a valid video file (e.g., .mp4, .avi, .mkv)', keep_on_top=True)
                continue
            Window['file_display'].update(inputVideo)
            outputFolder = os.path.dirname(inputVideo)
            print(f'Selected file name is {os.path.basename(inputVideo)}')
            outputAudio = inputVideo.replace('.mp4', '.mp3')
            # print(our_clip)
            our_clip=mp.VideoFileClip(inputVideo)
            our_clip.audio.write_audiofile(outputAudio, codec='mp3')
            sg.popup('Conversion successful!', f'Audio saved as {outputAudio}')
            if subprocess.os.name == 'nt':  # Check if the platform is Windows
                subprocess.Popen(f'explorer {outputFolder}')
                # print(subprocess.Popen(r'explorer outputFolder'))
            else:  # For non-Windows platforms (e.g., Linux, macOS)
                subprocess.Popen(['xdg-open', outputFolder])
        except FileNotFoundError as e:
            sg.popup_error(f'File not found: {e}', keep_on_top=True)
            print(e)
        except Exception as e:
            sg.popup_error(f'Error: {e}',keep_on_top=True)
            print(e)

 

# /home/anant/new
# "C:/Users/AU/Videos/InfraSound - Starlight   Epic Powerful Hybrid Orchestral Music.mp4"
