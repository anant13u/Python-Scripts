# 2 Modules crucial for web scraping - Beautiful Soup and Requests

# Installing Requests on Windows and macOS
# pip install requests

# Installing beautifulsoup4 on Windows and macOS
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://webscraper.io/test-sites/e-commerce/static")

print(type(webpage)) #This will give us the type of object 'webpage' is.

text = webpage.text
print(type(text))

print(text)