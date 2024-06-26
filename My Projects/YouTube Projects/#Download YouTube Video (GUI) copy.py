import webbrowser
import pyperclip
from pathlib import Path
import time
import PySimpleGUI as sg
from pytube import YouTube
from pytube.cli import on_progress
from datetime import datetime

sg.theme('darkamber') # sg.theme_previewer()
sg.set_options(font=('Calibri',11)) # https://stackoverflow.com/a/67155752/18791688
sg.ProgressBar(100, size=(20, 30), key='-progress')


folderBrowse = sg.FolderBrowse('Select Download Folder',key='download_folder', size=(45,2), pad=(40,(30,10)))
proceedButton = sg.B('Proceed', size=(18,2), pad=(45,30))

getDWPathWindow = sg.Window('Select the Download Destination and proceed',
                    [   [folderBrowse],
                        [proceedButton, sg.B('Exit', size=(18,2)) ]  ], keep_on_top=True)
while True:
    event, values = getDWPathWindow.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        exit()  # Exit the script if the window is closed or Exit button is clicked.
    elif event == 'Proceed':
        if values['download_folder'] == '':
            sg.popup('Please select a download location.', keep_on_top=True)
        else:
            download_path = Path(values['download_folder'])
            print(download_path)
            getDWPathWindow.close()
            break

replacers_dict = {'|':'', '।':'', ':':'', '/':'', '\\':'', '"':'', '*':'', '?':'', '<':'', '>':''}
# replacers = ['|','|', ':', '/', '\\', '"', '*', '?', '<', '>']


def download_another_video():
    """
    If the user clicks on Yes, the function download_video() is called again, else the program ends.
    """
    while True:
        event, values = sg.Window('Download another video?',
                        [   [sg.T('Do you wish to download another video?', pad=(50,15))],
                            [sg.B('Yes', size=(15,1), pad=(30,15)),sg.B('No', size=(15,1), pad=(30,15))]    ], keep_on_top=True).read(close=True) # close=True closes the Window after getting the input in form of Yes or No
        if event=='Yes':
            mains()
        # else:
        #     time.sleep(1)
        break


def download_video(channel_name, url, yt, stream, download_video_window):

    def on_progress(stream, chunk, bytes_remaining):
        size = stream.filesize
        bytes_downloaded = size - bytes_remaining
        progress_percent = (bytes_downloaded / size) * 100
        download_video_window['-progress-'].update_bar(progress_percent)

    # This line registers the on_progress function as a callback function for the YouTube object yt.
    # When a video download is in progress, the on_progress function will be automatically 
    # called periodically to update the progress of the download.
    yt.register_on_progress_callback(on_progress)

    # Below we are replacing the characters in the replacers_dict dictionary present in video name with an empty string.
    # for key, value in replacers_dict.items():
    #     video_name = video_name.replace(key,value)
    # print(f'\n Video name: "{video_name}"')
    final_file = Path(download_path,f'{channel_name} - .mp4') # Changing filename to now have the entire path, the channel name, and the mp4 extension.
    print(f'\n {final_file}')
    # Below we are checking if the file already exists in the download path.
    if Path(final_file).exists():
        sg.popup(f'The file already exists at {download_path}', keep_on_top=True)
    else:
        try:
            # print(download_path)
            # print(Path(final_file).name)
            stream.download(output_path=download_path, filename=Path(final_file).name) # Download path is already provided at the beginning of the script.
            print(f'\n Downloaded filename: \n "{final_file}"')
            curr_datetime = datetime.now().strftime('%d/%m/%y %H:%M:%S')
            with open(Path.joinpath(download_path,'Downloaded Videos.txt'),'a+',encoding='utf-8') as curr_log:
                curr_log.write(f'{curr_datetime}\n'
                                f'Download Location: {download_path}\n'
                                # f'Video: "{video_name}".\n'
                                f'URL: {url}\n'
                                f'Channel: {channel_name}.\n'
                                f'Length: {yt.length//60} minutes, {yt.length%60} seconds.\n'
                                f'Size: {round(final_file.stat().st_size/(1024*1024), 2)} MB.\n'
                                f'Description: {yt.description}\n\n')
            sg.popup(f'Your video has been downloaded and saved at - "{download_path}"', keep_on_top=True)
        except Exception as e:
            sg.popup(f'Error encountered: {e}')
            print(f'Error encountered: {e}')
    # webbrowser.open(download_path) # This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.


