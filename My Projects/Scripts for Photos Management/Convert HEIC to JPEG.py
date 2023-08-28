# Import the required libraries
import os
from pathlib import Path
from pillow_heif import register_heif_opener
from PIL import Image

# Register the HEIF opener with the PIL library
register_heif_opener()

# Get the base path from the user
base_path = input('Please enter the path where you want to search for Live Photos, PNG Files and AAE Files: \n')

# Extract the current folder name from the base path
curr_folder = os.path.basename(base_path)

# Create paths for various folders using the current folder name
heic_folder_path = os.path.join(base_path, f'HEIC to JPEG ({curr_folder})')

entries = os.listdir(base_path)
# print(entries)

# Loop through each file in the 'entries' list
for file in entries:
    # Create the full path to the current file
    curr_file_path = os.path.join(base_path, file)
    # Get the size of the file in megabytes
    file_size = os.path.getsize(curr_file_path) / (1024 * 1024)
    # Check if the current path points to a file and if the file has a .heic extension (case-insensitive)
    if Path(curr_file_path).is_file() and Path(curr_file_path).suffix.lower() == '.heic':
        # Create the HEIC folder if it doesn't exist
        if not os.path.exists(heic_folder_path):
            os.mkdir(heic_folder_path)
        # Open the HEIC image using the Image class from the PIL library
        image = Image.open(curr_file_path)
        # Construct the path for the JPEG output file by replacing '.HEIC' with '.jpg'
        jpeg_path = os.path.join(heic_folder_path, f'{file}.jpg'.replace('.HEIC', ''))
        # Save the opened image as a JPEG file
        image.save(jpeg_path, format='JPEG')

        new_file_path=os.path.join(heic_folder_path,file)
        os.rename(curr_file_path,new_file_path)

    

# F:\Musical World\Music Videos\^ H ^\90's
# H:\Pics\# Timeline #\2022\August 2022\New folder (4)
