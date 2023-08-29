"""
DESCRIPTION:
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""

# my solution

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# other solutions

# 1

def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"
  
# 2

def even_or_odd(number):
  return ["Even", "Odd"][number % 2]


