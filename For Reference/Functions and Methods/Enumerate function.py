our_string = 'Anant'

for index, letter in enumerate(our_string):
    print(f'Letter# {index} is {letter}')


# The longer method to replicate the same output as above is below:
index_count = 0

for letter in our_string:
    print(f'Letter# {index_count} is {letter}')
    index_count += 1
