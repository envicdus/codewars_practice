'''
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''
# my solution

def sum_two_smallest_numbers(numbers):
    #your code here
    return sum((sorted(numbers))[0:2])

# other solution

# 1

def sum_two_smallest_numbers(numbers):
    lowest_num1 = numbers[0]
    index = 0
    for i in range(0,len(numbers)):
        if lowest_num1 > numbers[i]:
            lowest_num1 = numbers[i]
            index = i
    numbers.pop(index)
    lowest_num2 = numbers[0]
    for i in range(0,len(numbers)):
        if lowest_num2 > numbers[i]:
            lowest_num2 = numbers[i]
            index = i;
    return lowest_num1 + lowest_num2

# 2

def sum_two_smallest_numbers(numbers):
    min1, min2 = numbers[0:2]
    
    for i in range(2, len(numbers)):
        if numbers[i] < min2 and numbers[i] < min1:
            min1 = numbers[i]
        elif min1 < numbers[i] < min2:
            min2 = numbers[i]
            
    return min1 + min2