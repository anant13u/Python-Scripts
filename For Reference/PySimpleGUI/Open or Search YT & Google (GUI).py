import webbrowser
import PySimpleGUI as sg

sg.theme('Reddit')

layout = [    [sg.T('Search for (Optional):', pad=(10,25)), sg.I(key='search_word', pad=(10,25))],
               [sg.B('Open Google', key='google_button', s=15, pad=(15,0)), sg.B('Open YouTube', key='yt_button', s=15, pad=(20,0)),
                sg.B('Open Reddit', key='reddit_button', s=15, pad=(15,0))],
               [sg.B('Exit', s=12, pad=(186,(20,15)))]   ]

window = sg.Window('Open website from GUI!', layout, keep_on_top=True, return_keyboard_events=True)

while True:
    event, values = window.read()
    if event in ('Exit', sg.WIN_CLOSED, 'Escape:27'):
        break
    if values['search_word'] != '':
        search_keyword = values['search_word']
        window.Element('google_button').update('Search Google')
        window.Element('yt_button').update('Search YouTube')
        window.Element('reddit_button').update('Search Reddit')
        if event == 'google_button':
            webbrowser.open_new_tab(f'https://www.google.com/search?q={search_keyword}')
        elif event == 'yt_button':
            webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={search_keyword}')
        elif event == 'reddit_button':
            webbrowser.open_new_tab(f'https://www.reddit.com/search/?q={search_keyword}')
    else:
        window.Element('google_button').update('Open Google')
        window.Element('yt_button').update('Open YouTube')
        window.Element('reddit_button').update('Open Reddit')
        if event == 'reddit_button':
            webbrowser.open_new_tab('https://reddit.com')
        elif event == 'google_button':
            webbrowser.open_new_tab('https://google.com')
        elif event == 'yt_button':
            webbrowser.open_new_tab('https://youtube.com')
