"""
DESCRIPTION:
Bob needs a fast way to calculate the volume of a cuboid with three values: the length, width and height of the cuboid. Write a function to help Bob with this calculation.
"""

# my solution

def get_volume_of_cuboid(length, width, height):
    # Code goes here...
    return length * width * height

# other solutions

# 1
def get_volume_of_cuboid(length, width, height):
    return length * width * height


# PEP8: kata function name should use snake_case not mixedCase
getVolumeOfCubiod = get_volume_of_cuboid

# 2
import math
def get_volume_of_cuboid(length, width, height):
    #convert input into a number
    length = float(length)
    width  = float(width)
    height = float(height)
    #check if input is not defined
    if (math.isnan(length) or math.isnan(width) or math.isnan(height)):
        return 0
    #check if input is less or equal to zero
    elif (length <= 0 or width <= 0 or height <= 0):
        return 0
    else:
        return length * width * height
    get_volume_of_cuboid(length, width, height)
# math.isnan ensures the input is a number, and the next statement ensures the input is positive. It prevents the whole program from crashing