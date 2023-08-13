"""
DESCRIPTION:
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""
# My solution
def remove_every_other(my_list):
    # Your code here!
    return my_list[::2]

#other solutions

#1
def remove_every_other(my_list):
    return [ my_list[i] for i in range(0,len(my_list),2)]

#2
remove_every_other = lambda m: m[::2]
