import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime

sg.theme('Reddit')
# sg.theme_previewer()


enterSongText = sg.Text('Enter Song Name',s=(30,2),pad=((40,20),10))
songInput = sg.I(key='-songname-',s=(15,2),pad=(40,10))

layout = [  [enterSongText, songInput],
            [sg.B('Search',s=(15,2),pad=(30,10)), sg.B('Exit',s=(15,2),pad=(70,10))]  ]

Window = sg.Window('Search song', layout)

while True:
    event, values = Window.read()
    # basepath = Path(values['-basepath-'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['-songname-']=='':
        sg.popup('Please specify a song to search.')
    elif event == 'Search':
        our_song = values['-songname-'].replace(' ', '-')
        # search_string = f"{our_song} artist name"
        # target_url = f'https://www.google.com/search?q={search_string}'
        target_url = f'https://gaana.com/song/{our_song}'
        
        browser = webdriver.Firefox()
        browser.get(target_url)
        artist_name = browser.find_element(By.CSS_SELECTOR, 'h1.title')
        print(artist_name.text)
        artist_name = browser.find_element(By.CSS_SELECTOR, '.iAIpCb > span:nth-child(1)')
        print(artist_name.text)
        # movie_name = browser.find_element(By.CSS_SELECTOR, '.xGj8Mb > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)')
        # print(movie_name.text)
        browser.close()

# Tauba Tumhare Ishare


# Error "name 'by' is not defined" using Python Selenium WebDriver
# from selenium.webdriver.common.by import By
