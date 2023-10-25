# Python code to convert video to audio

import PySimpleGUI as sg
import moviepy.editor as mp # Before this the moviepy module needs to be installed using PIP

sg.theme('Reddit')
sg.set_options(font=("Helvetica", 11))

layout = [[sg.FileBrowse('Select Video',pad=(20,20)), sg.B('Convert to Audio',pad=(20,20)), sg.B('Exit',pad=(20,20))]]

Window = sg.Window('Video -> Audio by AU', layout, grab_anywhere=True, keep_on_top=True)

while True:
    event, values = Window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

# Insert Local Video File Path 
# pth =  input('\nPlease enter the path of the video along with the extension which you wish to convert: ')
# pth = pth.replace('"','')
# clip = mp.VideoFileClip(pth)
  
# newfile = pth.replace('.mp4','.mp3') # Here 'newfile' will the complete path for the newly created audio file.

# Insert Local Audio File Path
# clip.audio.write_audiofile(newfile)

# "C:/Users/AU/Videos/InfraSound - Starlight   Epic Powerful Hybrid Orchestral Music.mp4"
