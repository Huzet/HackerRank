#!/bin/python3

# https://www.hackerrank.com/challenges/capitalize/problem

import math
import os
import random
import re
import sys


def solve(s):
    mylist = []
    title = s.split(" ")
    for x in title:
        mylist.append(x.capitalize()) 
    return " ".join(mylist)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()