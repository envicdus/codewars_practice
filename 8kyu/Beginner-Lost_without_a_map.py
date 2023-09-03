'''
DESCRIPTION:
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''

# my solution

def maps(a):
    return [i*2 for i in a]

# other solution

# 1

def maps(a):
    return map(lambda x:2*x, a)

# 2

def maps(a):
    return list(map(lambda s: s*2, a))

# 3

def maps(a):
    b = list()
    for i in range(len(a)):
        b.append(a[i]*2)
    return b