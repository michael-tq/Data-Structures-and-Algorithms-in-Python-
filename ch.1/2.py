'''Write a function is_even(k) that takes an integer and tells whether it is even or odd without using multiplication, modulo 
or division operators.'''
a = int(input("Enter a number: "))
def is_even(k):
    if a & 1 == 0:
        print('This number is even.')
    else:
        print('This number is odd.')
