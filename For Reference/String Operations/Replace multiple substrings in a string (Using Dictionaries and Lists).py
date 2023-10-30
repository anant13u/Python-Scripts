
video_name = 'Kaal in a "Nutshell" |/|\| Yogi Baba'
replacers_list = ['|', ':', '/', '\\', '"', '*', '?', '<', '>']

video_name_2 = 'If <Godzilla> Was In Jurassic World ?*: | ParkDub'
replacers_dict = {'|':'-', ':':'', '/':'', '\\':'', '"':'', '*':'', '?':'', '<':'', '>':'', '  ':' '}

# Method 1 - Iterating through the list of unallowed symbols in the replacers list.
for unallowed_symbol in replacers_list:
    if unallowed_symbol in video_name:
        video_name = video_name.replace(unallowed_symbol,'')
print(f'\n Video name: "{video_name}"')

# Method 2 - Iterating through the dictionary (replacers_dict) and replacing the key with the value.
for key, value in replacers_dict.items():
    video_name_2 = video_name_2.replace(key,value)
print(f'\n Video name: "{video_name_2}"')

# print(video_name)
# print(video_name_2)
