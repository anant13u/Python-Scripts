print(range(10))
# range(0, 10) # The output is range(0, 10) since range produces a generator.

# To get a list out of the range function we will have to use the list method.
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in range(7): # This will print all numbers starting from 0 till 6 (7 will be excluded).
    print(num)
# 0
# 1
# 2
# 3
# 4
# 5
# 6

for num in range(4,10):
    print(num)
# 4
# 5
# 6
# 7
# 8
# 9

for num in range(3,10,2):
    print(num)
# 3
# 5
# 7
# 9