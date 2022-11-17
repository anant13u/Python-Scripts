import webbrowser, PySimpleGUI as sg
sg.theme('darkamber')
helv=('Calibri',11)
from pytube import YouTube
from pytube.extract import video_id
layout = [  [sg.T(' ')],
            [sg.T(' '),sg.T('Please enter the URL for the YouTube video below:', font=helv)],
            [sg.T(' ')],
            [sg.T(' '),sg.InputText(size=(50,2))],
            # [sg.InputText(size=(15,10))],
            [sg.T(' ')],[sg.T(' '),sg.Ok('Fetch Video Details', font=helv, size=(17,2)),sg.T('  '),sg.Cancel(font=helv,size=(17,2))]]

Window = sg.Window('YouTube Video Downloader by AU', layout, size=(370,220))

while True:
    event, values = Window.read()
    url = values[0]
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif url=='':
        sg.popup('Please enter a valid YouTube Video URL!')
        # Window.read()
    else:
        yt = YouTube(url)   #.streams #.first().download()
        yt.streams.filter(file_extension='mp4') # .first().download()
        stream = yt.streams.get_by_itag(22)
        nm = stream.title
    # sg.popup('Your video is ' + nm)
        break
# print('\n Your video is ' + nm)
# ans = input(' Do you wish to download the video? Y/N : ')

layout = [  [sg.T(),sg.T(f'Your video is {nm}')],[sg.T()],
            [sg.Ok('Download Video'),sg.Cancel()]]

Window = sg.Window('YouTube Video Downloader',layout)

while True:
    event, values = Window.read()
    if event=='Download Video':
        sg.popup_get_text(title='Please enter the path where you wish to download the video', key='-DLPATH-')
        dlpath = values['-DLPATH-']
        if dlpath is None:
            stream.download('C:/Users/AU/Downloads')
            sg.popup(f'Your video {nm} has been downloaded and saved at - C:/Users/AU/Downloads')
            webbrowser.open('C:/Users/AU/Downloads') #This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
            # webbrowser.open_new_tab(url) # Use this line if you also want to open the Youtube video in the default browser.
            # Documentation for webbrowser module - https://docs.python.org/3/library/webbrowser.html
        else:
            stream.download(dlpath)
            sg.popup(f'Your video {nm} has been downloaded and saved at - {dlpath}')
            webbrowser.open('-DLPATH-') #This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
    else:
        sg.popup('Video has not been downloaded')
    break
# except:
#     print("Some error occured, please debug in an IDE")





# try:
#     if ans == 'Y' or ans == 'y':
#         stream.download('C:/Users/AU/Downloads')
#         print('\n Your video '+ nm +' has been downloaded and saved at - C:/Users/AU/Downloads')
#         webbrowser.open('C:/Users/AU/Downloads') #This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
#         # webbrowser.open_new_tab(url) # Use this line if you also want to open the Youtube video in the default browser.
#         # Documentation for webbrowser module - https://docs.python.org/3/library/webbrowser.html
#     else:
#         print('\n Video has not been downloaded')
# except:
#     print("Some error occured, please debug in an IDE")


# Local path for Pytube:
# C:\Users\AU\AppData\Local\Programs\Python\Python39\Lib\site-packages\pytube

# yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
# Use this example URL - http://youtube.com/watch?v=9bZkp7q19f0 (Gangnam Styles 8-) )
# https://www.youtube.com/watch?v=4KTvjFGgGkk (Thor: The Dark World Official Trailer #2 (2013) - Chris Hemsworth Movie HD)


# Solution for the error (pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W):
# https://stackoverflow.com/questions/70776558/pytube-exceptions-regexmatcherror-init-could-not-find-match-for-w-w and
# https://github.com/pytube/pytube/issues/1199

# Solution for the error (AttributeError: 'NoneType' object has no attribute 'span'):
# https://trustsu.com/python/attributeerror-nonetype-object-has-no-attribute-span/

# Also, make sure that you are on the latest version of pytube by installing from the source (Only works if you have Git installed on your system)
# python -m pip install git+https://github.com/pytube/pytube
