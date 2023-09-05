'''
Given an integer, if the length of it's digits is a perfect square, return a square block of sqroot(length) * sqroot(length). If not, simply return "Not a perfect square!".

Examples:

1212 returns:

"12
12"
Note: 4 digits so 2 squared (2x2 perfect square). 2 digits on each line.

123123123 returns:

"123
123
123"
Note: 9 digits so 3 squared (3x3 perfect square). 3 digits on each line.
'''

# my solution
def square_it(digits):
    # Your code here
    s = str(digits)
    s_len = len(s)
    len_sqrt = s_len ** 0.5
    int_sqrt = int(len_sqrt)
    if len_sqrt == int_sqrt:
        return '\n'.join(s[a:a + int_sqrt] for a in range(0, s_len, int_sqrt))
    return 'Not a perfect square!'

# other solution

# 1

def square_it(s):
    s=str(s)
    n = int(len(s)**0.5)
    if n**2 != len(s): return 'Not a perfect square!'
    return '\n'.join(s[i:i+n] for i in range(0, len(s), n))