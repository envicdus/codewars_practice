"""
write me a function stringy that takes a size and returns a string of alternating 1s and 0s.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.
"""

# my solution

def stringy(size):
    # Good Luck!
    return "10" * (size // 2) + "1" * (size % 2)

# other solutions

# 1

def stringy(size):
    return ('10' * size)[:size]

# 2

def stringy(size):
    return "".join([str(i % 2) for i in range(1, size + 1)])

# 3

def stringy(size):
    res = ""
    for x in range(0, size):
        res += "1" if x % 2 == 0 else "0"
    return res