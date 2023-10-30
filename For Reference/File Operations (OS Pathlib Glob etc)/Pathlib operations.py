import pathlib
from pathlib import Path

our_file = 'D:\Python\My Projects\Testing Grounds\Testing for moving files\Danny Avila - Breaking Your Fall (Sick Individuals Remix).mp3'

print(Path(our_file))
# D:\Python\My Projects\Testing Grounds\Testing for moving files\Danny Avila - Breaking Your Fall (Sick Individuals Remix).mp3

print(Path(our_file).absolute())
# D:\Python\My Projects\Testing Grounds\Testing for moving files\Danny Avila - Breaking Your Fall (Sick Individuals Remix).mp3

print(Path(our_file).name)
# Danny Avila - Breaking Your Fall (Sick Individuals Remix).mp3

print(Path(our_file).suffix)
# .mp3

print(Path(our_file).anchor)
# D:\

print(Path(our_file).drive)
# D:

# To get just the foler name of provided filename.
print(Path(our_file).parent.name)
# Testing for moving files


# pathlib.Path('D:\\Python\\My Projects\\Testing Grounds\\Testing for moving files\\PDF files\\_588121_-999_00-_1.pdf').rename('D:\Python\My Projects\Testing Grounds\Testing for moving files\_588121_-999_00-_1.pdf')