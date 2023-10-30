import os
import time
import shutil

def search_specific_extension():
	our_extension = input('\n Enter the extension you want the files of: ')[-3:] # [:3:] denotes last 3 characters of the string entered.
	# Can also use string.endswith() method instead of slicing in the above line.
	root_folder = input(' Enter the directory path where you want to perform the search: ')
	filelist = []

	for file in os.listdir(root_folder):
		if file.find(f'.{our_extension}')>-1: # if(file.endswith(".mp4") or file.endswith(".mkv")):
			                                  # Reason for using f'.{our_extension}' is to find files having .mp4 (for example), ignoring the files which have mp4 in middle of their names.
			filelist.append(file)
		#filelist.append(os.path.join(root,file))
	if filelist==[]:
		print(f'\n Sorry, we couldn\'t find any files with the extension ".{our_extension}" in "{root_folder}"\n')
	else:
		# final_list = '\n'.join(filelist)
		# print(f'\n Below is the list of files with the extension ".{our_extension}" in "{path}":\n\n{final_list}\n')
		print(f'\n We found {len(filelist)} files with the extension "{our_extension}" in this folder.\n')
		ans_1 = input(f' Do you want to move these files to a folder exclusively for ".{our_extension}" files? (Y/N): ')
		if ans_1 in ('Y','y'):
			new_files_path = f'{os.path.join(root_folder,our_extension.upper())} files'
			if os.path.exists(new_files_path):
				print(f'\n A folder already exists for {our_extension} files')
			else:
				os.mkdir(new_files_path)
				for file in filelist:
					shutil.move(f'{os.path.join(root_folder,file)}',new_files_path)
				print(f'\n All {our_extension} files have been moved to a new folder - "{new_files_path}"')
	ans = input('\n Do you want to perform another search & move? (Y/N): ')
	if ans in ('Y','y'):
		search_specific_extension()
	else:
		print('\n Goodbye!\n')
		time.sleep(1.5)

search_specific_extension()


# C:\Users\AU\Videos
# C:\Users\AU\Videos\Music Videos