"""
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Examples
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
"""
# my solution

def make_negative( number ):
    return number if number <= 0 else number * (-1)

# other solution

# 1
def make_negative( number ):
    # If the number is greater than zero, double the number and subtract it from the original to get the same number as a negative
    if number > 0:
        number = number - (number*2)
    return number

# 2

make_negative = lambda n: -n if n > 0 else n

# 3

def make_negative( number ):
    if number < 0 or number == 0:
        number = number
    elif number > 0:
        number = -number
    return number