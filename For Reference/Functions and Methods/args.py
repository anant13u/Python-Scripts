def print_args(*args):
    print(args)

print_args(3, 98, 21, 34)
# (3, 98, 21, 34)
# *args always stores the arguments in a tuple.


def get_sum(*args):
    return sum(args)

our_sum = get_sum(3, 4, 6, 8)
print(our_sum)
# 21


def get_5_precent_of_sum(*args):
    return sum(args) * 0.05

paanch_pratishat = get_5_precent_of_sum(100, 50, 150, 200, 400)
print(paanch_pratishat)
# 45.0
