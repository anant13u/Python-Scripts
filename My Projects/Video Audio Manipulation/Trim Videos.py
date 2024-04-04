import moviepy
import PySimpleGUI as sg
import subprocess
from pathlib import Path

sg.theme('Reddit')
# sg.theme_previewer()


layout = [  [sg.T('Select Video'), sg.FileBrowse()],
            [sg.B('Generate List',s=(15,2),pad=(30,10)), sg.B('Exit',s=(15,2),pad=(70,10))]  ]
