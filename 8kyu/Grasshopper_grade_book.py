'''
Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
'''

ef get_grade(s1, s2, s3):
    # Code here
    if 90 <= (s1+s2+s3)/3 <= 100:
        return 'A'
    elif 80 <= (s1+s2+s3)/3 <= 89:
        return 'B'
    elif 70 <= (s1+s2+s3)/3 <= 79:
        return 'C'
    elif 60 <= (s1+s2+s3)/3 <= 69:
        return 'D'
    else:
        return 'F'

# other solution

# 1

def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')

# 2
def get_grade(s1, s2, s3):
    grades = {range(60): 'F', range(60, 70): 'D', range(70, 80): 'C', range(80, 90): 'B', range(90, 101): 'A'}
    for x in grades:
        if int((s1 + s2 + s3) / 3) in x: return (grades[x])

# 3

