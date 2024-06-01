import pyautogui as pg
import PySimpleGUI as sg
import time

# sg.theme_previewer()
sg.theme('lightbrown3')
# pg.FAILSAFE = False

layout = [  [sg.B('Start', s=(15,3), p=(30,30)), sg.B('Exit', s=(15,3), p=(30,30))]  ]
Window = sg.Window('Cursor Mover', layout, keep_on_top=True, grab_anywhere=True)

while True:
    event, values = Window.read()
    if event in ('Exit', sg.WIN_CLOSED):
        break
    elif event == 'Start':
        # pg.moveTo(32,32)
        while True:
            pg.moveRel(-100,0)
            time.sleep(0.5)
            pg.moveRel(0,-100)
            time.sleep(0.5)
            pg.moveRel(100,0)
            time.sleep(0.5)
            pg.moveRel(0,100)
            time.sleep(0.5)
    elif event=='Stop':
        break