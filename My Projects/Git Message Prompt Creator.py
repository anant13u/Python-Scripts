import PySimpleGUI as sg
import pyperclip

sg.theme('Reddit')
    
layout = [  [sg.T(' '*30), sg.T('Intital Code'),sg.T(' '*73), sg.T('Current Code')],
            [sg.Multiline(size=(50,40),key='initial-code',do_not_clear=False),sg.Multiline(size=(50,40),key='current-code')],
            # [sg.T()],
            [sg.T(' '*20), sg.B('Create and copy prompt'),sg.T(' '*59), sg.B('Exit')],
            [sg.T()]  ]

Window = sg.Window('Git Commit Message Creator',layout, keep_on_top=True)

while True:
    event, values = Window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event=='Create and copy prompt':
        initialCode = values['initial-code']
        currentCode = values['current-code']
        # sg.popup(initialCode,currentCode)
        prompt = f'I need you to write a Git commit message (preferably in 3-4 lines max) for the code changes made below:\nPrevious code:\n{initialCode}\n\nCurrent Code:\n{currentCode}' 
        pyperclip.copy(prompt)


# On Linux, install xclip, xsel, or wl-clipboard (for "wayland" sessions) via package manager. For example, in Debian:
# sudo apt-get install xclip sudo apt-get install xsel sudo apt-get install wl-clipboard
