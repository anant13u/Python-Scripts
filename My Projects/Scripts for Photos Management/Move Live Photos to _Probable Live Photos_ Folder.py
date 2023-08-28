import os
from pathlib import Path

base_path = input('Please enter the path where you want to search for Live Photos: \n')
curr_folder = os.path.basename(base_path)
live_folder_path = os.path.join(base_path,f'Probable Live Photos ({curr_folder})')
# print(our_path)

entries = os.listdir(base_path)
# print(entries)

for file in entries:
    curr_file_path = os.path.join(base_path,file)
    # print(full_file_path)
    # print(Path(full_file_path).suffix.lower())
    # print(Path(full_file_path).is_file())
    # print(os.path.getsize(full_file_path)/(1024*1024))
    file_size = os.path.getsize(curr_file_path)/(1024*1024)
    if Path(curr_file_path).suffix.lower()=='.mov' and Path(curr_file_path).is_file() and (1<file_size<6):
        # print(f'{file} could be a Live Photo.')
        if not os.path.exists(live_folder_path):
            os.mkdir(live_folder_path)
        new_file_path=os.path.join(live_folder_path,file)
        os.rename(curr_file_path,new_file_path)
        with open(os.path.join(live_folder_path,'Probable Live Photos.txt'),'a+') as curr_log:
            curr_log.write(f'\nMoved file - "{file}". Size: {round(file_size,2)} MB.')


# F:\Musical World\Music Videos\^ H ^\90's
# H:\Pics\# Timeline #\2022\August 2022\New folder (4)
