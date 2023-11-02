# Python code to convert video to audio

import PySimpleGUI as sg
# from pathlib import Path
import os
import subprocess
import moviepy.editor as mp # Before this the moviepy module needs to be installed using PIP

# sg.theme('Reddit')
sg.theme('darkgreen7')
sg.set_options(font=("Helvetica", 11))

layout = [[sg.FileBrowse('Select Video',key='input-video',pad=20), sg.B('Convert to Audio'), sg.B('Exit',pad=20)]]

Window = sg.Window('Video -> Audio by AU', layout, grab_anywhere=True, keep_on_top=True)

while True:
    event, values = Window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event=='Convert to Audio':
        try:
            inputVideo = values['input-video']
            outputFolder = os.path.dirname(inputVideo)
            print(f'outputFolder is {outputFolder}')
            print(f'Current folder name is {os.path.basename(inputVideo)}')
            outputAudio = inputVideo.replace('.mp4', '.mp3')
            # print(our_clip)
            our_clip=mp.VideoFileClip(inputVideo)
            # our_clip.audio.write_audiofile(outputAudio)
            our_clip.audio.write_audiofile(outputAudio, codec='mp3')
            if subprocess.os.name == 'nt':  # Check if the platform is Windows
                subprocess.Popen(f'explorer {outputFolder}')
                # print(subprocess.Popen(r'explorer outputFolder'))
            else:  # For non-Windows platforms (e.g., Linux, macOS)
                subprocess.Popen(['xdg-open', outputFolder])
        except Exception as e:
            sg.popup_error(f'Error: {e}',keep_on_top=True)
            print(e)


# Insert Local Video File Path 
# pth =  input('\nPlease enter the path of the video along with the extension which you wish to convert: ')
# pth = pth.replace('"','')
# clip = mp.VideoFileClip(pth)
  
# newfile = pth.replace('.mp4','.mp3') # Here 'newfile' will the complete path for the newly created audio file.

# Insert Local Audio File Path
# clip.audio.write_audiofile(newfile)

# "C:/Users/AU/Videos/InfraSound - Starlight   Epic Powerful Hybrid Orchestral Music.mp4"
