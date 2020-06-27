#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    newtime = s.split(":")
    if newtime[2][2] == "P" and int(newtime[0]) == 12:
        newtime[0] = str('12')
        newtime[2] = newtime[2].replace('PM', '')
        newtime[0] = str(newtime[0])
        newtime = str(':'.join(newtime))
        return newtime

    elif newtime[2][2] == "P":
        newtime[0] = int(newtime[0]) + 12
        newtime[2] = newtime[2].replace('PM', '')
        newtime[0] = str(newtime[0])
        newtime = str(':'.join(newtime))
        return newtime

    elif newtime[2][2] == "A" and int(newtime[0]) == 12:
        newtime[0] = str('00')
        newtime[2] = newtime[2].replace('AM', '')
        newtime[0] = str(newtime[0])
        newtime = str(':'.join(newtime))
        return newtime

    elif newtime[2][2] == "A":
        newtime[2] = newtime[2].replace('AM', '')
        newtime[0] = str(newtime[0])
        newtime = str(':'.join(newtime))
        return newtime

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # f.write(result + '\n')

    # f.close()
