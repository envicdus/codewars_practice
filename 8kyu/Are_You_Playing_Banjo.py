'''
DESCRIPTION:
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.
'''

# my solution

def are_you_playing_banjo(name):
    # Implement me!
    return f"{name} {'plays banjo' if name[0] == 'r' or name[0] == 'R' else 'does not play banjo'}"

# 1

def areYouPlayingBanjo(name):
   return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"

# 2

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return "{} plays banjo".format(name)
    return "{} does not play banjo".format(name)

# 3

def are_you_playing_banjo(name):
    return name +" plays banjo" if name[0] in 'Rr' else name + " does not play banjo"
