import moviepy.editor as mp
import PySimpleGUI as sg
import subprocess
from pathlib import Path
import os

sg.theme('Reddit')
# sg.theme_previewer()


layout = [  [sg.T('Select Video', s=(35,2), pad=(30,20)), sg.FileBrowse(key='video_file', s=(15,2), pad=(30,20))],
            [sg.T('Start Time'), sg.I('', key = 'start_time', s=(15,2))],
            [sg.T('End Time'), sg.I('', key = 'end_time', s=(15,2))],
            [sg.B('Trim Video', s=(15,2)), sg.B('Exit', s=(15,2))]  ]
            
Window = sg.Window('Trim Videos', layout)

def time_to_seconds(time_str):
    # Split the time string into hours, minutes, and seconds
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    # Convert the time to seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

while True:
    event, values = Window.read()
    videoFile = values['video_file']
    # print(videoFile)
    # print(os.path.basename(videoFile).split('.')[0])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['video_file']=='':
        sg.popup('Please select a video to perform operations on.')
    elif values['start_time'] == '' or values['end_time']=='':
        sg.popup('Please enter start and end time for trimming the video.')
    elif event == 'Trim Video':
        filename = os.path.basename(videoFile).split('.')[0]
        startTime = time_to_seconds(values['start_time'])
        endTime = time_to_seconds(values['end_time'])
        ourClip = mp.VideoFileClip(videoFile)
        trimmedClip = ourClip.subclip(startTime, endTime)
        trimmedClip.write_videofile(videoFile.replace(filename, f'{filename}_{startTime}_{endTime}'), codec='libx264')

