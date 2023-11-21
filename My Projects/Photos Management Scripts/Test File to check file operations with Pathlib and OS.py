import os
from pathlib import Path
import PySimpleGUI as sg

layout = [
    [sg.Text("Select a file:")],
    [sg.InputText(key="FilePath"), sg.FileBrowse()],
    [sg.Button("OK")]
]

window = sg.Window("File Selection", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "OK":
        source_path = values["FilePath"]
        break

file_name, file_extension = os.path.splitext(os.path.basename(source_path))

file_ext = Path(source_path).suffix # file_ext is .MOV
filename = os.path.basename(source_path).split('.')[0] # filename is IMG_1109

print(file_name)
print(file_extension)

print(file_ext)
print(filename)
