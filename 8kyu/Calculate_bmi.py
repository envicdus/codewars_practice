'''
DESCRIPTION:
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''

def bmi(weight, height):
    #your code here
    calc_bmi = weight/height**2
    if calc_bmi <= 18.5:
        return "Underweight"
    if calc_bmi <= 25.0:
        return "Normal"
    if calc_bmi <= 30.0:
        return "Overweight"
    if calc_bmi > 30:
        return "Obese"


# other solutions

# 1

def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
# you can add boolean values in Python (True -> 1, False -> 0). For example, if b == 27 then you get for (b > 30) + (b > 25) + (b > 18.5) -> False + True + True -> 0 + 1 + 1 -> 2 ['Underweight', 'Normal', 'Overweight', 'Obese'][2] -> 'Overweight

# 2

def bmi(weight, height):
    bmi = weight / height ** 2
    return 'Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese"

# 3

bmi = lambda w,h: (lambda b=w/h**2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5<b) + (25<b) + (30<b)])()