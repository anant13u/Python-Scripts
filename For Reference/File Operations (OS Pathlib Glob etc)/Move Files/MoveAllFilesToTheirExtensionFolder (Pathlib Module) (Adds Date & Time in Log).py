import os
import time
from pathlib import Path
import contextlib
from datetime import datetime


def perform_another_search():
	"""
	If the user wants to perform another search, then call the search_specific_extension() function,
	otherwise print a goodbye message and exit the program.
	"""
	ans_3 = input('\n Do you want to perform another search & move? (Y/N): ')
	if ans_3 in ('Y','y'):
		search_specific_extension()
	else:
		print('\n Goodbye!\n')
		time.sleep(1.5)

def search_specific_extension():
	"""
	It will move all the files in the root folder to their respective extension folders.
	"""
	root_folder = Path(input('\n Enter the directory path where you want to perform the search & move: '))
	undo_list = [] # Creating this list so user can undo the move later on by moving the files from their extension folders back to the root folder.

	ans_1 = input(' Do you want to move all the files in this folder exclusively created for their extension? (Y/N): ')
	if ans_1 in ('Y','y'):
		# Below we are iterating through the root folder and checking if the entry is a file or not. If it is a file, it
		# will move it to its respective extension folder.
		moved_list = [] # This list will come handy while creating the log.
		exception_list = []
		for entry in os.listdir(root_folder):
			curr_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			# Below we make sure we don't move log and exception log files in the move. They need to be in the root folder.
			if Path.joinpath(root_folder,entry).is_file() and entry not in ('log.txt','exception.txt'):
				our_extension = Path(entry).suffix
				new_file_path = Path.joinpath(root_folder,f'{our_extension.upper()[1:]} files') # our_extension.upper()[1:] is ignoring the "." in the extension and taking the rest of it. Works on extensions of all lengths.
				if os.path.exists(new_file_path):
					if Path(Path.joinpath(new_file_path,entry)).exists():
						exception_list.append(f'{curr_date_time} - A file with name: {entry} already exists in {new_file_path}.\nNo action will be taken on this file.\n')
						# print(Path.joinpath(new_file_path,entry))
						# print(f' A file with name: {entry} already exists in {new_file_path}, no action will be taken on this file.\n')
					else:
						Path.joinpath(root_folder,entry).rename(Path.joinpath(new_file_path,entry))
						undo_list.append(Path.joinpath(new_file_path, entry))
						moved_list.append(f'{curr_date_time} - Moved "{entry}" from <{root_folder}> to <{new_file_path}>.')
						# print(f'\n Moved "{entry}" from <{root_folder}> to <{new_file_path}>.\n')
				else:
					os.mkdir(new_file_path)
					Path.joinpath(root_folder,entry).rename(Path.joinpath(new_file_path,entry))
					# undo_list.append(new_file_path)
					# undo_list.append(Path.joinpath(new_file_path, entry))
					undo_list.extend((new_file_path, Path.joinpath(new_file_path, entry)))
					moved_list.append(f'{curr_date_time} - "{new_file_path}" created.\n Moved "{entry}" from <{root_folder}> to <{new_file_path}>.')
			else:
				moved_list.append(f'{curr_date_time} - "{entry}" is not a file, no action will be taken on it.\n')
		print('\n All the files have been moved to their respective extension folders now. Check the log file in the root folder.')

		with open(f'{root_folder}\log.txt', 'w+') as log_file: # The w+ argument will create a new text file in write mode.
			log_file.write('\n'.join(moved_list)) # Creating a log file and logging the move actions in it.
		if exception_list != []:
			with open(f'{root_folder}\exception.txt', 'w+') as exception_file:
				exception_file.write('\n'.join(exception_list))
		ans_2 = input(' If you want to undo the move, press Y, or else press N to quit: (Y/N) ') # Checking to see if the user wants to undo the move.
		if ans_2 in ('Y','y'):
			for file in undo_list:
				if Path(Path.joinpath(root_folder,Path(file).name)).exists():
					exception_list.append(f'A file with name: {Path(file).name} already exists in {root_folder}.\nNo action will be taken on this file.\n')
				else:
					Path(file).rename(Path.joinpath(root_folder,Path(file).name)) # Returning all files back to root folder.
			print('\n All files have been moved back to the root folder.')
			# Below we are iterating through the undo_list and checking if the entry is a directory or not. If it is a
			# directory we created just now in above move operation, it will delete it.
			for entry in undo_list:
				if Path(entry).is_dir():
					with contextlib.suppress(OSError):
						Path.rmdir(entry)
			print(' Also, all folders created in the above move have been deleted.')
	perform_another_search()

search_specific_extension()


# The path to the folder where I want to perform the search & move.
# C:\Users\AU\Videos
# C:\Users\AU\Videos\Music Videos
