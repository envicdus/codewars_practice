"""
What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

Example(Input --> Output)

"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.
"""
# My solution

def add_length(str_):
    #your code here
    return ["{} {}".format(word, len(word)) for word in str_.split(' ')]

# Other Solutions

# 1
def add_length(strr):
	return [i+' '+str(len(i)) for i in strr.split()]

#2
def add_length(str_):
    answer = []
    for word in str_.split():
        answer.append(word + ' ' + str(len(word)))
    return answer

#3
def add_length(s):
    return ['%s %d' % (x, len(x)) for x in s.split()]