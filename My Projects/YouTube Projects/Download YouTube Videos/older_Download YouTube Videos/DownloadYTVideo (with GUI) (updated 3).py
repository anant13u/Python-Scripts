import webbrowser
import os
import PySimpleGUI as sg
from os import startfile
from pytube import YouTube
import time

sg.theme('darkamber')
helv= ('Calibri',11)
download_path = 'C:/Users/AU/Downloads'
mew = time.sleep(1.5)

# def main():
#     get_details()
#     download_video()

def download_another_video():
    while True:
        event, values = sg.Window('What to do Next',
                        [  [sg.T('Do you wish to download another video?')],
                        [sg.B('Yes'),sg.B('No')]    ]).read(close=True) # close=True closes the Window after getting the input in form of Yes or No
        if event=='Yes':
            download_video()
            # url, yt, stream, channel_name, nm = get_details()
            # download_video()
        else:
            mew
        break

def download_video():
    # values['-URL-']==''
    download_video_layout = [  [sg.T(' ')],
                [sg.T(' '),sg.T('Please enter the URL for the YouTube video below:',font=helv)],
                [sg.T(' ')],
                [sg.T(' '),sg.InputText(key='-URL-',size=(50,2))],
                [sg.T(' ')],
                [sg.T(' '),sg.Ok('Fetch Video Details',font=helv,size=(17,2)),sg.T('  '),sg.Cancel(font=helv,size=(17,2))],
                [sg.T('',key='-VIDEO_NAME-')]]

    download_video_window = sg.Window('YouTube Video Downloader by AU', download_video_layout, size=(370,220))

    while True:
        event, values = download_video_window.read()
        if event==sg.WIN_CLOSED or event=='Cancel':
            break
        elif values['-URL-']=='':
            sg.popup('Field cannot be blank, please enter a YouTube Video URL!')
        elif event=='Fetch Video Details' and values['-URL-'].find('https://www.youtube.com/watch?v=')<0: # IF an URL is provided not having "https://www.youtube.com/watch?v=" in it.
            sg.popup('Please enter a valid YouTube Video URL!')
        elif event=='Fetch Video Details':
            url = values['-URL-']
            yt = YouTube(url)
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(22)
            nm = stream.title
            channel_name=yt.author
            # print(nm)
            download_video_window.close()
            event, values = sg.Window('Wanna Download This?',
                            [  [sg.T()],
                            [sg.T(),sg.T(f'Your video is "{nm}"\n',font=helv)],
                            [sg.T(),sg.T(f'Length of the video is {yt.length//60} minutes and {yt.length%60} seconds\n',font=helv)],
                            [sg.T(),sg.T(f'{yt.description}',size=(55,5),font=helv)],
                            [sg.T()],
                            [sg.T(),sg.B('Download',font=helv),sg.T(),sg.B('Download and play Video',font=helv),sg.T(),
                             sg.B("I'd rather quit bro",font=helv)],
                            [sg.T()]  ]).read(close=True) # close=True closes the Window after getting the input in form of Yes or No
            def only_download():
                stream.download(download_path) # Download path is already provided at the beginning of the script.
                sg.popup(f'Your video "{nm}" has been downloaded and saved at - "{download_path}"',font=helv)
                webbrowser.open(download_path) # This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
                cleaned_name = nm.replace(':','') # Important to assign a new variable cleaned_name as we cannot use an assignment statement on nm in middle of a function.
                                                # https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment
                cleaned_name = cleaned_name.replace('#','')
                print(f'\n Video name: "{cleaned_name}"')
                final_file = f'{download_path}/{channel_name} - {cleaned_name}.mp4' # Changing filename to now have the entire path, the channel name, and the mp4 extension.
                print(f'\n Downloaded filename: "{final_file}"')
                os.replace(f'{download_path}/{cleaned_name}.mp4',final_file)
                return final_file # Using return to capture downloaded file's name so we can refer to only_download function later on and retrieve it.
            if event=='Download':
                only_download()
                download_another_video()
                break
            elif event=='Download and play Video':
                startfile(only_download())
                download_another_video()
                break
            else:
                break

download_video()
