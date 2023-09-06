'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

# my solution

def find_short(s):
    # your code here
    return len(min((word for word in s.split(' ') if word), key=len)) # l: shortest word length

# other solution

# 1
def find_short(s):
    return min(len(x) for x in s.split())

# 2

def find_short(s):
    return len(min(s.split(' '), key=len))

# 3

def find_short(s):
    min(map(len, s.split()))

# 4

find_short = lambda s: min(len(e) for e in s.split())