#!/bin/Python3

# https://www.hackerrank.com/challenges/designer-door-mat/problem

def doorMat(height):
    mat = []
    width = 3 * height

    for x in range(0, height):
        mat.append('-')
        for y in range(0, width):
         mat.append('-')
    
    for y in range(height):
        for x in range(width):
            print(mat[x][y], end='')
    print()

doorMat(7)