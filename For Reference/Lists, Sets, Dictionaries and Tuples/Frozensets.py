# Frozen sets are sets that are immutable, or sets that can't be modified once created.

list1 = [1,2,3,4,5]

frozen_set1 = frozenset(list1) # Creating a frozen set from the list.
print(frozen_set1)
# frozenset({1, 2, 3, 4, 5})

print(type(frozen_set1))
# <class 'frozenset'>

frozen_set1.add(7)
# Traceback (most recent call last):
#   File "d:\Python Projects\For Reference\Lists, Sets and Dictionaries\Frozensets.py", line 10, in <module>
#     frozen_set1.add(7)
# AttributeError: 'frozenset' object has no attribute 'add'

# Same thing happens if you try clear, pop or remove methods.
# Of course operations like difference(), intersection() and union() are still available since they are not 
# attempting to modify the content or structure of frozen sets.