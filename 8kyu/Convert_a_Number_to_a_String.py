"""
DESCRIPTION:
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
"""

# my solution
def number_to_string(num):
    # Return a string of the number here!
    return str(num)

# other solutions
# 1
def number_to_string(num):
    try:
        return str(num)
    except:
        return None

# 2
number_to_string = lambda n: str(n)

# 3
def number_to_string(num):
    # Return a string of the number here!
    # return "%s" % num          # %-formatting
    # return str(num)            # int to string
    # return "{n}".format(n=num) # str.format()
    return f"{num}"              # f-strings