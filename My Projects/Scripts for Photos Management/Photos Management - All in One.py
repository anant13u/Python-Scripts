import os
from pathlib import Path

# Get the base path from the user
base_path = input('Please enter the path where you want to manage Photos and other media files: \n')

# Extract the current folder name from the base path
curr_folder = os.path.basename(base_path)

# Create paths for the edited folder and log file.
edited_folder_path = os.path.join(base_path,f'Edited Photos and Videos ({curr_folder})')
edit_log_path = os.path.join(edited_folder_path,'Original and Edited Photos and Videos log.txt')

moved_pairs_list = ['Below is the list of moved pairs of media:\n']
moved_edited_only_list = ['Below is the list of moved edited media (original file was not found):\n']
error_list = ['Below are the errors encountered:\n']

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
                
        elif 0<file_size<1 or file_ext=='.mp4' or file_ext=='.gif':
        # elif 0<file_size<1 or (file_ext=='.mp4' and 1<file_size<7):
            # print(f'{file} - file or not status: {Path(curr_file_path).is_file()}')
            if not os.path.exists(misc_folder_path):
                os.mkdir(misc_folder_path)
            new_file_path=os.path.join(misc_folder_path,file)
            os.rename(curr_file_path,new_file_path)


for edited_file in entries:
    edited_file_path = os.path.join(base_path,edited_file)
    # Check if the entry is a regular file and starts with 'IMG_E'.
    if Path(edited_file_path).is_file() and edited_file.startswith('IMG_E'):
        try:
            # Create the edited folder if it doesn't exist.
            if not os.path.exists(edited_folder_path):
                os.mkdir(edited_folder_path)
            # Rename the edited file and move it to the edited folder.
            edited_file_new_path=os.path.join(edited_folder_path,edited_file)
            os.rename(edited_file_path,edited_file_new_path)

            # Create the name of the original file and its path.
            original_file=edited_file.replace('_E','_')
            original_file_path = os.path.join(base_path,original_file)
            if os.path.exists(original_file_path):
                # Rename the original file and move it to the edited folder.
                original_file_new_path=os.path.join(edited_folder_path,original_file)
                # original_file is os.path.basename(original_file_curr_path).
                os.rename(original_file_path, original_file_new_path)

                # Write a log entry for the moved pair of files.
                moved_pairs_list.append(f'Moved pair of files - {original_file} and {edited_file}.')
            else:
                 moved_edited_only_list.append(f"Moved file - {edited_file}. Original file not found for {edited_file}.")

        except Exception as e:
            print(f"An error occurred: {e}")
            error_list.append(f'{e}\n')

with open(edit_log_path,'a+') as edit_log:
    edit_log.write("\n".join(moved_pairs_list) + "\n\n\n" + "\n".join(moved_edited_only_list) + "\n\n\n" + "\n".join(error_list))


    


# F:\Musical World\Music Videos\^ H ^\90's
# H:\Pics\# Timeline #\2022\August 2022\New folder (4)
