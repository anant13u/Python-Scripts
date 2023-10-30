import PySimpleGUI as psg
import time

psg.theme('darkamber')

layout = [ [psg.Text('Please enter your name here: ', size=(30,1)),psg.InputText(size=(30,1))],
           [psg.Text('Please enter your Email Address here: ',size=(30,1)),psg.Input(size=(30,1))],
           [psg.OK(size=(15,1)),psg.Cancel(size=(15,1))] ]

Window = psg.Window('Hi AU, This is a GUI Program!', layout, margins = (80, 80))

while True:             
    event, values = Window.read()
    if event == 'OK':
        if values[0] == "" or values[1] == "":
            psg.popup('Please enter both fields', no_titlebar=True)
        else:
            psg.popup(f' Name is: {values[0]}\n Email Address is: {values[1]}', no_titlebar=True, background_color='black')
    elif event in (psg.WIN_CLOSED, 'Cancel'):
        if values[0] == '' or values[1] == '':
            psg.popup_error('Both fields were not filled in!')
            break
        else:
            psg.popup(f' Name is: {values[0]}\n Email Address is: {values[1]}', no_titlebar=True, background_color='black')
            break

print(f' Name is: {values[0]}\n Email Address is: {values[1]}')
# psg.popup(f' Name is: {values[0]}\n Email Address is: {values[1]}')

# psg.popup_error('Please enter both fields')