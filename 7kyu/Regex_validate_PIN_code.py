'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
'''

import re

def validate_pin(pin):
    #return true or false
    return True if re.fullmatch("\d{4}|\d{6}", pin) else False

# other solution

# 1

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# 2

import re

def validate_pin(pin):
    #return true or false
    return bool(re.fullmatch("\d{4}|\d{6}", pin))