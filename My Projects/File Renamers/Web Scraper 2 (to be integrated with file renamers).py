import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import PySimpleGUI as sg
from datetime import datetime
import subprocess

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
        our_song = values['-songname-']
        search_string = f"{our_song} artist name"
        target_url = f'https://www.google.com/search?q={search_string}'
        browser = webdriver.Firefox()
        browser.get(target_url)
        # element = browser.find_element(By.XPATH, '//*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/span')
        element = browser.find_element(By.CSS_SELECTOR, '.iAIpCb > span:nth-child(1)')
        print(element)
        print(element.text)
        browser.close()

# Tauba Tumhare Ishare
# //*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[3]/div[2]/div[1]/div/span
# /html/body/div[3]/div/div[13]/div[2]/div/div/div[3]/div/div[1]/div/div/div[3]/div[2]/div[1]/div/span
# //*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div/div[1]/div/div
# //*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/span
# /html/body/div[3]/div/div[13]/div[2]/div/div/div[3]/div/div[1]/div/div/div[3]/div[2]/div[1]/div/span
# By.XPATH

# .iAIpCb > span:nth-child(1)


# Error "name 'by' is not defined" using Python Selenium WebDriver
# from selenium.webdriver.common.by import By
