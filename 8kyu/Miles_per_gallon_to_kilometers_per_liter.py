"""
Sometimes, I want to quickly be able to convert miles per imperial gallon (mpg) into kilometers per liter (kpl).

Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).

Make sure to round off the result to two decimal points.

Some useful associations relevant to this kata:

1 Imperial Gallon = 4.54609188 litres
1 Mile = 1.609344 kilometres
"""

# My solution

def converter(mpg):
    #your code here
    return round((mpg * 1.609344) /4.54609188, 2)

# 1
def converter(mpg):
    '''Converts mpg to kpl. Rounds to two decimal places.'''
    kpl = round(mpg * 1.609344/4.54609188, 2)
    return kpl

# 2
KM_PER_MILE = 1.609344
LITERS_PER_UK_GALLON = 4.54609188

def converter(mpg):
    return round(mpg * KM_PER_MILE / LITERS_PER_UK_GALLON, 2)

# 3
converter = lambda x: round(x * 0.354006043538, 2)