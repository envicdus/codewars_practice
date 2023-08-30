"""
Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

Note: if this seems too simple for you try the next level
"""

# my solution

def print_array(arr):
    #your code here
    return ",".join(map(str, arr))

# other solution

# 1
def print_array(arr):
    return ','.join(str(a) for a in arr)

# 2
def print_array( _a ): return ','.join([str(i) for i in _a]) 

# 3

print_array=lambda a:','.join(map(str,a))