import os
import PySimpleGUI as sg

layout = [[sg.T('Do you really want to go into Hibernation, lol', p=(20,10))],
          [sg.Button('Yepp!'), sg.B('Cancel')]]

Window = sg.Window('Hibernate or Not', layout)

while True:
    event, values = Window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event=='Yepp!':
        # This will make the system go into hibernate mode.
        sg.popup_auto_close('Bye',auto_close_duration=2)
        os.system('shutdown /h')
