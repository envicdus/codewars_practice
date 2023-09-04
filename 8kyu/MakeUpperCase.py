"""
DESCRIPTION:
Write a function which converts the input string to uppercase.
"""
# my solution

def make_upper_case(s):
    # Code here
    return s.upper()

# other solution

# 1

def make_upper_case(s):
    return "".join(i.capitalize() for i in s)

# 2

make_upper_case=lambda s:s.upper()

# 3

make_upper_case = lambda x: x.upper()