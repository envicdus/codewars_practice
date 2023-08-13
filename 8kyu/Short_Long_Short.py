"""
DESCRIPTION:
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ).

Hint for R users:

The length of string is not always the same as the number of characters
For example: (Input1, Input2) --> output

("1", "22") --> "1221"
("22", "1") --> "1221"
"""
# My Solution

def solution(a, b):
    return (b + a + b) if len(a) > len(b) else (a + b + a)

# Other Solution

#1
def solution(a, b):
    if len(a)>len(b):
        return(b+a+b)
    else:
        return(a+b+a)
    
#2
def solution(a, b):
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))
# Takes more time as sorting is generally O(nlogn) while you can compare len(a), len(b) faster than sorting.