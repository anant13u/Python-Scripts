from difflib import Differ
from difflib import HtmlDiff
from difflib import SequenceMatcher

file1 = "D:\Python\For Reference\File Operations (OS Pathlib Glob etc)\File Operations - Test Folder\Jaws 3 - Longer.txt"
file2 = "D:\Python\For Reference\File Operations (OS Pathlib Glob etc)\File Operations - Test Folder\Jaws 3.txt"

with open(file1) as f1, open(file2) as f2:
    # d1 = Differ().compare(f1.readlines(), f2.readlines())
    # print('\n'.join(d1))
    
    #d2 = SequenceMatcher(None, f1.read(), f2.read()).quick_ratio()
    #print(d2)
    #print("There is a %.2f percent match!" % (d2 * 100))

    d3 = HtmlDiff().make_file(fromlines = f1.readlines(), tolines = f2.readlines(), fromdesc = 'file1', todesc = 'file2')
    print(d3, file = open(r'D:\Python\For Reference\File Operations (OS Pathlib Glob etc)\File Operations - Test Folder\result.html', "w"))
