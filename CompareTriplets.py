#!/bin/python3

import math
import os
import random
import re
import sys

# Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for x in range(3):
        if(a[x] == b[x]):
            continue
        elif(a[x] > b[x]):
            alice=alice+1
        else:
            bob=bob+1
    return(alice, bob)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()