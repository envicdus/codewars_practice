'''
Implement a function that accepts 3 integer values a, b, c. The function should return true if 
a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
'''

# my solution

def is_triangle(a, b, c):
    return True if (a + b) > c and (a + c) > b and (b + c) > a else False

# other solution

# 1

def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

# 2

def is_triangle(a, b, c):
    return 2 * max(a, b, c) < a + b + c

# 3

def is_triangle(*args):
    return 2 * max(args) < sum(args)

# 4

def is_triangle(a, b, c):
    return all([a < b+c, b < a+c, c < a+b]) 

