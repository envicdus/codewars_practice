'''
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	return
name equals owner	'Hello boss'
otherwise	'Hello guest'
'''

# my solution

def greet(name, owner):
    # Add code here
    return "Hello boss" if name == owner else "Hello guest"

# other solution

# 1

def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")

# 2

def greet(name, owner):
    return f"Hello {'boss' if name == owner else 'guest'}"

# 3

def greet(name, owner):
    return 'Hello '+['guest','boss'][name==owner]