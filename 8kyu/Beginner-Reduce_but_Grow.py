'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''

# my solution

import math

def grow(arr):
    return math.prod(arr)

# other solution

# 1

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

# 2

from math import prod as grow

# 3

def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product