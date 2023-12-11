import webbrowser, sys

# plc = input('Please enter the name of place you want to search for: ')

print('Just enter the name of any city, state or country and search for it in Google Maps: \n')
webbrowser.open('https://google.com/maps/place/' + input('Name of place you want to search for: '))

# if len(sys.argv)>1:
#     ' '.join(sys.argv[1:])

# print(sys.argv)