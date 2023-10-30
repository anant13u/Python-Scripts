cities = ['Hyderabad','Bhopal','Bhilai','Raipur']

print(cities)
# ['Raipur', 'Hyderabad', 'Bhopal', 'Bhilai']

cities.reverse() #Reverses the order of items in the list.
print(cities)
# ['Raipur', 'Bhilai', 'Bhopal', 'Hyderabad']

cities.sort() # Sorting the list in alphabetical order.
print(cities)
# ['Bhilai', 'Bhopal', 'Hyderabad', 'Raipur']

# Sorting the list in reverse alphabetical order.
cities.sort(reverse=True)

print(cities.index('Bhopal')) #Returns the Index of the mentioned item (In this case 2)
# 2

# Checking if the string 'Mumbai' is present in the list 'cities'. This will return False.
print('Mumbai' in cities)
# False

# Checking if the string 'Bhilai' is present in the list 'cities'. This will return True.
print('Bhilai' in cities)
# True
