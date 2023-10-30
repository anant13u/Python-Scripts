import pathlib
from pathlib import Path

our_file = 'D:\Python\My Projects\Testing Grounds\Testing for moving files\PDF files\coffee_break_python_slicing.pdf'

print(Path(our_file))
# D:\Python\My Projects\Testing Grounds\Testing for moving files\PDF files\coffee_break_python_slicing.pdf

print(Path(our_file).name)
# coffee_break_python_slicing.pdf

print(Path(our_file).suffix)
# .pdf

print(Path(our_file).absolute())
# D:\Python\My Projects\Testing Grounds\Testing for moving files\PDF files\coffee_break_python_slicing.pdf

print(Path(our_file).anchor)
# D:\

print(Path(our_file).drive)
# D:

# pathlib.Path('D:\\Python\\My Projects\\Testing Grounds\\Testing for moving files\\PDF files\\_588121_-999_00-_1.pdf').rename('D:\Python\My Projects\Testing Grounds\Testing for moving files\_588121_-999_00-_1.pdf')