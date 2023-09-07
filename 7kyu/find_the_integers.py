'''
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''

# my solution
def divisors(integer):
    divisor_list = list(a for a in range(2, int(integer/2) + 1) if integer % a == 0)
    return f"{integer} is prime" if len(divisor_list) == 0 else divisor_list

# other solution

# 1
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n

# 2

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

# 3

def divisors(integer):
  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)
