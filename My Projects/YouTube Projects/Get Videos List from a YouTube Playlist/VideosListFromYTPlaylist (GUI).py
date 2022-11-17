from pytube import Playlist
import time, PySimpleGUI as sg
from pathlib import Path

sg.theme("darkamber")
curr_dir = Path.cwd()
print(curr_dir)

def yo(x):
    time.sleep(x)

layout= [   [sg.T(' '*8)],[sg.T(' '*8),sg.T('Please enter the YouTube playlist URL')],
            [sg.T(' '*8)],
            [sg.Input(key='-URL-')],
            [sg.T(' '*8)],
            [sg.T(' '*6),sg.Button('Fetch Videos list'),sg.T(' '*5),sg.Button('Exit',size=10)],[sg.T(' '*8)]    ]

window = sg.Window('YouTube Playlist by AU', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        sg.popup_auto_close('Goodbye!',auto_close_duration=1)
        break
    elif values['-URL-']=='': #If no URL has been entered.
        sg.popup('URL field cannot be left blank!')
    elif values['-URL-'].find('https://www.youtube.com/playlist?list')<0: # IF an URL is provided not having "https://www.youtube.com/playlist?list" in it.
        # print(str(values['-URL-']).find('https'))
        sg.popup('Please enter a valid Playlist URL!')
    elif event=='Fetch Videos list':
        play_list=Playlist(values['-URL-'])
        lst=[] # Creating a list where we will store the name of all videos one by one.
        playlist_name=play_list.title # Getting the name of the Playlist.
        for link, video in zip(play_list, play_list.videos): # https://stackoverflow.com/questions/16552508/python-loops-for-simultaneous-operation-two-or-possibly-more
            video_name = video.title
            lst.extend((video_name, f'URL - {link}\n'))
        final_list='\n'.join(lst) # Joining all the items in the list with a new line.
        # https://stackoverflow.com/questions/57239909/how-do-i-print-each-element-of-list-in-a-new-line-with-pysimplegui
        # final_list='\n\n'.join([str(i) for i in lst])
        with open(Path.joinpath(curr_dir,f'{playlist_name}.txt'),'w') as playlist_log:
                print(f'\n\n{playlist_name}\n\n{final_list}', file=playlist_log)
        print(final_list)
        sg.popup_scrolled(final_list) # This kind of popup lets us select and copy text.
        sg.popup(final_list,title=f'Videos List from {playlist_name}')
        break




# yo(1)
# input(' Press Enter to Exit!')
# yo(0.5)
# print(' Goodbye!')
# yo(1)
# exit

# Filepath - C:\Users\AU\Desktop\Python\My Projects\YouTube Projects\VideosListFromYTPlaylist (with GUI).py
# https://stackoverflow.com/questions/65698332/how-do-you-get-name-of-every-video-in-a-playlist-from-youtube-in-python-using-py

# Example Playlist - https://www.youtube.com/playlist?list=PLl8dD0doyrvGdGCe9Kkd1gszSyqMbVSL1
# Example Playlist 2 - https://www.youtube.com/playlist?list=PLACWuX8gM_KHueMDmXLJViAcwQvtHTFcT

# To-do:
# GUI with a popup that lists all the Videos in the Playlist.
# GUI which saves down the list of YouTube videos in an Excel spreadsheet.


# for items in play_list:
#     print(items)
# for video in play_list.videos:
#     name = video.title    
#     print(name)