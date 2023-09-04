'''
DESCRIPTION:
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
'''

# my solution

def count_positives_sum_negatives(arr):
    return [] if arr == [] else [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)]

# other solution

# 1

def count_positives_sum_negatives(arr):
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []

# 2

def count_positives_sum_negatives(arr):
    if not arr: return arr
    return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)]

# 3

def count_positives_sum_negatives(arr):
  output = []
  if arr:
    output.append(sum([1 for x in arr if x > 0]))
    output.append(sum([x for x in arr if x < 0]))
  return output