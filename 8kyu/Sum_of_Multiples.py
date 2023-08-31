"""
Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples
Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"
"""

# my solution

ef sum_mul(n, m):
    if n == 0 or m == 0:
        return 'INVALID'
    elif n == m:
        return 0
    elif n < 0 or m < 0:
        return 'INVALID'
    elif m < n:
        return 0
    else:
        return sum(list(range(n, m, n)))

# other solution

# 1
def sum_mul(n, m):
    suma = 0
    if n <= 0 or m <= 0:
        return "INVALID"
    for number in range(n, m):
        if number % n == 0:
            suma += number
    
    return suma

# 2
def sum_mul(n, m):
    arr = []

    return sum(i for i in range(n,m) if i % n == 0) if n >= 1 and m > 0 else 'INVALID'

# 3

def sum_mul(n, m): 
    if n == 0 or m == 0 or n < 0 or m < 0:
        return 'INVALID'
    elif n == m:
        return 0
    return sum([i for i in range(n, m, n)])


# 4

def sum_mul(n, m):

    #if n > 0 and m > 0:
    #    i = n
    #    sum = 0
    #    while i < m:
    #        if i % n == 0:
    #            sum += i
    #        i += 1
    #    return sum    
    #else:
    #    return 'INVALID'
    return ['INVALID', sum([x for x in range(n, m) if  n != 0 and x % n == 0])][n > 0 and m > 0]
   