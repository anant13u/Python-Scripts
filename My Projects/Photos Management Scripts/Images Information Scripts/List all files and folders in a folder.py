# Get filenames from a folder

import os
from pathlib import Path

base_path = input('Please enter the path where you want to search for Live Photos: \n')
# print(our_path)

entries = os.listdir(base_path)
# print(entries)

dirs_log = ['Directories:\n']
files_log = ['\n\n\nFiles:\n']
log_file = os.path.join(base_path,'Log File.txt')

for entry in entries:
    entry_path = os.path.join(base_path,entry)
    try:
        if Path(entry_path).is_dir():
            dirs_log.append(entry)
            # print(f'{entry} is a directory.')
        elif Path(entry_path).is_file:
            files_log.append(entry)
            # print(f'{entry} is a file.')
        else:
            print(f'{entry} type is unknown.')
    except Exception as e:
        print(f'Encountered error with {entry}: {e}')

with open(log_file,'w') as log_file:
    log_file.write('\n'.join(dirs_log) + '\n'.join(files_log))
        
# /media/anant/Games, Torrents, Other Stuff
# /media/anant/Games, Torrents, Other Stuff/Torrents/Movies and Shows
# /home/anant/Downloads


