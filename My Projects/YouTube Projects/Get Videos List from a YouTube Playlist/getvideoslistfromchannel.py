from pytube import Playlist, YouTube
from pytube.extract import video_id
url = input('\n Please enter the YouTube playlist URL: \n ')

try:
    video_links = Playlist(url).video_urls
    print(f'\nThere are {len(video_links)} videos in this playlist: \n')
except Exception:
    print('\n Please enter a valid YouTube Playlist URL')
    
for link in video_links:
    lngth = YouTube(link).length
    print(f'{YouTube(link).title} - {str(lngth)} seconds - {link}')

# print('\n Your video is ' + nm)

# Example Playlist - https://www.youtube.com/playlist?list=PLzMcBGfZo4-k-_nZU2GCrVKJF3Kvj7yFw
# Example Video Link - https://www.youtube.com/watch?v=YQEn0Exy4vc (This should result in an error as this is not a playlist URL)
