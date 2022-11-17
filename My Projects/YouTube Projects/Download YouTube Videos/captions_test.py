from pytube import YouTube

# yt=YouTube(input('Please enter the URL: '))
yt = YouTube('https://www.youtube.com/watch?v=51u5fnyrGj4')

# yt.streams.filter(file_extension='mp4')
# stream = yt.streams.get_by_itag(22)
# print(yt.captions.all())

# stream = yt.streams.get_highest_resolution()
# stream.download(r'C:\Users\AU\Downloads\New folder', 'testfile.mp4')
caption = yt.captions.get_by_language_code('en')
print(caption)

# caption.xml_captions
# print(caption)
# print(caption.generate_srt_captions())


# print(yt.captions.get('a.en'))
# print(yt_captions)
# video_name_raw = stream.title
# channel_name = yt.author
# download_video_window.close()
# print(video_name_raw)
