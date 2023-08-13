"""
DESCRIPTION:
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""

# My solution

def bool_to_word(boolean):
    # TODO
    return 'Yes' if boolean == True else 'No'

# Other Solution

#1
def bool_to_word(bool):
    return "Yes" if bool else "No"

#2
def bool_to_word(bool):
     if bool:
         return "Yes"
     return "No"

#3
def bool_to_word(bool):
    return ['No', 'Yes'][bool]
#it will throw an IndexError when going outside the index
#better to use tuple instead of list, it is faster than list.