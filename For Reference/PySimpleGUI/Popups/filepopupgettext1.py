import PySimpleGUI as psg
import time

psg.theme('darkamber')
layout = [    [psg.Text('Inside Text\n2nd Line')],[psg.Button('Popup to get your name')]]

Window = psg.Window('Hi AU, This is a GUI Program!' ,layout)
Window.read()

while True:
    event, values = Window.read()
    if event in (psg.WIN_CLOSED, 'Cancel'):
        break
    elif event=='Popup to get your name':
        psg.popup_get_text('Please enter your name: ',keyword='-name-')
        name = '-name-'
        print(f'Your entered name is {name}')
        break


