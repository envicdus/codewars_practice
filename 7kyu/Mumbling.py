'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
# my solution

def accum(s):
    # your code
    return '-'.join(str.title(l * n) for n, l in enumerate(s, start=1))

# other solutions

# 1

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# 2

def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]