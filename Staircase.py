#!/bin/python3

# https://www.hackerrank.com/challenges/staircase/problem

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def str_append(s, n):
    output = ''
    i = 0
    while i < n:
        output = output + s
        i = i + 1
    return output

def staircase(n):
    for x in range(1,n+1):
        print(str_append('#', x).rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
    




