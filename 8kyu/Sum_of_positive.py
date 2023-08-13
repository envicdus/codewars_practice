"""
DESCRIPTION:
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

# My Solution
def positive_sum(arr):
    # Your code here
    return sum(number for number in arr if number > 0)

#1
def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

#2
def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))

#3
def positive_sum(arr):
    return sum(map(lambda x: x if x > 0 else 0, arr))