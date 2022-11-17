import webbrowser
from pytube import YouTube
from pytube.extract import video_id
url = input('\n Please enter the YouTube video URL: ')
yt = YouTube(url)   #.streams #.first().download()
yt.streams.filter(file_extension='mp4') # .first().download()
stream = yt.streams.get_by_itag(22)
# stream = yt.streams#.first()

video_name = stream.title
print(f'''\n Your video is: {video_name}
 Length of the video is {yt.length//60} minutes and {yt.length%60} seconds.
 Channel name is: {yt.author}
 Video Description: {yt.description}''')

# yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
# Use this example URL - http://youtube.com/watch?v=9bZkp7q19f0 (Gangnam Styles 8-) )
# https://www.youtube.com/watch?v=4KTvjFGgGkk (Thor: The Dark World Official Trailer #2 (2013) - Chris Hemsworth Movie HD)

# Solution for the error (pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W):
# https://stackoverflow.com/questions/70776558/pytube-exceptions-regexmatcherror-init-could-not-find-match-for-w-w and
# https://github.com/pytube/pytube/issues/1199
