import webbrowser
from os import startfile
from pathlib import Path
import time
import PySimpleGUI as sg
from pytube import YouTube
from datetime import datetime

sg.theme('darkamber')
sg.set_options(font=('Calibri',11)) # https://stackoverflow.com/a/67155752/18791688
# download_path = Path('C:/Users/Anant/Downloads') # Setting default download path to user's Downloads folder.

getDWPath = sg.Window('Select the Download Folder',
                    [  [sg.FolderBrowse('Select Download Folder',key='download_folder'), sg.B('Proceed')]  ])
while True:
    event, values = getDWPath.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Proceed':
        # print('okkkk')
        download_path = Path(values['download_folder'])
        print(download_path)
        break
getDWPath.close()

mew = time.sleep(1.5)
replacers_dict = {'|':'', ':':'', '/':'', '\\':'', '"':'', '*':'', '?':'', '<':'', '>':''}
# replacers = ['|','|', ':', '/', '\\', '"', '*', '?', '<', '>']


def download_another_video():
    """
    If the user clicks on Yes, the function download_video() is called again, else the program ends.
    """
    while True:
        event, values = sg.Window('What to do Next',
                        [  [sg.T('Do you wish to download another video?')],
                        [sg.B('Yes', pad=(30,10)),sg.B('No', pad=(30,10))]    ]).read(close=True) # close=True closes the Window after getting the input in form of Yes or No
        if event=='Yes':
            download_video()
        else:
            mew
        break

def download_video():
    download_video_layout = [  [sg.T(' ')],
                [sg.T(' '),sg.T('Please enter the URL for the YouTube video below:      '),sg.T()],
                [sg.T(' ')],
                [sg.T(' '),sg.InputText(key='-URL-')],
                [sg.T(' ')],
                [sg.T(' '),sg.Ok('Fetch Video Details',size=(17,2)),sg.T('  '),sg.B('Exit',size=(17,2))],
                [sg.T()]]

    download_video_window = sg.Window('YouTube Video Downloader by AU', download_video_layout)

    while True:
        event, values = download_video_window.read()
        if event in (sg.WIN_CLOSED or 'Exit'):
            break
        elif values['-URL-']=='':
            sg.popup('Field cannot be blank, please enter a YouTube Video URL!')
        elif event=='Fetch Video Details' and values['-URL-'].find('https://www.youtube.com/')<0: # IF an URL is provided not having "https://www.youtube.com/watch?v=" in it.
            sg.popup('Please enter a valid YouTube Video URL!')
        elif event=='Fetch Video Details':
            url = values['-URL-']
            try:
                yt = YouTube(url)
            except:
                download_video_window.close()
                sg.popup(f'"yt = YouTube(url)" line could not be resolved. Go cry a fu***ng river.')
                download_another_video()
                break
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(22)
            # yt_captions = yt.captions.get_by_language_code('en')
            video_name_raw = stream.title
            channel_name = yt.author
            download_video_window.close()
            print(video_name_raw)
            event, values = sg.Window('Wanna Download This?',
                [  [sg.T()],
                [sg.T(),sg.T(f'Your video is "{video_name_raw}"\n\nChannel Name: {channel_name}\n\nLength of the video is {yt.length//60} minutes and {yt.length%60} seconds\n\nApprox Size of the video is {round(stream.filesize_approx/(1024*1024),2)} MB\n')],
                [sg.T(),sg.T(f'{yt.description}',size=(55,8))],
                [sg.T()],
                [sg.T(),sg.B('Only Download',size=(22,2)),sg.T(' '*5),sg.B('Download and play Video',size=(22,2)),sg.T(' '*5),sg.B("I'd rather quit bro",size=(22,2))],
                [sg.T()]  ]).read(close=True) # close=True closes the Window after getting the input in form of Yes or No
            def only_download():
                # video_name_cleaned = video_name_raw
                # Below we are replacing the characters in the replacers_dict dictionary with an empty string.
                for key, value in replacers_dict.items():
                    video_name_cleaned = video_name_raw.replace(key,value) # Important to assign a new 
                        # variable video_name_cleaned as we cannot use an assignment statement on nm in middle of a function.
                        # https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment
                print(f'\n Video name: "{video_name_cleaned}"')
                final_file = Path.joinpath(download_path,f'{channel_name} - {video_name_cleaned}.mp4') # Changing filename to now have the entire path, the channel name, and the mp4 extension.
                print(f'\n {final_file}')
                # Below we are checking if the file already exists in the download path. If it does, it will open
                # the download path in the browser and show the file already exists.
                if Path(final_file).exists():
                    sg.popup(f'The file already exists at {download_path}')
                else:
                    # Below we will show a popup with the text "Downloading..." and the duration of the popup is
                    # the size of the video divided by 3.
                    sg.popup_auto_close('Downloading...',auto_close_duration=5)
                    # auto_close_duration=stream.filesize_approx/(1024*1024*3)
                    stream.download(output_path=download_path, filename=Path(final_file).name) # Download path is already provided at the beginning of the script.
                    # with open(Path.joinpath(download_path,'captions.txt'),'a+') as captions:
                    #     for c in yt_captions:
                    #         captions.write(c)
                    print(f'\n Downloaded filename: \n "{final_file}"')
                    curr_datetime = datetime.now().strftime('%d/%m/%y %H:%M:%S')
                    with open(Path.joinpath(download_path,'Downloaded Videos.txt'),'a+') as curr_log:
                        curr_log.write(f'\n{curr_datetime} - Downloaded "{final_file}"')
                    sg.popup(f'Your video "{video_name_raw}" has been downloaded and saved at - "{download_path}"')
                webbrowser.open(download_path) # This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
                return final_file # Using return to capture downloaded file's name so we can refer to only_download function later on and retrieve it.
            if event=='Only Download':
                only_download()
                # download_another_video()
            elif event=='Download and play Video':
                startfile(only_download())
            download_another_video()
            break

download_video()
