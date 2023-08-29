"""
Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.

Example:

['John', 'Smith'], 'Phoenix', 'Arizona'
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!
"""

# My solution

def say_hello(name, city, state):
    #your code here
    return 'Hello, {}! Welcome to {}, {}!'.format(" ".join(name), city, state)

# 1

def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

# 2

def say_hello(name, city, state):
    return 'Hello, %s! Welcome to %s, %s!' % (' '.join(name), city, state)

# 3

def say_hello(name, city, state):
    return 'Hello, ' + ' '.join(name) + '! Welcome to ' + city + ', ' + state + '!'