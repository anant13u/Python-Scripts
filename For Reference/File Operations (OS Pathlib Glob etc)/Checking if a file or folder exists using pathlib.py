from pathlib import Path

our_file = 'D:\Python\My Projects\Testing Grounds\Testing for moving files\Danny Avila - Breaking Your Fall (Sick Individuals Remix).mp3'
our_folder = 'D:\Python\My Projects\Testing Grounds\Testing for moving files'

if Path(our_file).is_file():
    print(f'{Path(our_file).name} exists and is a file.')
else:
    print(f'{Path(our_file).name} either does not exist or is a folder.')


if Path(our_folder).is_file():
    print(f'{Path(our_folder).name} exists and is a file.')
else:
    print(f'{Path(our_folder).name} either does not exist or is a folder.')

# We can also use below code to check the same thing:

if Path(our_file).exists():
    print(f'{Path(our_file).name} exists')

if Path(our_folder).exists():
    print(f'{Path(our_folder).name} exists')
