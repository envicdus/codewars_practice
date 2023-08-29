"""
You can print your name on a billboard ad. Find out how much it will cost you. Each character has a default price of £30, but that can be different if you are given 2 parameters instead of 1 (allways 2 for Java).

You can not use multiplier "*" operator.

If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a character).
"""

# my solution

def billboard(name, price=30):
    name_price = 0
    for i in name:
        i = price
        name_price += i
    return name_price

# other solution

# 1

def billboard(name, price=30):
    return sum(price for letter in name)

# 2

def billboard(_n, _p=30): return sum(len( _n ) for _ in range( _p ))

# 3

def billboard(name, price = 30):
    amt = len(name) / (1.0 / price)
    return amt

# 4

def billboard(name, price=30):
    return len(name) / (1 / price)