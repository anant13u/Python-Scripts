import requests
from bs4 import BeautifulSoup
import pyperclip

# Enter the City Name
our_song = input("Enter the City Name: ")
search = f"{our_song} artist name"

# URL
url = f"https://www.google.com/search?q={search}"

# Sending HTTP request
req = requests.get(url)

# Pulling HTTP data from internet
sor = BeautifulSoup(req.text, "html.parser")
# print(sor)

# Finding temperature in Celsius
temp = sor.find("div", class_='nwVKo').heading
# pyperclip.copy(temp)
print(temp)
sor.find()

print(f'Artist of {our_song} is {temp}')
