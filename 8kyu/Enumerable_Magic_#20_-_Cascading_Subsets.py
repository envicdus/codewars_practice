"""
Create a method each_cons that accepts a list and a number n, and returns cascading subsets of the list of size n, like so:

each_cons([1,2,3,4], 2)
  #=> [[1,2], [2,3], [3,4]]

each_cons([1,2,3,4], 3)
  #=> [[1,2,3],[2,3,4]]
  
As you can see, the lists are cascading; ie, they overlap, but never out of order.
"""
# my solution

def each_cons(lst, n):
    # your solution here
    cascading_list = []
    for iteration in range(len(lst) - n + 1):
        cascading_list.append(lst[iteration:iteration + n])
    return cascading_list

# other solution

# 1

def each_cons(lst, n):
    return [lst[i:i+n] for i in range(len(lst)) if len(lst[i:i+n]) == n]

# 2

def each_cons(ar1, N):
    arr = []
    for i in range(len(ar1)):
        if len(ar1[i:i+N]) == N:
            arr.append(ar1[i:i+N])
            
    return arr

# 3

def each_cons(List, N): return [ List[x : x+N] for x in range(len( List ) - N + 1) ]

# 4

each_cons = lambda a, n: [a[i:i + n] for i in range(len(a) - n + 1)]