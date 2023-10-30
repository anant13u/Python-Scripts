import os

# E:\Torrents\Python and Excel and Others\Python 3 Complete Masterclass - Make Your Job Tasks Easier!

path = 'D:\Python\Git & GitHub'
filelist=[]

[filelist.append(os.path.join(root,file)) for root, dirs, files in os.walk(path) for file in files] # List comprehension is used.

print(*filelist)
# D:\Python\Git & GitHub\desktop.ini D:\Python\Git & GitHub\explanation.png D:\Python\Git & GitHub\Git.txt D:\Python\Git & GitHub\lifecycle.png D:\Python\Git & GitHub\QaeAZ.png

# Method 1 to display contents of filelist, each in new line.
print(*filelist, sep='\n')
# D:\Python\Git & GitHub\desktop.ini
# D:\Python\Git & GitHub\explanation.png
# D:\Python\Git & GitHub\Git.txt
# D:\Python\Git & GitHub\lifecycle.png
# D:\Python\Git & GitHub\QaeAZ.png

# Method 2 to display contents of filelist, each in new line.
print('\n'.join(filelist))
# D:\Python\Git & GitHub\desktop.ini
# D:\Python\Git & GitHub\explanation.png
# D:\Python\Git & GitHub\Git.txt
# D:\Python\Git & GitHub\lifecycle.png
# D:\Python\Git & GitHub\QaeAZ.png

# Method 3 to display contents of filelist, each in new line.
for name in filelist:
    print(name)
# D:\Python\Git & GitHub\desktop.ini
# D:\Python\Git & GitHub\explanation.png
# D:\Python\Git & GitHub\Git.txt
# D:\Python\Git & GitHub\lifecycle.png
# D:\Python\Git & GitHub\QaeAZ.png

# Method 4 to display contents of filelist, each in new line.
[print(os.path.join(root,file)) for root, dirs, files in os.walk(path) for file in files] # List comprehension is used.
# D:\Python\Git & GitHub\desktop.ini
# D:\Python\Git & GitHub\explanation.png
# D:\Python\Git & GitHub\Git.txt
# D:\Python\Git & GitHub\lifecycle.png
# D:\Python\Git & GitHub\QaeAZ.png

# Example Folder path - D:\Python\My Projects\Mass File Renamer
