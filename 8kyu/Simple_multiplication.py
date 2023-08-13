"""
DESCRIPTION:
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""
# My Solution
def simple_multiplication(number) :
    # Your code goes here
    if (number % 2) == 0:
        return number * 8
    else:
        return number * 9
    
# Other Solution

#1
def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8

#2
def simple_multiplication(n) :
    return n * (8 + n%2)
# best and clever solution

#3
simple_multiplication = lambda a : a * (8 + (a & 1))