"""
Your task is simply to count the total number of lowercase letters in a string.

Examples
"abc" ===> 3

"abcABC123" ===> 3

"abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3

"" ===> 0;

"ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0

"abcdefghijklmnopqrstuvwxyz" ===> 26
"""

# my solution

import re

def lowercase_count(strng):
    # Your code here
    return len(re.findall(r"[a-z]", strng))

# other solutions

# 1
def lowercase_count(strng):
    return sum(a.islower() for a in strng)

# 2
def lowercase_count(str):
    return sum(1 for c in str if c.islower())

# 3
def lowercase_count(strng):
    return len([ch for ch in strng if ch.islower()])