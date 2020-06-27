#!/bin/python3
# 
# 

time = "5:05:45AM"
newtime = time.split(":")

if newtime[2][2] == "P":
    newtime[0] = int(newtime[0]) + 12
    print(newtime)
elif newtime[2][2] == "A" and int(newtime[0]) == 12:
    newtime[0] = str('00')
    print(newtime)
elif newtime[2][2] == "A":
    newtime[0] = "0" + newtime[0]
    print(newtime)