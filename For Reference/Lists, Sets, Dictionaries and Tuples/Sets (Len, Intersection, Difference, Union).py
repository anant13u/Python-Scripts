# Sets are values that are unordered and have no duplicates.

animals_list = ['lion', 'shark', 'dog', 'salmon', 'cat', 'lion', 'squirrel', 'dog']
print(animals_list)
# ['lion', 'shark', 'dog', 'salmon', 'cat', 'lion', 'squirrel', 'dog']

animals_set2 = set(animals_list) # Converting the list into a set. Notice that the duplicate values are gone in the newly created set.
print(animals_set2)
# {'cat', 'lion', 'squirrel', 'shark', 'salmon', 'dog'} # This order can change every time we print the set.

# Notice that we have entered 'lion' twice in the set but when we print the set it'll only list 'lion' once as it removes the duplicates.
animals_set = {'lion', 'shark', 'dog', 'salmon', 'cat', 'lion'}
print(animals_set)
# {'lion', 'cat', 'dog', 'shark', 'salmon'}

fishes_set = {'shark', 'tuna', 'salmon', 'goldfish'}

print(len(fishes_set))
# 4

print(fishes_set.intersection(animals_set)) # Finding the values that are in both sets.
# {'shark', 'salmon'}

print(fishes_set.difference(animals_set)) # Finding the values that are in the fishes_set but not in the animals_set.
# {'tuna', 'goldfish'}

print(fishes_set.union(animals_set)) # Finding the values that are in both sets and removing the duplicates
# {'lion', 'tuna', 'goldfish', 'salmon', 'cat', 'shark', 'dog'}

print('shark' in fishes_set)
# True

print('Manta Ray' in fishes_set)
# False

fishes_set.add('Mackerel') # Adding the value 'Mackerel' to the set.
print(fishes_set)
# {'salmon', 'goldfish', 'tuna', 'shark', 'Mackerel'}

fishes_set.clear() # Clearing the set.
print(fishes_set)
# set()
