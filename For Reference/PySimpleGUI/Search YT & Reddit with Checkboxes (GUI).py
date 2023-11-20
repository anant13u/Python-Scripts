import webbrowser
import PySimpleGUI as sg

sg.set_options(font=("Helvetica", 11))
sg.theme('Reddit')
# sg.theme('Sandy Beach')

layout = [  [sg.T()],
            [sg.T('Enter the search keyword: '), sg.I(key='search_word')],
            [sg.Checkbox('Search in Reddit', key='reddit_check',pad=(0,20)),
            sg.Checkbox('Search in YouTube', key='yt_check'),
            sg.B('Search', size=10, pad=(10,20)), sg.B('Exit', size=10)] ]

search_window = sg.Window('Search in YouTube and Reddit!', layout, keep_on_top=True, grab_anywhere=True, margins=(20,5),return_keyboard_events=True)

while True:
    event, values = search_window.read()
    search_keyword = values['search_word']
    # Checking if the event is either the window being closed, the button named 'Exit' being clicked, or the Escape key being pressed.
    if event in (sg.WIN_CLOSED, 'Exit', 'Escape:27'):
        break
    elif values['search_word'] == '':
        sg.popup('Search Keyword cannot be blank!', title='Blank Keyword!', keep_on_top=True)
        # sg.Window('Continue?', [[sg.T('Do you want to continue?')], [
        #           sg.Yes(s=10), sg.No(s=10)]], disable_close=True).read(close=True)
    elif event=='Search':
        if values['reddit_check'] == True and values['yt_check'] == True:
            webbrowser.open(f'https://www.reddit.com/search/?q={search_keyword}')
            webbrowser.open(f'https://www.youtube.com/results?search_query={search_keyword}')
        elif values['reddit_check'] == True:
            webbrowser.open(f'https://www.reddit.com/search/?q={search_keyword}')
        elif values['yt_check'] == True:
            webbrowser.open(f'https://www.youtube.com/results?search_query={search_keyword}')
        
    # search_window.close()
