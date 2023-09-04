"""
DESCRIPTION:
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
"""

# my solution

def lovefunc( flower1, flower2 ):
    # ...
    return False if flower1 == flower2 or flower1 %2 == 0 and flower2 %2 == 0 or flower1 %2 > 0 and flower2 %2 > 0 else True

# other solution

# 1

def lovefunc( flower1, flower2 ):
    return bool((flower1+flower2) % 2)

# 2

def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2 == 1

# 3

def lovefunc( flower1, flower2 ):
    return (flower1 + flower2)%2 != 0