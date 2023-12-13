from selenium import webdriver
srch = input("Please enter search query: ")
driver = webdriver.Chrome('C:/Users/AU/AppData/Local/SeleniumBasic/chromedriver.exe')
driver.maximize_window()
driver.get(f'https://www.google.com/search?q={srch}')
driver.execute_script("window.open('about:blank','secondtab');")
# It is switching to second tab now
driver.switch_to.window("secondtab")
# In the second tab, it opens Youtube:
driver.get(f'https://www.youtube.com/results?search_query={srch}')

driver.execute_script("window.open('about:blank','thirdtab');")
driver.switch_to.window("thirdtab")
driver.get(f'https://www.imdb.com/find?q={srch}')



