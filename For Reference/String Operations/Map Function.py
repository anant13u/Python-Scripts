
from operator import add


x, z = map(str,(1,2)) # Converting the numbers 1 and 2 to strings and assigning them to the variables x and z.
print(f'The numbers in string format are {x + z}')

list_of_nums = [1,3,5,7,9]

xx,cc,vv,bb,nn = map(add(1),list_of_nums)
print(cc)

print(min(list_of_nums))
