'''
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''
# my solution

def longest(a1, a2):
    # your code
    return "".join(sorted(set(a1+a2)))

# other solution

# 1

def longest(s1, s2):
    return ''.join(sorted((set(s1+s2))))

# 2

def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))

# 3

def longest(s1, s2):
    return ''.join(sorted(set(s1).union(s2)))