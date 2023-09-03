# Get filenames from a folder

import os
from pathlib import Path

base_path = input('Please enter the path where you want to search for Live Photos: \n')
# print(our_path)

entries = os.listdir(base_path)
# print(entries)

# for entry in entries:
    # print(f'Entry: {entry}')
    # print(f'Entry Absolute: {Path(entry).absolute()}')

for entry in entries:
    entry_path = os.path.join(base_path,entry)
    try:
        if Path(entry_path).is_dir():
            print(f'{entry} is a directory.')
        else:
            print(f'{entry} is not a directory.')
    except Exception as e:
        print(f'Encountered error with {entry}: {e}')
        
# /media/anant/Games, Torrents, Other Stuff
