#!/bin/python3



if __name__ == '__main__':
    s = input()
    counter = 0
    for letters in s:
        if letters.isalnum() == True:
            counter = counter + 1        
    if counter > 0:
        print(True)
    else:
        print(False)
    counter = 0
    for letters in s:
        if letters.isalpha() == True:
            counter = counter + 1
    if counter > 0:
        print(True)
    else:
        print(False)
    counter = 0    
    for letters in s:
        if letters.isdigit() == True:
            counter = counter +1
    if counter > 0:
        print(True)
    else:
        print(False)
    
    counter = 0
    for letters in s:
        if letters.islower() == True:
            counter = counter +1
    if counter > 0:
        print(True)
    else:
        print(False)

    counter = 0
    for letters in s:
        if letters.isupper() == True:
            counter = counter +1
    if counter > 0:
        print(True)
    else:
        print(False)       

