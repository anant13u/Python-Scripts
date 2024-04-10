import moviepy
import PySimpleGUI as sg
import subprocess
from pathlib import Path

sg.theme('Reddit')
# sg.theme_previewer()


layout = [  [sg.T('Select Video'), sg.FileBrowse(key='video_file')],
            [sg.T('Start Time'), sg.I('', key = 'start_time', s=(15,2))],
            [sg.T('End Time'), sg.I('', key = 'end_time', s=(15,2))]  ]
            
Window = sg.Window('Trim Videos', layout)

while True
    event, values = Window.read()
    videoFile = Path(values['video_file'])
    if event in (sg.WIN_CLOSED, 'Exit')
        break
    elif values['video_file']==''
        sg.popup('Please select a video to perform operations on.')

