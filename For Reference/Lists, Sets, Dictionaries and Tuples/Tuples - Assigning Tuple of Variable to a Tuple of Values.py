from unicodedata import name


tuple1 = ('Anant', 32, 'Web Developer')

(my_name, my_age, my_profession) = tuple1 # Unpacking the tuple.

print(my_name)
# Anant
# Important thing to remember is that both tuples should have same number of elements, otherwise a ValueError 
# will occur (See example below).

(my_name, my_age, my_profession, my_city) = tuple1
# ValueError: not enough values to unpack (expected 4, got 3)

