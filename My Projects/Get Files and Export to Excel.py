import os
from pathlib import Path
import PySimpleGUI as sg
import openpyxl

sg.theme('Reddit')

filelist=[]

layout = [  [sg.Text('Select Folder',s=(30,3),pad=((40,20),10),justification="center"), sg.FolderBrowse(key='-basepath-',s=(15,2),pad=(40,10))],
            # [sg.Radio('Full name?','1')],
			[sg.B('Generate List',s=(15,2),pad=((100,30),10)), sg.B('Exit',s=(15,2),pad=(70,10))]  ]

Window = sg.Window('Generate list of files', layout)

while True:
    event, values = Window.read()
    basepath = Path(values['-basepath-'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif basepath == None or basepath=='':
        sg.popup('Path cannot be blank.')
    elif event == 'Generate List':
        # Window.close()
        for root, dirs, files in os.walk(basepath):
            filelist.append(f'There are {len(dirs)} folders and {len(files)} files in {root}\n'
                            f'{root}')
            for entry in os.listdir(root):
                filelist.append(entry)

            # for dir in dirs:
            #     filelist.append(f'\nParent Directory: {Path(root,dir)}')
            #     for entry in os.listdir(Path(root,dir)):
            #         filelist.append(entry)
            filelist.append('\n')
        filelist = '\n'.join(filelist)
        sg.popup_scrolled(filelist, title='Filelist')

        # Create a new Excel workbook and select the active sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Write the list items to the Excel sheet column
        row_number = 1  # Specify the column number where you want to display the data
        for list_item in filelist.split('\n'):
            sheet.cell(row=row_number, column=1, value=list_item)
            row_number += 1
        
        # Auto-adjust column width
        max_length = 0
        column = sheet['A']
        for cell in column:
            if len(str(cell.value))>max_length:
                max_length=len(cell.value)
        adjusted_width = max_length+1
        sheet.column_dimensions['A'].width = adjusted_width

        # Save the workbook to a file
        workbook.save(Path(basepath,f'Files from {Path(basepath).name}.xlsx'))



# current_file_size = round(os.path.getsize(current_file)/(1024*1024),2)
