import webbrowser
import pyperclip
from pathlib import Path
import time
import PySimpleGUI as sg
from pytube import YouTube
from datetime import datetime

sg.theme('darkamber') # sg.theme_previewer()
sg.set_options(font=('Calibri',11)) # https://stackoverflow.com/a/67155752/18791688

folderBrowse = sg.FolderBrowse('Select Download Folder',key='download_folder', size=(45,2), pad=(40,(30,10)))
proceedButton = sg.B('Proceed', size=(18,2), pad=(45,30))

getDWPathWindow = sg.Window('Select the Download Destination',
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

# mew = time.sleep(1.5)
replacers_dict = {'|':'', '।':'', ':':'', '/':'', '\\':'', '"':'', '*':'', '?':'', '<':'', '>':''}
# replacers = ['|','|', ':', '/', '\\', '"', '*', '?', '<', '>']


def download_another_video():
    """
    If the user clicks on Yes, the function download_video() is called again, else the program ends.
    """
    while True:
        event, values = sg.Window('Download another video?',
                        [   [sg.T('Do you wish to download another video?', pad=(50,15))],
                            [sg.B('Yes', size=(15,1), pad=(30,15)),sg.B('No', size=(15,1), pad=(30,15))]    ]).read(close=True) # close=True closes the Window after getting the input in form of Yes or No
        if event=='Yes':
            mains()
        else:
            time.sleep(1)
        break


def download_video(video_name, channel_name, url, yt, stream):
    # Below we are replacing the characters in the replacers_dict dictionary present in video name with an empty string.
    for key, value in replacers_dict.items():
        video_name = video_name.replace(key,value)
    print(f'\n Video name: "{video_name}"')
    final_file = Path.joinpath(download_path,f'{channel_name} - {video_name}.mp4') # Changing filename to now have the entire path, the channel name, and the mp4 extension.
    print(f'\n {final_file}')
    # Below we are checking if the file already exists in the download path. If it does, it will open
    # the download path in the browser and show the file already exists.
    if Path(final_file).exists():
        sg.popup(f'The file already exists at {download_path}')
    else:
        # Below we will show a popup with the text "Downloading..." and the duration of the popup is (size of the video)/3.
        sg.popup_auto_close('Downloading...',auto_close_duration=5)
        # auto_close_duration=stream.filesize_approx/(1024*1024*3)
        try:
            print(download_path)
            print(Path(final_file).name)
            stream.download(output_path=download_path, filename=Path(final_file).name) # Download path is already provided at the beginning of the script.
        except Exception as e:
            sg.popup(f'Error encountered: {e}')
            print(f'Error encountered: {e}')
        print(f'\n Downloaded filename: \n "{final_file}"')
        curr_datetime = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        with open(Path.joinpath(download_path,'Downloaded Videos.txt'),'a+',encoding='utf-8') as curr_log:
            curr_log.write(f'{curr_datetime}\n'
                            f'Download Location: {download_path}\n'
                            f'Video: "{video_name}".\n'
                            f'URL: {url}\n'
                            f'Channel: {channel_name}.\n'
                            f'Length: {yt.length//60} minutes, {yt.length%60} seconds.\n'
                            f'Size: {round(final_file.stat().st_size/(1024*1024), 2)} MB.\n'
                            f'Description: {yt.description}\n\n')
        sg.popup(f'Your video: "{video_name}" has been downloaded and saved at - "{download_path}"')
    webbrowser.open(download_path) # This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
    # return final_file # Using return to capture downloaded file's name so we can refer to only_download function later on and retrieve it.


def mains():
    download_video_layout = [   [sg.T('Please enter the URL for the YouTube video below:', pad = (20,20))],
                                [sg.InputText(pyperclip.paste(),key='-URL-', pad = (20,10))],
                                [sg.Ok('Fetch Video Details',size=(17,2), pad=(20,20)),sg.B('Exit',size=(17,2), pad=(20,20))]    ]
        
    download_video_window = sg.Window('YouTube Video Downloader by AU', download_video_layout,keep_on_top=True)

    while True:
        event, values = download_video_window.read()
        if event in (sg.WIN_CLOSED or 'Exit'):
            break
        elif values['-URL-']=='':
            sg.popup('Field cannot be blank, please enter a YouTube Video URL!', keep_on_top=True)
        elif event=='Fetch Video Details' and values['-URL-'].find('https://www.youtube.com/')<0: # IF a URL is provided but does not have "https://www.youtube.com/" in it.
            sg.popup('Please enter a valid YouTube Video URL!')
        elif event=='Fetch Video Details':
            url = values['-URL-']
            try:
                yt = YouTube(url)
            except Exception as e:
                download_video_window.close()
                sg.popup(f'"yt = YouTube(url)" line could not be resolved.\nError Encountered: {e}', keep_on_top=True)
                print(f'"yt = YouTube(url)" line could not be resolved.\nError Encountered: {e}')
                download_another_video()
                break
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(22)
            video_name = stream.title
            channel_name = yt.author
            download_video_window.close()
            print(video_name)
            box_height = (len(video_name)//50) + 1
            event, values = sg.Window('Want to Download This Video?',
                [   [sg.T(f'Your video is "{video_name}"', s=(50,box_height), pad=(20,10))],
                    [sg.T(f'Channel Name: {channel_name}', pad=(20,10))],
                    [sg.T(f'Length of the video is {yt.length//60} minutes and {yt.length%60} seconds.', pad=(20,10))],
                    [sg.T(f'Approx Size of the video is {round(stream.filesize_approx/(1024*1024),2)} MB.', pad=(20,10))],
                    [sg.T(f'{yt.description}', size=(55,8), pad=(20,(10,25)))],
                    [sg.B('Download', size=(22,2), pad=(30,20)), sg.B("Exit",size=(22,2), pad=(20,20))]    ], keep_on_top=True).read(close=True) # close=True closes the Window after getting the input in form of Yes or No

            if event=='Download':
                download_video(video_name, channel_name, url, yt, stream)

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
