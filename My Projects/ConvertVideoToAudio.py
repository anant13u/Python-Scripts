# Python code to convert video to audio

import moviepy.editor as mp # Before this the moviepy module needs to be installed using PIP
  
# Insert Local Video File Path 
pth =  input('\nPlease enter the path of the video along with the extension which you wish to convert: ')
pth = pth.replace('"','')
clip = mp.VideoFileClip(pth)
  
newfile = pth.replace('.mp4','.mp3') # Here 'newfile' will the complete path for the newly created audio file.

# Insert Local Audio File Path
clip.audio.write_audiofile(newfile)

# "C:/Users/AU/Videos/InfraSound - Starlight   Epic Powerful Hybrid Orchestral Music.mp4"