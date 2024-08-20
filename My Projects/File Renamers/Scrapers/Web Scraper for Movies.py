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


enterMovieText = sg.Text('Enter Movie Name',s=(30,2),pad=((40,20),10))
songInput = sg.I(key='-moviename-',s=(15,2),pad=(40,10))

layout = [  [enterMovieText, songInput],
            [sg.B('Search',s=(15,2),pad=(30,10)), sg.B('Exit',s=(15,2),pad=(70,10))]  ]

Window = sg.Window('Search song', layout)

while True:
    event, values = Window.read()
    # basepath = Path(values['-basepath-'])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif values['-moviename-']=='':
        sg.popup('Please specify a movie to search.')
    elif event == 'Search':
        # our_movie = values['-moviename-'].replace(' ', '-')
        our_movie = values['-moviename-']
        # search_string = f"{our_song} artist name"
        # target_url = f'https://www.google.com/search?q={search_string}'
        target_url = f'https://www.imdb.com/find/?q={our_movie}'
        
        browser = webdriver.Firefox()
        browser.get(target_url)
        # artist_name = browser.find_element(By.CSS_SELECTOR, '.iAIpCb > span:nth-child(1)')
        movie_name = browser.find_element(By.CSS_SELECTOR, 'li.find-title-result:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)')
        print(movie_name.text)
        movie_year = browser.find_element(By.CSS_SELECTOR, 'li.find-title-result:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > span:nth-child(1)')
        print(movie_year.text)
        
        # movie_name = browser.find_element(By.CSS_SELECTOR, '.xGj8Mb > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)')
        # print(movie_name.text)
        browser.close()

# Tauba Tumhare Ishare
# //*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[3]/div[2]/div[1]/div/span
# /html/body/div[3]/div/div[13]/div[2]/div/div/div[3]/div/div[1]/div/div/div[3]/div[2]/div[1]/div/span
# //*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div/div[1]/div/div
# //*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/span
# /html/body/div[3]/div/div[13]/div[2]/div/div/div[3]/div/div[1]/div/div/div[3]/div[2]/div[1]/div/span
# By.XPATH
# .xGj8Mb > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)
# .iAIpCb > span:nth-child(1)


# Error "name 'by' is not defined" using Python Selenium WebDriver
# from selenium.webdriver.common.by import By
