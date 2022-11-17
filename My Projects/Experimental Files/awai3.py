from ast import arg


our_list = list(input('Please enter the number you want the squares of: '))
print(our_list)

def get_squares(*args):
    return args**2
    # return x*x

get_squares(*our_list)

# print(f'Squares of {our_list} are {list(map(get_squares, our_list))}')
# print(tuple(map(get_squares, [1,2,3,4])))
# print(set(map(get_squares, [1,2,3,4])))
# print(map(get_squares, [1,2,3,4]))

