our_string = 'Anant upadhyay'

print(our_string.upper()) # Converting the string to uppercase.
# ANANT UPADHYAY

print(our_string.lower()) # Converting the string to lowercase.
# anant upadhyay

print(our_string.split()) # Splitting the string based on the separator (' ' by default).
# ['Anant', 'upadhyay']

print(our_string.split('a')) # Splitting the string based on the separator 'a'.
# ['An', 'nt up', 'dhy', 'y']

print(our_string.find('t')) # Finding the index of the first occurence of the character 't' in the string.
# 4

new_string = our_string.replace('Anant', 'A') # Replacing the first occurence of the string 'Anant' with the string 'A'.
print(new_string)
# A upadhyay

print(our_string.count('a')) # Counting the number of occurences of the character 'a' in our_string.
# 3
