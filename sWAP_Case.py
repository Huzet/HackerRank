#!/bin/bash

# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    newstring = ""
    for x in s:
        if (x.isupper() == True):
            x = x.lower()
        else:
            x = x.upper()
        newstring = newstring + x
    return newstring
if __name__ == '__main__':
    s = input()
    swap_case(s)
    result = swap_case(s)
    print(result)