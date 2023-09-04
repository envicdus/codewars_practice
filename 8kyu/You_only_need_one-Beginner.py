'''
DESCRIPTION:
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
'''

# my solution

def check(seq, elem):
    return True if elem in seq else False

# other solution

# 1

def check(seq, elem):
    return elem in seq

# 2

def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False

# 3

from operator import contains as check