#!/bin/python3

# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

line = 'this is a string' 

def split_and_join(line):
   lines = line.split() 
   lines = "-".join(lines)
   return lines

split_and_join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)