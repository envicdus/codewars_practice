'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

# my solution

def get_count(sentence):
    vowels = "aeiou"
    return  len([each for each in sentence if each in vowels])

# other solutions

# 1

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# 2

def getCount(s):
    return sum(c in 'aeiou' for c in s)

# 3

def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])