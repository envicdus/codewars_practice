"""
Given the molecular mass of two molecules M1 and M2, their masses present m1 and m2 in vessel of volume V at a 
specific temperature T, find the total pressure Ptotal exerted by molecules.

Output: Ptotal, in units atm
Note: temperature is given in Celcius while SI unit is kelvin
"""

# my solution

def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    return (((given_mass1/molar_mass1)+(given_mass2/molar_mass2))*0.082*(temp + 273.15))/volume # your code goes here

# other solution

# 1
def solution(M1, M2, m1, m2, V, T) :
    return (m1/M1+m2/M2)*0.082*(T+273.15)/V

# 2
def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    

    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2 # 1 - Calculate the amount of substance in moles
    Temp_Kelvin = temp + 273.15 # 2 - Convert the temperature from Celcius to kelvin 
    R = 0.082 # 3 - Enter the gas constant
    P1 = (n1 * R * Temp_Kelvin) / volume
    P2 = (n2 * R * Temp_Kelvin) / volume # 4 - Calculate the ideal gas law
    P = P1 + P2 # 5 - Apply Dalton's law
    return P

# 3
def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    R = 0.082  # Gas constant
    T = temp + 273.15  # Kelvin
    n1 = given_mass1 / molar_mass1  # Amount of substance 1
    n2 = given_mass2 / molar_mass2  # Amount of substance 2
    return (n1 + n2) * R * T / volume