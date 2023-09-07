'''
Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
    return ' '.join(map(str, [''.join(reversed(i)) for i in text.split(' ')]))

# other solution

# 1

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

# 2

import re

def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)

# 3

def reverse_words(str):
  return " ".join(map(lambda word: word[::-1], str.split(' ')))