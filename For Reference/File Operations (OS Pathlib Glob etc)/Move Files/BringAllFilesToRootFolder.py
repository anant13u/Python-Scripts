from pathlib import Path
import os
# import contextlib
from datetime import datetime


root_folder = input('\n Enter the directory path where you want to perform the search & move: ')
root_folder = Path(root_folder.replace('"',''))

for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file!='log.txt':
            try:
                Path.joinpath(Path(root), file).rename(Path.joinpath(root_folder, file))
            except FileExistsError:
                with open(Path.joinpath(root_folder,'log.txt'),'a') as log_file:
                    curr_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    log_file.write(f'\n{curr_datetime} - "{root_folder}" already contains a file named "{file}".')

        # with contextlib.suppress(FileExistsError):
        #      Path.joinpath(Path(root),Path(file)).rename(Path.joinpath(root_folder, file))

    # D:\Python\For Reference\File Operations (OS Pathlib Glob etc)\Testing Grounds\Testing for moving files
