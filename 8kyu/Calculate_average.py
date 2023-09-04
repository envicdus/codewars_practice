'''
DESCRIPTION:
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
'''

# my solution

# 1

def find_average(numbers):
    # your code here
    return 0 if sum(numbers) == 0 else sum(numbers)/len(numbers)

# 2

def find_average(array):
    return sum(array) / len(array) if array else 0

# 3

def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0