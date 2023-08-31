import os
from pathlib import Path

# Get the base path from the user
base_path = input('Please enter the path where you want to search for Live Photos, PNG Files and AAE Files: \n')

# Extract the current folder name from the base path
curr_folder = os.path.basename(base_path)

# Create paths for various folders using the current folder name
live_folder_path = os.path.join(base_path, f'Probable Live Photos ({curr_folder})')
misc_folder_path = os.path.join(base_path, f'Miscellaneous ({curr_folder})')
aae_folder_path = os.path.join(misc_folder_path, f'AAE Files ({curr_folder})')
png_folder_path = os.path.join(misc_folder_path, f'Screenshots and other PNG Files ({curr_folder})')

entries = os.listdir(base_path)
# print(entries)

for file in entries:
    curr_file_path = os.path.join(base_path,file)
    if Path(curr_file_path).is_file():
        # print(full_file_path)
        # print(Path(full_file_path).suffix.lower())
        # print(Path(full_file_path).is_file())
        # print(os.path.getsize(full_file_path)/(1024*1024))
        file_size = os.path.getsize(curr_file_path)/(1024*1024)
        file_ext = Path(curr_file_path).suffix.lower()
        if file_ext=='.mov' and file_size<7:
        # if file_ext=='.mov' and 1<file_size<7:
            # print(f'{file} could be a Live Photo.')
            if not os.path.exists(live_folder_path):
                os.mkdir(live_folder_path)
            new_file_path=os.path.join(live_folder_path,file)
            os.rename(curr_file_path,new_file_path)
            with open(os.path.join(live_folder_path,'Probable Live Photos.txt'),'a+') as curr_log:
                curr_log.write(f'\nMoved file - "{file}". Size: {round(file_size,2)} MB.')

        elif file_ext=='.aae':
            if not os.path.exists(misc_folder_path):
                os.mkdir(misc_folder_path)
            if not os.path.exists(aae_folder_path):
                os.mkdir(aae_folder_path)
            new_file_path=os.path.join(aae_folder_path,file)
            os.rename(curr_file_path,new_file_path)
            with open(os.path.join(aae_folder_path,'AAE Files.txt'),'a+') as curr_log:
                curr_log.write(f'\nMoved AAE file - "{file}".')

        elif file_ext=='.png':
        # print(f'{file} is an AAE file.')
            if not os.path.exists(misc_folder_path):
                os.mkdir(misc_folder_path)
            if not os.path.exists(png_folder_path):
                os.mkdir(png_folder_path)
            new_file_path=os.path.join(png_folder_path,file)
            os.rename(curr_file_path,new_file_path)
            with open(os.path.join(png_folder_path,'PNG Files.txt'),'a+') as curr_log:
                curr_log.write(f'Moved PNG file - "{file}".\n')
                
        elif 0<file_size<1 or file_ext=='.mp4':
        # elif 0<file_size<1 or (file_ext=='.mp4' and 1<file_size<7):
            # print(f'{file} - file or not status: {Path(curr_file_path).is_file()}')
            if not os.path.exists(misc_folder_path):
                os.mkdir(misc_folder_path)
            new_file_path=os.path.join(misc_folder_path,file)
            os.rename(curr_file_path,new_file_path)
    


# F:\Musical World\Music Videos\^ H ^\90's
# H:\Pics\# Timeline #\2022\August 2022\New folder (4)
