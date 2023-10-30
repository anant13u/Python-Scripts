names = ['Anant','Pratiksha','Sourabh','Tushar','Sumalya']

print(names)
# ['Anant', 'Pratiksha', 'Sourabh', 'Tushar', 'Sumalya']

print(*names)
# Anant Pratiksha Sourabh Tushar Sumalya

print(*names,sep=' and ', end='. Bas itne hi log hain.\n')
# Anant and Pratiksha and Sourabh and Tushar and Sumalya. Bas itne hi log hain.

names_str = ', '.join(names) #Here we used a Join function to join ', ' to every item on the 'names' list.
print (names_str)
# Anant, Pratiksha, Sourabh, Tushar, Sumalya


nms = "\n\n".join(names)
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


for index, ds in enumerate(names, start = 1): #start = 1 tells the code to start indexing with number 1.
    print(index, ds)
# 1 Anant
# 2 Pratiksha
# 3 Sourabh
# 4 Tushar
# 5 Sumalya


new_names = names_str.split(', ') #This split method can be used to split the items of an existing list using the seperator we provide.
print(new_names)
# ['Anant', 'Pratiksha', 'Sourabh', 'Tushar', 'Sumalya']

