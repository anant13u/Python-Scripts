import os
from pathlib import Path

base_path = input('Please enter the path where you want to search for Edited Photos and Videos: \n')
curr_folder = os.path.basename(base_path)
# Create paths for the edited folder and log file.
edited_folder_path = os.path.join(base_path,f'Edited Photos and Videos ({curr_folder})')
curr_log_path = os.path.join(edited_folder_path,'Original and Edited Photos and Videos log.txt')

entries = os.listdir(base_path)

moved_pairs_list = ['Below is the list of moved pairs of media:\n']
moved_edited_only_list = ['Below is the list of moved edited media (original file was not found):\n']
error_list = ['Below are the errors encountered:\n']

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

with open(curr_log_path,'a+') as curr_log:
    log_text = "\n".join(moved_pairs_list) + "\n\n\n" + "\n".join(moved_edited_only_list) + "\n\n\n" + "\n".join(error_list)
    curr_log.write(log_text)

# F:\Musical World\Music Videos\^ H ^\90's
# H:\Pics\# Timeline #\2022\August 2022\New folder (4)
