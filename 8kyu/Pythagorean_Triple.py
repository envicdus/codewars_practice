"""
Given an unsorted array of 3 positive integers [ n1, n2, n3 ], determine if it is possible to form a Pythagorean Triple using those 3 integers.

A Pythagorean Triple consists of arranging 3 integers, such that:

a2 + b2 = c2

Examples
[5, 3, 4] : it is possible to form a Pythagorean Triple using these 3 integers: 32 + 42 = 52

[3, 4, 5] : it is possible to form a Pythagorean Triple using these 3 integers: 32 + 42 = 52

[13, 12, 5] : it is possible to form a Pythagorean Triple using these 3 integers: 52 + 122 = 132

[100, 3, 999] : it is NOT possible to form a Pythagorean Triple using these 3 integers - no matter how you arrange them, you will never find a way to satisfy the equation a2 + b2 = c2

Return Values
For Python: return True or False
For JavaScript: return true or false
Other languages: return 1 or 0 or refer to Sample Tests.
"""
# my solution

# input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    # return True if it is possible to form a Pythagorean triple with the 3 integers
    # return False if it is not possible
    x = integers[0] * integers[0]
    y = integers[1] * integers[1]
    z = integers[2] * integers[2]
    return True if (x == y + z or y == x + z or z == x + y) else False

# Other solutions

# 1
def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a * a + b * b == c * c

# 2

def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a**2 + b**2 == c**2

# 3

def pythagorean_triple(arr): 
    arr = sorted(arr); # sorted array
    return arr[0]**2 + arr[1]**2 == arr[2]**2;