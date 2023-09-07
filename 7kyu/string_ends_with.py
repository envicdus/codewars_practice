'''
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''
# my solution

# 1
def solution(text, ending):
    # your code here...
    return text.endswith(ending)

# other solution

# 1

def solution(string, ending):
    return (string[len(string)-len(ending):len(string)] == ending)

# 2

def solution(string, ending):
    return ending in string[-len(ending):]

# 3

def solution(string, ending):
    return string[-(len(ending))::] == ending

# 4

def solution(string, ending):
    # your code here...
    return ending == string[len(string)-len(ending):]