'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
'''
# my solution

def is_isogram(string):
    #your code here
    return len(string) == len(set(string.lower()))

# other solution

# 1

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True

# 2

def is_isogram(string):
    s = set(string.lower()) 
    if len(s) == len(string): 
        return True
    return False
