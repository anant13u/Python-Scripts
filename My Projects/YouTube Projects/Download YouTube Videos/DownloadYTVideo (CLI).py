import webbrowser
from os import startfile
import time
from pytube import YouTube
from pytube.extract import video_id

def geturl():
    url = input('\n Please enter the YouTube video URL: ')
    if url=='':
        print('\n No URL has been entered')
        time.sleep(1)
        geturl()
    elif url.find('https://www.youtube.com/watch?')<0 and url.find('http://www.youtube.com/watch?')<0:
        print('\n Please enter a valid YouTube Video Link')
        time.sleep(1)
        geturl()
    else:
        yt = YouTube(url)   #.streams #.first().download()
        yt.streams.filter(file_extension='mp4') # .first().download()
        stream = yt.streams.get_by_itag(22)
        # stream = yt.streams#.first()
        nm = stream.title
        print(f'\n Your video is {nm}')
        ans = input(' Do you wish to download the video? Y/N : ')
    
        try:
            if ans in ('Y', 'y'):
                stream.download('C:/Users/AU/Downloads')
                print(f'\n Your video "{nm}" has been downloaded and saved at - C:/Users/AU/Downloads')
                webbrowser.open('C:/Users/AU/Downloads') #This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
                newname=nm.replace('#','')
                newname=newname.replace(':','')
                startfile(f'C:/Users/AU/Downloads/{newname}.mp4')
                # webbrowser.open_new_tab(url) # Use this line if you also want to open the Youtube video in the default browser.
                # Documentation for webbrowser module - https://docs.python.org/3/library/webbrowser.html
            else:
                print('\n Video will not be downloaded')
                time.sleep(1)
                print('\n Goodbye!\n')
                time.sleep(1.5)
        except:
            print("Some error occured, please debug in an IDE")

geturl()

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
