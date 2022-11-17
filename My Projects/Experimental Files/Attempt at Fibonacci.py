def fibonacci():
    i = int(input('Please enter the number till which you want the Fibonacci Sequence: \n'))
    a = 0
    b = 1
    print(f"\nHere's the Fibonacci sequence till the number {i}:")
    # Iterating over the range of the number entered by the user.
    for i in range(i): # Equivalent to for i in range(0,i):
        c = a + b
        print(a)
        a = b
        b = c
    print(f'Sum till now is {c}')

fibonacci()
