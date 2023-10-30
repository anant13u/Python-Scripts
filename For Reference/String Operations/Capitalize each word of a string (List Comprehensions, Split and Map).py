our_string = 'anant upadhyay'
print(our_string)
# anant upadhyay

a_string = our_string.split() # One way to convert a string to a list (based on the separator, ' ' by default).
print(a_string)
# ['anant', 'upadhyay']

# Method 1:
b_string=[]
for word in a_string:
    b_string.append(word.capitalize())
print(*b_string)
# Anant Upadhyay

# Method 2 (Notice the square brackets indicating we're denoting c_string as a list):
c_string = [word.capitalize() for word in a_string]
print(*c_string)
# Anant Upadhyay

# Method 3 (Further compressing Method 2 into a one-liner):
print(' '.join((word.capitalize() for word in a_string)))
# Anant Upadhyay

# Method 4 (Using the map function):
print(' '.join(map(str.capitalize, our_string.split(' '))))
