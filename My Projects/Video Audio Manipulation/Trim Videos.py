import moviepy.editor as mp
import PySimpleGUI as sg
import subprocess
from pathlib import Path

sg.theme('Reddit')
# sg.theme_previewer()


layout = [  [sg.T('Select Video', s=(35,2), pad=(30,20)), sg.FileBrowse(key='video_file', s=(15,2), pad=(30,20))],
            [sg.T('Start Time'), sg.I('', key = 'start_time', s=(15,2))],
            [sg.T('End Time'), sg.I('', key = 'end_time', s=(15,2))],
            [sg.B('Trim Video', s=(15,2)), sg.B('Exit', s=(15,2))]  ]
            
Window = sg.Window('Trim Videos', layout)

while True:
    event, values = Window.read()
    videoFile = Path(values['video_file'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['video_file']=='':
        sg.popup('Please select a video to perform operations on.')
    elif values['start_time'] == '' or values['end_time']=='':
        sg.popup('Please enter start and end time for trimming the video.')

    elif event == 'Trim Video':
        ourClip = mp.VideoFileClip(videoFile)
        trimmedClip = ourClip.subclip

