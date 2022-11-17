import webbrowser
import os
import PySimpleGUI as sg
from os import startfile
from pytube import YouTube

sg.theme('darkamber')
helv= ('Calibri',11)
download_path = 'C:/Users/AU/Downloads'

# def main():
#     get_details()
#     download_video()

def get_details():
    # values['-URL-']==''
    get_details_layout = [  [sg.T(' ')],
                [sg.T(' '),sg.T('Please enter the URL for the YouTube video below:',font=helv)],
                [sg.T(' ')],
                [sg.T(' '),sg.InputText(key='-URL-',size=(50,2))],
                [sg.T(' ')],
                [sg.T(' '),sg.Ok('Fetch Video Details',font=helv,size=(17,2)),sg.T('  '),sg.Cancel(font=helv,size=(17,2))],
                [sg.T('',key='-VIDEO_NAME-')]]

    get_details_window = sg.Window('YouTube Video Downloader by AU', get_details_layout, size=(370,220))

    while True:
        event, values = get_details_window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif values['-URL-']=='':
            sg.popup('Please enter a valid YouTube Video URL!')
        elif event=='Fetch Video Details':
            url1 = values['-URL-']
            yt1 = YouTube(url1)
            yt1.streams.filter(file_extension='mp4')
            stream1 = yt1.streams.get_by_itag(22)
            nm1 = stream1.title
            channel_name1=yt1.author
            get_details_window.close()
            break
    get_details_window.close()
    return url1, yt1, stream1, channel_name1, nm1
    # return values['-URL-']

url, yt, stream, channel_name, nm = get_details()
print(nm)

# url = values['-URL-']
# yt = YouTube(url)
# yt.streams.filter(file_extension='mp4')
# stream = yt.streams.get_by_itag(22)
# nm = stream.title
# channel_name=yt.author

def download_another_video():
    while True:
        event, values = sg.Window('What to do Next',
                        [  [sg.T('Do you wish to download another video?')],
                        [sg.B('Yes'),sg.B('No')]    ]).read(close=True) # close=True closes the Window after getting the input in form of Yes or No
        if event=='Yes':
            get_details()
            url, yt, stream, channel_name, nm = get_details()
            download_video()
        break

def download_video():
    download_layout = [  [sg.T()],
                [sg.T(),sg.T(f'Your video is "{nm}"\n',font=helv)],
                [sg.T(),sg.T(f'Length of the video is {yt.length//60} minutes and {yt.length%60} seconds\n',font=helv)],
                [sg.T(),sg.T(f'{yt.description}',size=(55,5),font=helv)],
                [sg.T()],
                [sg.T(),sg.B('Download Video',font=helv),sg.T(),sg.Cancel(font=helv)],
                [sg.T()]  ]

    download_window = sg.Window('YouTube Video Downloader', download_layout)

    while True:
        event, values = download_window.read()
        if event=='Download Video':
            download_window.close()
            stream.download('C:/Users/AU/Downloads') # Download path is already provided at the beginning of the script.
            sg.popup(f'Your video {nm} has been downloaded and saved at - {download_path}')
            webbrowser.open('C:/Users/AU/Downloads') # This will open the directory where we've downloaded the video. Webbrowser module will be imported automatically.
            clean_name = nm.replace(':','') # Important to assign a new variable newnm as we cannot use an assignment statement on nm in middle of a function.
                                            # https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment
            clean_name = clean_name.replace('#','')
            print(clean_name+'\n')
            final_file = f'{download_path}/{channel_name} - {clean_name}.mp4' # Changing filename to now have the entire path, the channel name, and the mp4 extension.
            print(final_file+'\n')
            os.replace(f'{download_path}/{clean_name}.mp4',final_file)
            startfile(final_file)
            # print(f'The entire path for the downloaded file is "{final_file}"\n')
            # webbrowser.open_new_tab(url) # Use this line if you also want to open the Youtube video in the default browser.
            # Documentation for webbrowser module - https://docs.python.org/3/library/webbrowser.html
            download_another_video()
            break
        else:
            sg.popup('Video has not been downloaded')
            break

download_video()
