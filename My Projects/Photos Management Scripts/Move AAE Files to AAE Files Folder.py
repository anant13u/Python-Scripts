import os
from pathlib import Path

base_path = input('Please enter the path where you want to search for AAE Files: \n')
curr_folder = os.path.basename(base_path)
aae_folder_path = os.path.join(base_path,f'AAE Files ({curr_folder})')
# print(our_path)

entries = os.listdir(base_path)
# print(entries)

for file in entries:
    curr_file_path = os.path.join(base_path,file)
    # print(full_file_path)
    # print(Path(full_file_path).suffix.lower())
    # print(Path(full_file_path).is_file())
    # print(os.path.getsize(full_file_path)/(1024*1024))
    if Path(curr_file_path).suffix.lower()=='.aae' and Path(curr_file_path).is_file():
        # print(f'{file} is an AAE file.')
        if not os.path.exists(aae_folder_path):
            os.mkdir(aae_folder_path)
        new_file_path=os.path.join(aae_folder_path,file)
        os.rename(curr_file_path,new_file_path)
    with open(os.path.join(aae_folder_path,'AAE Files.txt'),'a+') as curr_log:
        curr_log.write(f'\nMoved AAE file - "{file}".')
    

# F:\Musical World\Music Videos\^ H ^\90's
# H:\Pics\# Timeline #\2022\August 2022\New folder (4)
