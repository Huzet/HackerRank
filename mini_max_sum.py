#!/bin/python3

# https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    newarr = sorted(arr)
    small_count = 0
    big_count = 0
    for x in range(0, 4):
        small_count = small_count + newarr[x]
    for x in range(1, 5):
        big_count = big_count + newarr[x]
    print(small_count, big_count)

if __name__ == '__main__':
    arr = map(int, input().rstrip().split())

    miniMaxSum(arr)