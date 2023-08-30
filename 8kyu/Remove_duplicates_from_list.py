"""
DESCRIPTION:
Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

Examples:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]
"""
# My solution

def distinct(seq):
    return list(dict.fromkeys(seq))

# other solutions

# 1

def distinct(seq):
    return sorted(set(seq), key = seq.index)

# 2

def distinct(seq):
    result = []
    seen = set()
    for a in seq:
        if a not in seen:
            result.append(a)
            seen.add(a)
    return result

# 3

from collections import OrderedDict
def distinct(seq):
    return list(OrderedDict.fromkeys(seq))

# 4

def distinct(seq):
    nl = []
    [nl.append(i) for i in seq if i not in nl]
    return nl