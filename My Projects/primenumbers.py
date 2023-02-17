my_num = int(input('Enter a number:\n'))
mynum_is_prime = False # We use this variable as a flag to determine whether or not our number is a prime number.

if my_num == 1:
    print('Neither prime nor composite')
elif my_num == 2:
    print('prime')
else:
    for i in range(2,my_num):
        if my_num % i == 0: # If the remainder is 0 it means we have found a number that my_num is completely divisible by.
            mynum_is_prime = False
            break # We use break since once we've found a number that my_num is divisible by then our number is not a prime number.
        else:
            mynum_is_prime = True

    if mynum_is_prime == True:
        print(f'{my_num} is a prime number.')
    else:
        print(f'{my_num} is not a prime number. It is divisible by {i} and {int(my_num/i)}.')
