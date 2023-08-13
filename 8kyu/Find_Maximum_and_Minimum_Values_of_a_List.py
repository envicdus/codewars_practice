"""
DESCRIPTION:
Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

Examples (Input -> Output)
* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
Notes
You may consider that there will not be any empty arrays/vectors.
"""

# My Solution

def minimum(arr):
    #your code here...
    return min(arr)

def maximum(arr):
    #...and here
    return max(arr)

# other solutions
#1
def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]
# sorting is O(n log(n)) at worst while min / max is always O(n). So using sorted here is a bad idea

#2
minimum = min
maximum = max

#3
minimum, maximum = min, max

