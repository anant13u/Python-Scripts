import PySimpleGUI as sg
import webbrowser as wb

sg.theme('DarkAmber')

layout = [  [sg.T('Enter the search keyword here ->'), sg.InputText(key='-search_text-', size=(50,25))],
            [sg.T()],
            [sg.T(' '*9),sg.B('Search in Reddit Forums',size=(20,2)),sg.T(' '*18), sg.B('Search in YouTube',size=(20,2))]    ]

Window = sg.Window('Search in Reddit or YouTube', layout, margins=(40,50))

def search_further():
    while True:
        event, values = sg.Window('What to do Next',
                                  [  [sg.T('Do you wish to search further?')],
                                     [sg.B('Yes'),sg.B('No')]    ]).read(close=True) # close=True closes the Window after getting the input in form of Yes or No
        if event=='Yes':
            search_ytred()
        break

def search_ytred():
    while True:
        event, values = Window.read()
        search_text = values['-search_text-']
        if event in [sg.WIN_CLOSED, 'Cancel']:
            break
        if search_text in ('', None):
            sg.popup('You need to enter a keyword to search')
        elif event=='Search in Reddit Forums' and search_text!='':
            # wb.open_new_tab(f'https://www.google.com/search?q=site:reddit.com {search_text}')
            wb.open_new_tab(f'https://www.reddit.com/search/?q={search_text}')
            search_further()
            break
        elif event=='Search in YouTube' and search_text!='':
            wb.open_new_tab(f'https://www.youtube.com/results?search_query={search_text}')
            search_further()
            break

search_ytred()
