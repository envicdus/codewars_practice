'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''


def high_and_low(numbers):
    # ...
    split_numbers = (numbers.split(' '))
    int_num = sorted([int(n) for n in split_numbers])
    return f"{int_num[-1]} {int_num[0]}"

# other solution

# 1

def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))

# 2

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

# 3

def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])