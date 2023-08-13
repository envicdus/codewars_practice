"""DESCRIPTION:
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.
"""

# My solution
def invert(lst):
    return [number * -1 for number in lst] if len(lst) > 0 else []

# Other Solution

#1
def invert(lst):
    return [-x for x in lst]

#2
def invert(lst):
    return list(map(lambda x: -x, lst));

#3
def invert(lst):
    return list(map(int.__neg__, lst))

