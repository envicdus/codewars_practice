"""
DESCRIPTION:
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
"""

# my solution
def boolean_to_string(b):
    #your code here
    return str(b)

# other solutions

#1
def boolean_to_string(b):
    return 'True' if b else 'False'

#2
def boolean_to_string(b):
    if b:
        return "True"
    return "False"