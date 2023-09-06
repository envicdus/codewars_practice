'''
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.
'''

# my solution

def friend(x):
    #Code
    return [i for i in x if len(i)==4]


# could even just add .isdigit()/.isalpha() to check for numbers in the string.
# def friend(x): return [f for f in x if len(f) == 4 and not f.isdigit()]

# other solution

# 1

def friend(x):
    return list(filter(lambda s : len(s)==4 ,x))

# 2

def friend(x):
    myFriends = []                   # Initialize list variable
    for person in x:                 # Loop through list of names 
        if len(person) == 4:         # Check to see if the name is of length 4
            myFriends.append(person) # If the name is 4 characters long, append it to variable myFriends
    return myFriends                 # Return myFriends list