def mains():
    fetch_details_layout = [    [sg.T('Please enter the URL for the YouTube video below:', pad = (20,20))],
                                [sg.InputText(pyperclip.paste(),key='-URL-', pad = (20,10))],
                                [sg.Ok('Fetch Video Details',size=(17,2), pad=(20,20)),sg.B('Exit',size=(17,2), pad=(20,20))]    ]
        
    fetch_details_window = sg.Window('YouTube Video Downloader by AU', fetch_details_layout,keep_on_top=True)

    while True:
        event, values = fetch_details_window.read()
        if event in (sg.WIN_CLOSED or 'Exit'):
            break
        elif values['-URL-']=='':
            sg.popup('Field cannot be blank, please enter a YouTube Video URL!', keep_on_top=True)
        elif event=='Fetch Video Details' and values['-URL-'].find('https://www.youtube.com/')<0: # IF a URL is provided but does not have "https://www.youtube.com/" in it.
            sg.popup('Please enter a valid YouTube Video URL!')
        elif event=='Fetch Video Details':
            url = values['-URL-']
            try:
                yt = YouTube(url) # on_progress_callback=on_progress
                yt.streams.filter(file_extension="mp4").get_highest_resolution()
                # print(yt)
            except Exception as e:
                fetch_details_window.close()
                sg.popup(f'Error encountered: {e}', keep_on_top=True)
                print(f'Error encountered: {e}')
                download_another_video()
                break
            # Attempt to get a stream with the specified itag (itag 22 typically corresponds to 720p resolution).
            # try:
            #     stream = yt.streams.get_by_itag(18)
            # except:
            print(yt.streams)
            stream = yt.streams.get_by_itag(22)
            # stream = yt.streams.get_highest_resolution()
            print(stream)
            # stream = yt.streams.first()
            # try:
            #     video_name = stream.title
            # except:
            #     # Fall back to getting the title from the first available stream if 720p isn't available.
            #     # stream = yt.streams.first()
            #     # video_name = stream.title
            #     pass
            channel_name = yt.author
            fetch_details_window.close()
            # print(video_name)
            download_video_layout = [   [sg.T(f'Your video is ', s=(50,1), pad=(20,10))],
                        [sg.T(f'Channel Name: {channel_name}', pad=(20,10))],
                        [sg.T(f'Length of the video is {yt.length//60} minutes and {yt.length%60} seconds.', pad=(20,10))],
                        # [sg.T(f'Approx Size of the video is {round(stream.filesize_approx/(1024*1024),2)} MB.', pad=(20,10))],
                        [sg.T(f'{yt.description}', size=(55,8), pad=(20,(10,25)))],
                        [sg.ProgressBar(100, key='-progress-', s=(30,20), pad=(50,10))],
                        [sg.B('Download', size=(22,2), pad=(30,20)), sg.B("Exit",size=(22,2), pad=(20,20))]    ] # close=True closes the Window after getting the input in form of Yes or No
            download_video_window = sg.Window('YouTube Video Downloader by AU', download_video_layout)
            event, values = download_video_window.read()

            if event=='Download':
                download_video(channel_name, url, yt, stream, download_video_window)

            download_video_window.close()

            download_another_video()

            break

mains()



# https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment


# quality_radio_layout = [sg.Radio('720p', 'video_res_radio', default=True), sg.Radio('1080p', 'video_res_radio', k='1080_selected')]
                  
# [sg.Frame('Video Quality', [quality_radio_layout], pad = (110,10))],
    
# if values['1080_selected']:
#     try:
#         stream = yt.streams.filter(res='1080p').first() # Get the first stream with 1080p resolution
#         # stream = yt.streams.get_by_itag(137)
#         video_name = stream.title
