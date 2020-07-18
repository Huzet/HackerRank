#!/bin/Python3

# https://www.hackerrank.com/challenges/designer-door-mat/problem

def doorMat(height):
    mat = []
    width = 3 * height


    for x in range(0, height):
        column = []
        for y in range(0, width):
         column.append('-')
         mat.append(column)
    print(mat)
    for y in range(height):
        for x in range(width):
            print(mat[x][y], end='')
        print() 

doorMat(9)