#!/bin/python3

# https://www.hackerrank.com/challenges/staircase/problem

import math
import os
import random
import re
import sys

# Complete the staircase function below.

def staircase(n):
    for x in range(1,n+1):
        stairs = ''
        i = 0
        while i < x:
            stairs += '#'
            i = i + 1
        print(stairs)
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
    




