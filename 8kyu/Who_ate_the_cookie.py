'''
For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and punctuation.

Please leave feedback for this kata. Cheers!
'''

# my solution

def cookie(x):
    # Zach = string, Monica = Float or int, else = dog
    return f"Who ate the last cookie? It was {'Zach' if type(x) == str else 'Monica' if type(x) == float or type(x) == int  else 'the dog'}!"

# other solution

# 1

def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")

# 2

CULPRITS = {
    str: 'Zach',
    int: 'Monica', float: 'Monica'
}

def cookie(x):
    return "Who ate the last cookie? It was {}!".format(CULPRITS.get(type(x), 'the dog'))

# 3

def cookie(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who

# 4

def cookie(x):
    types = {
        'str': 'Zach',
        'int': 'Monica',
        'float': 'Monica'
    }
        
    return 'Who ate the last cookie? It was {0}!'.format(
            types.get(type(x).__name__, 'the dog'))