import os
from pathlib import Path
import PySimpleGUI as sg
from openpyxl import Workbook
from datetime import datetime

sg.theme('Darkblue12')
# sg.theme_previewer()


def create_excel(basepath, filelist, Window):
    # Create a new Excel workbook and select the active sheet
    wb = Workbook()
    ws = wb.active # Or you can use the below line as well, fetches the first worksheet.
    # sheet = workbook.worksheets[0]

    # Write the list items to the Excel sheet column
    # row_number = 1  # Specify the row number where you want to display the data
    for list_item in filelist:
        # sheet.cell(row=row_number, column=1, value=list_item)
        # row_number += 1
        ws.append(list_item)

    
    # Auto-adjust column width
    for column in ws.columns:
        max_length = 0
    # column = sheet['A']
        for cell in column:
            if len(str(cell.value))>max_length:
                max_length=len(str(cell.value))
        max_length = max_length + 2
    # sheet.column_dimensions['A'].width = adjusted_width
        ws.column_dimensions[column[0].column_letter].width = max_length


    try:
        curr_date_time = datetime.now().strftime('%d-%m-%Y %H_%M_%S')
        # Save the workbook to a file
        wb.save(Path(basepath,f'Files from {Path(basepath).name} ({curr_date_time}).xlsx'))
    except PermissionError:
        sg.popup('The output Excel file is already open. Please close and try again.')
    # Window.reappear()

    # mains()


def mains():
    selectFolderText = sg.Text('Select Folder', s=(30,2), pad=((40,20),10))
    folderBrowse = sg.FolderBrowse(key='-basepath-', s=(15,2), pad=(40,15))
    includeRadio = sg.Radio('Include File Size', 'size_group', k='-includesize-', pad=((100,30),15))
    excludeRadio = sg.Radio('Exclude File Size', 'size_group', default=True, k='-excludesize-')
    generateButton = sg.B('Generate List',s=(15,2),pad=((80,30),25))

    layout = [  [selectFolderText, folderBrowse],
                [sg.HorizontalSeparator()],
                [includeRadio, excludeRadio],
                [sg.HorizontalSeparator()],
                [generateButton, sg.B('Exit',s=(15,2),pad=(70,10))]  ]

    Window = sg.Window('Generate list of files', layout, keep_on_top=True, grab_anywhere=True)

    while True:
        event, values = Window.read()
        basepath = Path(values['-basepath-'])
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif values['-basepath-']=='':
            sg.popup('Please select a folder to perform operations in.')
        elif event == 'Generate List':
            filelist=[]
            print(basepath)
            if values['-includesize-']:
                filelist.append(['File Name','File Size (in MB)','File Type','Full Path'])
                for root, dirs, files in os.walk(basepath):
                    # filelist.append(f'There are {len(dirs)} folders and {len(files)} files in {root}\n')
                    for entry in os.listdir(root):
                        if Path(root, entry).is_file():
                            file_size = os.path.getsize(Path(root, entry))/(1024*1024) # file_size is 5.0469865798950195
                            file_extension = Path(root, entry).suffix
                        else:
                            file_size = 0
                            file_extension = 'Folder'
                        filelist.append([entry, round(file_size, 2), file_extension, str(Path(root, entry))]) # .replace(".","")
                        # if len(str(Path(root, entry)))>218:
                        #     print(str(Path(root, entry)))
            else:
                filelist.append(['File Name','File Type','Full Path'])
                for root, dirs, files in os.walk(basepath):
                    for entry in os.listdir(root):
                        if Path(root, entry).is_file():
                            file_extension = Path(root, entry).suffix
                        else:
                            file_extension = 'Folder'
                        filelist.append([entry, file_extension, str(Path(root, entry))])

            create_excel(basepath, filelist, Window)


mains()


            # for dir in dirs:
            #     filelist.append(f'\nParent Directory: {Path(root,dir)}')
            #     for entry in os.listdir(Path(root,dir)):
            #         filelist.append(entry)


# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)
