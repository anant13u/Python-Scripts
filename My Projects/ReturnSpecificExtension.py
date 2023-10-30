import os
import time

def search_specific_extension():
	our_extension = input('\n Enter the extension you want the files of: ')[-3:] # [:3:] denotes last 3 characters of the string entered.
	# Can also use string.endswith() method instead of slicing in the above line.
	path = input(' Enter the directory path where you want to perform the search:\n')
	filelist = []

	for root, dir, files in os.walk(path):
		for file in files:
			# if(file.endswith(".mp4") or file.endswith(".mkv")):
			if file.find(our_extension)>-1:
				filelist.append(f' {os.path.join(root,file)}')
			#filelist.append(os.path.join(root,file))
	if filelist==[]:
		print(f'\n Sorry, we couldn\'t find any files with the extension ".{our_extension}" in "{path}"\n')
	else:
		final_list = '\n'.join(filelist)
		print(f'\n Below is the list of files with the extension ".{our_extension}" in "{path}":\n\n{final_list}\n')
	ans = input(' Do you want to perform another search? (Y/N): ')
	if ans in ('Y','y'):
		search_specific_extension()
	else:
		print(' Goodbye!\n')
		time.sleep(1.5)

search_specific_extension()


# C:\Users\AU\Videos
# C:\Users\AU\Videos\Music Videos
# /media/anant/Development
# /media/anant/Development/AU - Documents
