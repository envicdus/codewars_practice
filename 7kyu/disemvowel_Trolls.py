'''
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
'''
# my solution

def disemvowel(string_):
    return string_.translate({ord(i): None for i in 'aeiouAEIOU'})

# other solutions

# 1

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

# 2

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

# 3

import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

# 4

def disemvowel(string):
    return string.translate(None, 'aAeEuUoOiI')