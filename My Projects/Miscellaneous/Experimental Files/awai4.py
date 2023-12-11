import requests

url = "https://unogsng.p.rapidapi.com/genres"

headers = {
    "X-RapidAPI-Host": "unogsng.p.rapidapi.com",
    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
