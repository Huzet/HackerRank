#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/grading/problem

def myround(x, base=5):
    while x % base != 0:
        x = x + 1
    return x

def gradingStudents(grades):
    for x in range(0, len(grades)):
        rounded_grade = myround(grades[x])
        if abs(rounded_grade - grades[x]) < 3 and grades[x] >= 38:
            grades[x] = rounded_grade
    print(grades)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()