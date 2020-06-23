#!/bin/python3

import math
import os
import random
import re
import sys

s = 'adam bom g3 3g'

def solve(s):
    title = s.title()
    print(title)
    return title
    

solve(s)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()