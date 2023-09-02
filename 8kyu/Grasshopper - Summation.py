"""
DESCRIPTION:
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example (Input -> Output):

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
"""

# my solution

def summation(num):
    return sum(list(i for i in range(0, num + 1))) # Code here

# other solution

# 1

def summation(num):
    return (1+num) * num / 2
