'''
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
'''
# my solution

def count_sheep(n):
    # your code
    return ''.join([f"{i} sheep..." for i in range(1,n+1)])

# other solution

# 1

def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep

# 2

def count_sheep(n):
    return "".join(str(x) + " sheep..." for x in range(1, n + 1))