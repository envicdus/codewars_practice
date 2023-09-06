def get_sum(a,b):
    #good luck!
    return sum(list(range(a, b+1))) if a < b else sum(list(range(b, a+1))) if a > b else a

# other solution

# 1
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
# it uses sum of integers formula, S = ((number of integers)(first_term + last_term))/2, which is faster

# 2

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

# 3

def get_sum(a,b):
    a,b = sorted((a, b))
    return sum(range(a, b+1))