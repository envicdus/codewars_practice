'''
You will be given an array of non-negative integers and positive integer bin width.

Your task is to create the Histogram method that will return histogram data corresponding 
to the input array. The histogram data is an array that stores under index i the count of 
numbers that belong to bin i. The first bin always starts with zero.

On empty input you should return empty output.

Examples:

For input data [1, 1, 0, 1, 3, 2, 6] and binWidth=1 the result will be [1, 3, 1, 1, 0, 0, 1] 
as the data contains single element "0", 3 elements "1" etc.
For the same data and binWidth=2 the result will be [4, 2, 0, 1]
For input data [7] and binWidth=1 the result will be [0, 0, 0, 0, 0, 0, 0, 1]
'''

#other solution

# 1

def histogram(lst, w):
    lst = [n // w for n in lst]
    m = max(lst, default=-1) + 1
    return [lst.count(n) for n in range(m)]

# 2

def histogram(values: list, width: int) -> list:
    res = [0] * (max(values, default=-1) // width + 1)
    for value in values:
        res[value // width] += 1
    return res

# 3

def histogram(values, bin_width):
    if not values: return []
    
    bins = [0 for i in range(0, max(values) + 1, bin_width)]
    for value in values:
        bins[value // bin_width] += 1
    return bins

# 4

def histogram(v, w):
    return [sum(j in range(i, w+i) for j in v) for i in range(0, max(v)+1, w)] if v else []