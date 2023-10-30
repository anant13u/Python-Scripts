from math import exp, sqrt

our_list = [1, 2, 3, 4]

print(our_list)
# [1, 2, 3, 4]

squared_list = [x**2 for x in our_list]
[print(f'The square of {x} is {y}') for x, y in zip(our_list, squared_list)]
# The square of 1 is 1
# The square of 2 is 4
# The square of 3 is 9
# The square of 4 is 16

# Removing the need for declaring a separate list.
[print(f'The cube of {x} is {y}') 
 for x, y in zip(our_list,map(lambda x:x**3,our_list))]
# The cube of 1 is 1
# The cube of 2 is 8
# The cube of 3 is 27
# The cube of 4 is 64

# Removing the need for declaring a separate list.
[print(f'The cube of {x} is {x**3}') for x in our_list]
# The cube of 1 is 1
# The cube of 2 is 8
# The cube of 3 is 27
# The cube of 4 is 64

list_2 = [x**2 for x in range(10)]
print(*list_2)
# 0 1 4 9 16 25 36 49 64 81

list_3 = [3, 5, 9, 13]
[print(f'Square of {x} is {x**2}') for x in list_3]
# Square of 3 is 9
# Square of 5 is 25
# Square of 9 is 81
# Square of 13 is 169

[print(f'The square-root of {x} is {round(y,3)}') for x, y in zip(our_list,map(sqrt, our_list))]
# The square-root of 1 is 1.0
# The square-root of 2 is 1.414
# The square-root of 3 is 1.732
# The square-root of 4 is 2.0

[print(f'The square-root of {x} is {round(x**(1/2),3)}') for x in our_list]
