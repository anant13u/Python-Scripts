from pytube import Playlist
import time

def pl():
    try:
        play_list = Playlist(input('\n Please enter the YouTube playlist URL: \n\n '))
        print(f'\n There are {len(play_list)} videos in this playlist. Here\'s the list: \n')
        for item, video in zip(play_list, play_list.videos): # https://stackoverflow.com/questions/16552508/python-loops-for-simultaneous-operation-two-or-possibly-more
            name = video.title
            print(f' {name} - {item}')
        # [print(f' {video.title} - {video.watch_url}') for video in play_list.videos]
    except NameError:
        print(' Please enter a valid YouTube URL!')
        pl()

pl()

# def yo(x):
#     time.sleep(x)

# yo(1)
# input(' Press Enter to Exit!')
# yo(0.5)
# print(' Goodbye!')
# yo(1)
# exit

# Filepath - C:\Users\AU\Desktop\Python\My Projects\VideosListFromYTPlaylist.py
# https://stackoverflow.com/questions/65698332/how-do-you-get-name-of-every-video-in-a-playlist-from-youtube-in-python-using-py

# Example Playlist - https://www.youtube.com/playlist?list=PLl8dD0doyrvGdGCe9Kkd1gszSyqMbVSL1

# To-do:
# GUI with a popup that lists all the Videos in the Playlist.
# GUI which saves down the list of YouTube videos in an Excel spreadsheet.


# for items in play_list:
#     print(items)
# for video in play_list.videos:
#     name = video.title    
#     print(name)