"""
DESCRIPTION:
Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.

Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).

Don't worry about numbers, special characters, or non-string types being passed to the function. The string lengths will be from 1 character up to 10 characters, but will never be empty.
"""

# my solution

def capitalize_word(word):
    return word.capitalize()

# other solutions

# 1
def capitalizeWord(s):
    return s.title()

# 2
def capitalizeWord(word):
    return word[0].upper() + word[1:]