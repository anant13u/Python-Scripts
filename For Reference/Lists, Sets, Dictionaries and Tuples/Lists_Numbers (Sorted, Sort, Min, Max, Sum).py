num = [7, 6, 1, 4, 89, 32, 2]

print(num)
# [7, 6, 1, 4, 89, 32, 2]

# Using the function sorted you can display the sorted version of a list without ACTUALLY sorting/changing the original list.
sorted_num = sorted(num)
print(sorted_num)
# [1, 2, 4, 6, 7, 32, 89]

num.sort() # Sorting the list in place. This method will sort the list 'in place'. No need to store it in a variable.
print(num)
# [1, 2, 4, 6, 7, 32, 89]

print(min(num))  # Return the smallest item from the list
# 1

print(max(num))  # Return the largest item from the list
# 89

print(sum(num))  # Return the sum of all items in the list
# 141

print(sum(num)/len(num)) # Finding the average of the list.
# 20.142857142857142
