#!/bin/python3

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    tallest_candle = ar[0]
    candle_count = 0
    for x in ar:
        if tallest_candle < x:
            tallest_candle = x
    for x in ar:
        if tallest_candle == x:
            candle_count = candle_count + 1
    return candle_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
