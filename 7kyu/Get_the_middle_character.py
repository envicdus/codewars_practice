'''
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
#Input

A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.
'''

# my solution

def get_middle(s):
    return s[int(len(s)/2)] if len(s)%2 != 0 else s[(int(len(s)/2))-1:int(len(s)/2)+1]

# other solution

# 1

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]

# 2

def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s

# 3

def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]

