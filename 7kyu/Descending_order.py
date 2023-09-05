'''
our task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
'''
# my solution

def descending_order(num):
    # Bust a move right here
    return int(''.join(sorted([i for i in str(num)], reverse=True)))


# other solution

# 1

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

# 2

def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')

# 3

def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))

# 4

Descending_Order = lambda n: int(''.join(reversed(sorted(str(n)))))