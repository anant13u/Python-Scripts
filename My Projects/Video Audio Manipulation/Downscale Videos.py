import moviepy.editor as mp
import PySimpleGUI as sg
import subprocess
from pathlib import Path
import os

sg.theme('Reddit')
# sg.theme_previewer()

widthInput = sg.I('', key = 'video_width', s=(15,2), pad=((10,30), 20))
heightInput = sg.I('', key = 'video_height', s=(15,2), pad=((10,30), 20))

layout = [  [sg.T('Select Video', s=(35,2), pad=((50,30),20)), sg.FileBrowse(key='video_file', s=(15,2), pad=(30,30))],
            [sg.T('Output Width', pad=(30,20)), widthInput, sg.T('Output Height', pad=(30,20)), heightInput],
            [sg.B('Downscale Video', s=(18,2), pad=(80,30)), sg.B('Exit', s=(15,2), pad=(50,20))]  ]
            
Window = sg.Window('Downscale Videos', layout, keep_on_top=True, grab_anywhere=True)

# def time_to_seconds(time_str):
#     # Split the time string into hours, minutes, and seconds
#     hours, minutes, seconds = map(int, time_str.split(':'))
    
#     # Convert the time components to seconds and sum them up
#     total_seconds = hours * 3600 + minutes * 60 + seconds
#     return total_seconds

while True:
    event, values = Window.read()
    videoFile = values['video_file']
    print(os.path.dirname(videoFile))
    # print(videoFile)
    # print(os.path.basename(videoFile).split('.')[0])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['video_file']=='':
        sg.popup('Please select a video to perform operations on.')
    elif values['video_width'] == '' or values['video_height']=='':
        sg.popup('Please enter width and height for downscaling the video.')
    elif event == 'Downscale Video':
        filename = os.path.basename(videoFile).split('.')[0] # Extract the filename from the path and remove the extension
        try:
            videoWidth = int(values['video_width']) # Convert start time from HH:MM:SS to total seconds
            videoHeight = int(values['video_height']) # Convert end time from HH:MM:SS to total seconds
        except ValueError:
            sg.popup_error('Invalid width or height format.')
        # if startTime >= endTime:
        #     sg.popup("Start Time can't be greater than End Time.")
        ourClip = mp.VideoFileClip(videoFile) # Load the video file
        target_resolution = (videoWidth, videoHeight)
        print(target_resolution)
        # Resize the video to the target resolution
        resized_clip = ourClip.resize(target_resolution)
        # Compute the modified file name with start and end times appended
        new_filename = f'{filename}_{videoHeight}'
        # Write the trimmed video to a new file with the start and end times appended to the filename:
        resized_clip.write_videofile(videoFile.replace(filename, new_filename), codec='libx264')
        # Close the video clip object to release resources
        ourClip.close()
        subprocess.Popen(['explorer.exe', Path(videoFile).parent])


