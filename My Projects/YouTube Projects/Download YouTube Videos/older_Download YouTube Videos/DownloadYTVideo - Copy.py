import webbrowser
from pytube import YouTube
# from pytube.extract import video_id
url = input('\n Please enter the YouTube video URL: ')
yt = YouTube(url)   #.streams #.first().download()
# print('Captions available: ', yt.captions())
# en_caption = yt.captions.all
# en_caption_convert_to_srt = en_caption.
# print(en_caption_convert_to_srt)

yt.streams.filter(file_extension='mp4') # .first().download()
stream = yt.streams.get_by_itag(22)
# stream = yt.streams#.first()

nm = stream.title
print('\n Your video is ' + nm)
ans = input(' Do you wish to download the video? Y/N : ')

try:
    if ans in ('Y', 'y'):
        stream.download('C:/Users/AU/Downloads')
        print('\n Your video '+ nm +' has been downloaded and saved at - C:/Users/AU/Downloads')
        webbrowser.open('C:/Users/AU/Downloads') #This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
        # webbrowser.open_new_tab(url) # Use this line if you also want to open the Youtube video in the default browser.
        # Documentation for webbrowser module - https://docs.python.org/3/library/webbrowser.html
    else:
        print('\n Video will not be downloaded')
except:
    print("Some error occured, please debug in an IDE")
