import os

curr_path = r'C:\Users\AU\Videos\Crypto'

# Using a for loop to get all the filenames printed using os.walk method.
for root, dirs, files in os.walk(curr_path, topdown=True):
    for file in files:
        print(os.path.join(root, file))
# D:\Python\.idea\.gitignore
# D:\Python\.idea\misc.xml
# D:\Python\.idea\modules.xml
# D:\Python\.idea\Python.iml
# D:\Python\.idea\workspace.xml
# D:\Python\.idea\inspectionProfiles\profiles_settings.xml

print('\n')

# List comprehension is used to achieve the same result as above.
[print(os.path.join(root,file)) for root, dirs, files in os.walk(curr_path) for file in files]
# D:\Python\.idea\.gitignore
# D:\Python\.idea\misc.xml
# D:\Python\.idea\modules.xml
# D:\Python\.idea\Python.iml
# D:\Python\.idea\workspace.xml
# D:\Python\.idea\inspectionProfiles\profiles_settings.xml
