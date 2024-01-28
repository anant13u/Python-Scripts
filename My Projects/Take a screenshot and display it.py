import pyautogui
import time
import os
from datetime import datetime
from pathlib import Path
import PySimpleGUI as sg

sg.theme('DarkGreen7')
save_path = Path('C:/Users/Anant/Pictures/Screenshots')

screenshotButton = sg.B('Take Screenshot and display', key='screenshot_button', pad=(30,20), s=(30,2))
padding_changed = (150, 20)

layout = [  [screenshotButton, sg.B('Exit', pad=(30,20), s=(15,2))],
            [sg.Im('', k='image_box')]   ]

Window = sg.Window('Screenshot Window', layout, enable_close_attempted_event=True)


while True:
    event, values = Window.read()
    if event in (sg.WIN_CLOSED, sg.WINDOW_CLOSE_ATTEMPTED_EVENT, 'Exit'):
        if sg.popup_yes_no('Do you really want to go?') == 'Yes':
            break
    elif event == 'screenshot_button':
        try:
            curr_datetime = datetime.now().strftime('%d-%m-%y %H_%M_%S')
            Window.disappear() # Hide the window temporarily to take the screenshot
            screenshot_path = Path(save_path, f'{curr_datetime}.png')
            pyautogui.screenshot(screenshot_path)
            Window['image_box'].update(str(screenshot_path))
            Window.reappear()

        except KeyboardInterrupt:
            print(f'\n\nStopped at {curr_datetime}\n\n')
            break


# curr_date = datetime.now().date().strftime('%d-%m-%y')
# print(curr_date) # 21-01-24
