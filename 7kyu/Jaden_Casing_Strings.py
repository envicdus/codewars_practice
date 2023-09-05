'''
aden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
'''

# my solution

def to_jaden_case(string):
    # ...
    return ' '.join(word.capitalize() for word in string.lower().split())

# 1

import string
toJadenCase = string.capwords
'''
what this code is actually doing is -

import string # importing the string module

to_jaden_case = string.capwords # defining a function string.capwords to a variable named (to_jaden_case)

when this code will be runned a function will be called tojaden_case like this - to_jaden_case("the arguments inside")

which would be interpreted as - string.capwords("the arguments inside")

and hence the function actually has a return statement.
'''

# 2

def to_jaden_case(string):
    words = string.split(" ")
    output = ""
    for word in words:
        corrected = word.capitalize()
        output += corrected + " "
        
    return output[0:-1]

# 3

def to_jaden_case(string):
    return ' '.join(map(str.capitalize, string.split()))