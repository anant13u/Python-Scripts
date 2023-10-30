# Lists always start with square brackets - [], separated by commas, and are mutable.

cities = ['Hyderabad', 'Bhopal', 'Bhilai', 'Raipur']

print(cities)
# ['Hyderabad', 'Bhopal', 'Bhilai', 'Raipur']

print(len(cities)) # Returning the number of items in the list.
# 4

print(cities[1])  # Retrieving the item on the list having Index 1.
# Bhopal

print(cities[0:2]) # Returning the items from the list starting from Index 0 (Hyderabad) till but excluding Index 2 (Bhilai).
# ['Hyderabad', 'Bhopal']

print(cities[:2]) # Same as above.
# ['Hyderabad', 'Bhopal']

# Returns the items from the list starting from Index 1 (Bhopal) till the last item on the list.
print(cities[1:])
# ['Bhopal', 'Bhilai', 'Raipur']

cities.append('Mumbai') # Adding the item 'Mumbai' to the end of the list.
cities.insert(1, 'Shimla') # Inserting the item 'Shimla' at Index 1.
print(cities)
# ['Hyderabad', 'Shimla', 'Bhopal', 'Bhilai', 'Raipur', 'Mumbai']

cities_2 = ['Melbourne', 'Sydney']  # Introducing a 2nd list.
cities.extend(cities_2) # Adding the items from the list `cities_2` to the end of the list `cities`.
print(cities)
# ['Hyderabad', 'Shimla', 'Bhopal', 'Bhilai', 'Raipur', 'Mumbai', 'Melbourne', 'Sydney']

cities.remove('Raipur')  # Removing the item 'Raipur' from the list.
print(cities)
# ['Hyderabad', 'Shimla', 'Bhopal', 'Bhilai', 'Mumbai', 'Melbourne', 'Sydney']

cities.remove(cities[2])  # Removing the item on the list having Index 2.
print(cities)
# ['Hyderabad', 'Shimla', 'Bhilai', 'Mumbai', 'Melbourne', 'Sydney']

cities.pop()  # Removing the last item on the list.
print(cities)
# ['Hyderabad', 'Shimla', 'Bhilai', 'Mumbai', 'Melbourne']

# Removing the last item on the list and storing it in a variable called popped_item.
popped_item = cities.pop()
print(popped_item)
# Melbourne

cities.append('Bhilai') # Adding the item 'Bhilai' to the end of the list. 
print(cities.count('Bhilai')) # Counting the number of times the item 'Bhilai' is present in the list.
# 2
