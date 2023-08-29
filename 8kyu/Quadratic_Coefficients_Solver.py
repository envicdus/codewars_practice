"""
In this Kata you are expected to find the coefficients of quadratic equation of the given two roots (x1 and x2).

Equation will be the form of ax^2 + bx + c = 0

Return type is a Vector (tuple in Rust, Array in Ruby) containing coefficients of the equations in the order (a, b, c).

Since there are infinitely many solutions to this problem, we fix a = 1.

Remember, the roots can be written like (x-x1) * (x-x2) = 0
"""
# My solution

def quadratic(x1, x2):
    # code away!
    coefficient = [1]
    b = (x1 + x2) * -1
    c = x1 * x2
    coefficient.append(b)
    coefficient.append(c)
    tuple_coeff = tuple(coefficient)
    return tuple_coeff

# other solutions
# 1

def quadratic(x1, x2):
    return (1,-x1-x2,x1*x2)

# 2

import numpy as np

def quadratic(*args):
    return tuple(np.poly(args))

# 3

def quadratic(x1, x2):
    """Return the coefficients 
    for a quadratic equation"""
    p = - (x1 + x2)
    q = x1 * x2
    return (1, p, q)
