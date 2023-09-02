"""
Color Ghost
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
"""

# my solution

import random


class Ghost(object):
    # your code goes here
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

# other solution

# 1
import random

class Ghost(object):
  colors = ["white", "yellow", "purple", "red"]
  
  def __init__(self):
    self.color = random.choice(Ghost.colors)

# 2

import random
colors = ['white', 'yellow', 'purple', 'red']
class Ghost(object):
    def __init__(self):
        self.color = colors[random.randint(0,3)]