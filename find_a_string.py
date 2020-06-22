#!/bin/python3

# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    keep_loop = True
    count = 0
    start_counter = 0
    while keep_loop == True:
        if (string.find(sub_string, start_counter, len(string)) != -1):
            count = count + 1
            start_counter = string.find(sub_string, start_counter, len(string)) + 1
        else:
            keep_loop = False
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)