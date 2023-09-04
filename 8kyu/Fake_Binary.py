'''
DESCRIPTION:
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
'''

# my solution

def fake_bin(x):
    return "".join('0' if int(n) < 5  else '1' for n in x)

# other solutions

# 1
def fake_bin(x):
    map = str.maketrans('123456789', '000011111')
    return x.translate(map)

# 2

def fake_bin(x):
    return ''.join([str(int(i) // 5) for i in x])

# 3

fake_bin=lambda x:''.join('10'[e<'5']for e in x)