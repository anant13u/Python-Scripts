import moviepy
import PySimpleGUI as sg
import subprocess
from pathlib import Path

sg.theme('Reddit')
# sg.theme_previewer()


layout = [  [sg.T('Select Video'), sg.FileBrowse(key='video_file')],
            [sg.T('Start Time'), sg.I('',s=(15,2))],
            [sg.T('End Time'), sg.I('',s=(15,2))]  ]
            
Window = sg.Window('Trim Videos', layout)
