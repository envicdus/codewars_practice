"""
DESCRIPTION:
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""

# my solution

def abbrev_name(name):
    initial_name = name.split()
    return "{}.{}".format(initial_name[0][0].upper(), initial_name[1][0].upper())

# other solution

# 1

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

# 2
def abbrevName(name):
    names = name.split()
    return f"{names[0][0]}.{names[1][0]}".upper()

# 3

def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

# 4

def abbrevName(name):
    return '.'.join(filter(str.isupper,name.title()))