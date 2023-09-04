'''
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
'''

# my solution

def rps(p1,p2):
    retval= {
        "rock":{"rock": 0, "scissors":-1, "paper": 1},
        "scissors":{"rock": 1, "scissors": 0, "paper":-1},
        "paper":{"rock":-1, "scissors": 1, "paper": 0}
    }
    return 'Draw!' if retval[p1][p2] == 0 else 'Player 1 won!' if retval[p1][p2] == -1 else 'Player 2 won!'

# other solution

# 1

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

# 2

def rps(p1, p2):
    d1 = [('paper','rock'), ('rock', 'scissors'), ('scissors', 'paper')]
    return 'Draw!' if p1 == p2 else "Player {} won!".format(1 if (p1, p2) in d1 else 2)

# 3

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

# 4

rps = lambda a, b: ['Draw!', 'Player 1 won!', 'Player 2 won!'][('srp'.index(a[0]) - 'srp'.index(b[0])) % 3]