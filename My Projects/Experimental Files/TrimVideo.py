# Python code to convert video to audio
from moviepy.editor import *
import moviepy.editor as mp
  
# Insert Local Video File Path 
pth =  input('\nPlease enter the path of the video along with the extension which you wish to convert: ')
pth = pth.replace('"','')
clip = mp.VideoFileClip(pth)
startpoint = input('\nPlease enter the beginning point: ')
endpoint = input('\nPlease enter the end point: ')
clip2 = clip.subclip(startpoint,endpoint)

newfile = pth.replace('.mp4','_2.mp4')

clip2.write_videofile(newfile)

# "C:/Users/AU/Videos/InfraSound - Starlight   Epic Powerful Hybrid Orchestral Music.mp4"