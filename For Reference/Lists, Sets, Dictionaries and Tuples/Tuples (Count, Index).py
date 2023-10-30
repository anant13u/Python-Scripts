# Tuples are very similar to lists. However they have one key difference - immutability.
# Once an element is inside a tuple, it cannot be reassigned, removed or appended.
# Tuples use parenthesis: (1, 2, 3)

tuple_animals = ('lion', 'cat', 'sheep', 'shark', 'shark')
print(tuple_animals)
# ('lion', 'cat', 'sheep', 'shark', 'shark')

print(tuple_animals.count('shark')) # Counting the number of times the word 'shark' appears in the tuple.
# 2

print(tuple_animals.index('cat')) # Returning the index of the word 'cat' in the tuple.
# 1

tuple_2 = ('some guy')
print(type(tuple_2))
# <class 'str'> # Python understands our tuple_2 variable as a string since it only has 1 element without any comma(s).

tuple_2=('some guy',)
print(type(tuple_2))
# <class 'tuple'>

# tuple_animals[1] = 'dog'
# print(tuple_animals)
# If you uncomment the above 2 lines and then run the code it will throw the error: "TypeError: 'tuple' 
# object does not support item assignment"


# Benefits of using a tuple over a list:

# Using a tuple instead of a list can give the programmer and the interpreter a hint that the data should not be changed.

# Tuples are commonly used as the equivalent of a dictionary without keys to store data. For Example,
# [('Swordfish', 'Dominic Sena', 2001), ('Snowden', ' Oliver Stone', 2016), ('Taxi Driver', 'Martin Scorsese', 1976)]

# The immutable nature of tuples allows them to be hashable. This means tuples can be used as keys in a dictionary.

# Tuples are generally more memory-efficient than lists. If you know you won’t need to modify the contents of your list, 
# you should use a tuple, because it will generally be faster.
