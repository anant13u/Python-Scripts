# Error Handling:

def DivBy13(x):
    try:
        return 13 / x
    except ZeroDivisionError:
        print('Error: You tried to divide by Zero')

x = int(input('Please enter a number to be divided by 13: '))
print (DivBy13(x))
x = int(input('Please enter a number to be divided by 13: '))
print (DivBy13(x))
x = int(input('Please enter a number to be divided by 13: '))
print (DivBy13(x))
print (DivBy13(5))

 # Whenever entered 0 as input that line will give us an error as 13/0 will result in an ZeroDivisionError. 
 # To solve that we use the try and except method.
