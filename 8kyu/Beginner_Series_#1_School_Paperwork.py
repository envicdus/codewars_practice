"""
DESCRIPTION:
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

Example:
n= 5, m=5: 25
n=-5, m=5:  0
Waiting for translations and Feedback! Thanks!
"""

# My solution

def paperwork(n, m):
    # Happy Coding! ^_^
    return 0 if n < 0  or m < 0 else n * m

# other solutions

# 1
def paperwork(n, m):
    if m<0 or n<0:
        return 0
    else:
        return n*m

# 2
def paperwork(n, m):
    return n*m if n>=0 and m>=0 else 0

# 3

paperwork = lambda a,b: a*b if min(a,b)>0 else 0
