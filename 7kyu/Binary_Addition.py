'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''

# other solution

# 1 
def add_binary(a,b): 
    return bin(a+b)[2:] if a+b>=0 else f"-{bin(a+b)[3:]}"

# 2

def add_binary(a,b):
    return bin(a+b)[2:]
# can't give correct answer for negative binary

# 3

def add_binary(a,b):
    return '{0:b}'.format(a + b)
# works for both positive and negative integer

# 4
def add_binary(a,b):
    return f"{a + b:b}"
