import pyautogui as pg
import PySimpleGUI as sg
import time

# sg.theme_previewer()
sg.theme('lightbrown3')
# pg.FAILSAFE = False

layout = [  [sg.B('Start', s=(25,4), p=(40,30)), sg.B('Exit', s=(25,4), p=(40,30))]  ]
Window = sg.Window('Cursor Mover', layout, keep_on_top=True, grab_anywhere=True)

while True:
    event, values = Window.read()
    if event in ('Exit', sg.WIN_CLOSED):
        break
    elif event == 'Start':
        # pg.moveTo(32,32)
        while True:
            pg.moveRel(-50,0)
            time.sleep(0.5)
            pg.moveRel(0,-50)
            time.sleep(0.5)
            pg.moveRel(50,0)
            time.sleep(0.5)
            pg.moveRel(0,50)
            time.sleep(0.5)
