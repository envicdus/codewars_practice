'''
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
'''
# my solution

def string_to_array(s):
    # your code here
    return [''] if s == '' else list(s.split())

# other solution

# 1

def string_to_array(string):
    return string.split(" ")
# string.split() can`t solve testcase when is empty string = ""