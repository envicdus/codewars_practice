"""
Complete the function which converts a binary number (given as a string) to a decimal number.
"""
# My Solution

def bin_to_decimal(inp):
    return int(inp, 2)

# other solution

# 1

def bin_to_decimal(inp):
    num = 0
    inp = inp[::-1]
    for i in range(len(inp)):
        num += int(inp[i]) * 2 ** i
    return num

# 2

bin_to_decimal = lambda inp: int(inp,2)

# 3

def bin_to_decimal(inp):
    return int(inp, base=2)