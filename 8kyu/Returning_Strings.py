"""
DESCRIPTION:
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
"""
#my solution

def greet(name):
    #Good Luck (like you need it)
    return f"Hello, {name} how are you doing today?"

# other solution
#1
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

#2
def greet(name):
    return "Hello, %s how are you doing today?" % name

#3
greet = lambda name: f'Hello, {name} how are you doing today?'