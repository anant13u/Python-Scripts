# Get filenames from a folder

import os
from pathlib import Path

base_path = input('Please enter the path where you want to search for Live Photos: \n')
# print(our_path)

entries = os.listdir(base_path)
# print(entries)

log = []

for entry in entries:
    entry_path = os.path.join(base_path,entry)
    try:
        if Path(entry_path).is_dir():
            print(f'{entry} is a directory.')
        elif Path(entry_path).is_file:
            print(f'{entry} is a file.')
        else:
            print(f'{entry} type is unknown.')
    except Exception as e:
        print(f'Encountered error with {entry}: {e}')
        
# /media/anant/Games, Torrents, Other Stuff
# /media/anant/Games, Torrents, Other Stuff/Torrents/Movies and Shows

