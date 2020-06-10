#!/bin/python3

# https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    postive = 0
    negative = 0
    zero = 0
    for number in arr:
        if( number > 0):
            postive = postive + 1
        elif( number < 0):
            negative = negative + 1
        elif( number == 0):
            zero =zero + 1
    print(round(postive/len(arr), 6))
    print(round(negative/len(arr), 6))
    print(round(zero/len(arr), 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)