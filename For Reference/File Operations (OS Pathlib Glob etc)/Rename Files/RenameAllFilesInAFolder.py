import os
from pathlib import Path
from posixpath import split

curr_path = Path(input('\nPlease enter the directory where you want to rename the files: \n'))

# xs = split(curr_path)
# print(Path(curr_path).name)
# print(xs[-1])

# for file in os.listdir(curr_path):
#     if Path(file).is_file():
#         Path(file).rename(f'{split(curr_path,2)} - {file}')

