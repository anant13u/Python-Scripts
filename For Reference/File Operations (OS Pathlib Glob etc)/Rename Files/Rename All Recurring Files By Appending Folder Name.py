import os
from pathlib import Path

curr_path = Path(input('\nPlease enter the directory where you want to rename the files: \n'))

for root, dirs, files in os.walk(curr_path):
    for file in files:
        if Path.joinpath(Path(root),Path(file)).is_file():
            # print(Path(root).name)
            Path(Path.joinpath(Path(root),file)).rename(Path.joinpath(Path(root),f'{Path(root).name} - {file}'))

