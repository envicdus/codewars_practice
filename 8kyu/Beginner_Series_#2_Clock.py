"""
DESCRIPTION:
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
"""
#my solution

def past(h, m, s):
    # Good Luck!
    return (1000 * s) + (m * 60 * 1000) + (h * 3600 * 1000)

#other solution

#1
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000

#2
def past(h, m, s):
    return (s + (m + h * 60) * 60) * 1000