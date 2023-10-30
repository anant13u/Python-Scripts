import os
import pathlib
import time
import shutil
from pathlib import Path, PurePath

def search_specific_extension():
	our_extension = input('\n Enter the extension you want the files of: ')[-3:] # [:3:] denotes last 3 characters of the string entered.
	# Can also use string.endswith() method instead of slicing in the above line.
	root_folder = Path(input(' Enter the directory path where you want to perform the search: '))
	filelist = []

	for entry in os.listdir(root_folder):
		if Path(entry).suffix==f'.{our_extension}': # if(file.endswith(".mp4") or file.endswith(".mkv")):
			filelist.append(entry)
		#filelist.append(os.path.join(root,file))
	if filelist==[]:
		print(f'\n Sorry, we couldn\'t find any files with the extension ".{our_extension}" in "{root_folder}"')
	else:
		# print(f'\n Below is the list of files with the extension ".{our_extension}" in "{path}":\n\n{final_list}\n')
		print(f'\n We found {len(filelist)} files with the extension ".{our_extension}" in this folder.\n')
		ans_1 = input(f' Do you want to move these files to a folder exclusively for ".{our_extension}" files? (Y/N): ')
		if ans_1 in ('Y','y'):
			# new_folder = f'{our_extension.upper()} files'
			new_files_path = Path.joinpath(root_folder,f'{our_extension.upper()} files')
			if os.path.exists(new_files_path):
				print(f'\n A folder already exists for {our_extension} files')
				for file in filelist:
					Path(Path.joinpath(root_folder,file)).rename(Path.joinpath(new_files_path,file))
				print(f'\n All remaining {our_extension} files have been moved to the already existing folder - "{new_files_path}"')
			else:
				os.mkdir(new_files_path)
				for file in filelist:
					Path(Path.joinpath(root_folder,file)).rename(Path.joinpath(new_files_path,file))
				print(f'\n All {our_extension} files have been moved to a new folder - "{new_files_path}"')
	ans_2 = input('\n Do you want to perform another search & move? (Y/N): ')
	if ans_2 in ('Y','y'):
		search_specific_extension()
	else:
		print('\n Goodbye!\n')
		time.sleep(1.5)

search_specific_extension()


# C:\Users\AU\Videos
# C:\Users\AU\Videos\Music Videos