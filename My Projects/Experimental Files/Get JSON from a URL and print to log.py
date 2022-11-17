from pathlib import Path
import requests
import PySimpleGUI as sg

curr_dir = Path.cwd()
print(curr_dir)

json_layout = [  [sg.T('Enter the URL from which to get JSON:')],
                 [sg.Input(key='link_for_json')],
                 [sg.B('Get JSON'),sg.B('Exit')]  ]

json_window = sg.Window('Get JSON',json_layout)#,keep_on_top=True)

while True:
    event, values = json_window.read()
    if event in ('Exit', sg.WIN_CLOSED):
        sg.popup_auto_close('Goodbye',auto_close_duration=1,no_titlebar=True)
        break
    elif event == 'Get JSON':
        page_url = values['link_for_json']
        if page_url not in ('',None):
            r = requests.get(page_url)
            json_window['link_for_json'].update('') # Updating Input Box's input to blank.
            # Below we are opening a file named json.txt in the current working directory and appending the JSON to it.
            with open(Path.joinpath(curr_dir,'json.txt'),'a',encoding='utf-8') as json_log:
                print(f'\n\n{r.json()}',file=json_log)
                # f.writelines(r.json()) # The JSON is in dictionary form so write or writelines will not work.
            # break # Commenting out break so the main window doesn't close after fetching the JSON.
            

# UnicodeEncodeError: 'charmap' codec can't encode characters
# https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
