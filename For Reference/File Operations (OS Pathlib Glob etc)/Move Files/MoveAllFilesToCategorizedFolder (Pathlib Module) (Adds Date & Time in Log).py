from pathlib import Path
import os

format_dict = {'.mp4': 'Media Files', '.mkv': 'Media Files', '.mov': 'Media Files', '.mp3': 'Media Files',
               '.docx': 'Documents', '.doc': 'Documents', '.xlsx': 'Documents', '.xls': 'Documents',
               '.xlsm': 'Documents', '.csv': 'Documents', '.html': 'Documents', '.txt': 'Documents',
               '.epub': 'Documents', '.pdf': 'Documents', '.torrent': 'Documents', '.jpg': 'Images', '.png': 'Images', '.bmp': 'Images',
               '.rar': 'Compressed', '.zip': 'Compressed', '.exe': 'Programs'}

root_folder = input('\n Enter the directory path where you want to perform the search & move: ')
root_folder = Path(root_folder.replace('"', ''))

for file in os.listdir(root_folder):
    for key, value in format_dict.items():
        if Path(file).suffix == key:
            if not Path(Path.joinpath(root_folder, value)).exists():
                Path(Path.joinpath(root_folder, value)).mkdir()
            try:
                Path.joinpath(root_folder, file).rename(Path.joinpath(root_folder, value, file))
            except FileExistsError:
                pass

# import itertools
# +for file, (key, value) in itertools.product(os.listdir(root_folder), format_dict.items()):
# +    if Path(file).suffix == key:
# +        if not Path(Path.joinpath(root_folder, value)).exists():
# +            Path(Path.joinpath(root_folder, value)).mkdir()
# +        Path.joinpath(root_folder, file).rename(
# +            Path.joinpath(root_folder, value, file))

    # D:\Python\For Reference\File Operations (OS Pathlib Glob etc)\Testing Grounds\Testing for moving files
