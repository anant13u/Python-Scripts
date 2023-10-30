names = ['Anant','Pratiksha','Sourabh','Tushar','Sumalya']

print(names)
# ['Anant', 'Pratiksha', 'Sourabh', 'Tushar', 'Sumalya']

print(*names)
# Anant Pratiksha Sourabh Tushar Sumalya

print(*names,sep=' and ', end='. Bas itne hi log hain.\n')
# Anant and Pratiksha and Sourabh and Tushar and Sumalya. Bas itne hi log hain.

names_str = ', '.join(names) # Joining the items of the list with a comma and a space.
print (names_str)
# Anant, Pratiksha, Sourabh, Tushar, Sumalya

nms = '\n\n'.join(names) # Joining the items of the list with a new line.
print(nms)
# Anant

# Pratiksha

# Sourabh

# Tushar

# Sumalya


for x in names:
    print(x)
# Anant
# Pratiksha
# Sourabh
# Tushar
# Sumalya


for index, ds in enumerate(names): #Enumerate function helps in retrieving the index numbers for the list.
    print(index, ds)
# 0 Anant
# 1 Pratiksha
# 2 Sourabh
# 3 Tushar
# 4 Sumalya


# A for loop that is iterating over the list `names` and enumerating the items in the list. The
# enumerate function helps in retrieving the index numbers for the list. The `start` parameter is used
# to set the starting index value (1 in this case).
for index, ds in enumerate(names, start = 1):
    print(index, ds)
# 1 Anant
# 2 Pratiksha
# 3 Sourabh
# 4 Tushar
# 5 Sumalya


# The `split` function is used to split the string into a list. The `split` function takes a delimiter
# as an argument. In this case, the delimiter is a comma and a space.
new_names = names_str.split(', ')
print(new_names)
# ['Anant', 'Pratiksha', 'Sourabh', 'Tushar', 'Sumalya']

