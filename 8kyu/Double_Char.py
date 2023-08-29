"""
DESCRIPTION:
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!
"""

# my solution

def double_char(s):
    return ''.join(char + char for char in s)

# other solution

# 1
def double_char(s):
    return ''.join(c * 2 for c in s)

# 2
def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res


