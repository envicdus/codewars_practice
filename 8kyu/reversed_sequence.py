'''
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
'''
# my solution

def reverse_seq(n):
    return list(range(n,0,-1))

# other solution

# 1

def reverseseq(n):
    return range(n, 0, -1)

# 2

def reverseseq(n):
    return [x for x in range(n,0,-1)]

# 3

def reverse_seq(n):
    return [x for x in range(n,0,-1)]