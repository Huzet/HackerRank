# https://www.hackerrank.com/challenges/diagonal-difference/problem

arr =  [[3,2,4],
        [4,4,6],
        [4,8,3]]

def diagonalDifference(arr):
    left_diagonal=0   # GOOD
    right_diagonal=0
    for x in range(0,len(arr[0]),1):
        left_diagonal=left_diagonal +arr[x][x]
    for i in range(len(arr[0])-1,-1,-1):
        # print(i)
        # print(abs(i-(len(arr)-1)))
        right_diagonal=right_diagonal +arr[i][abs(i-(len(arr)-1))]
    # print(f"left {left_diagonal}")
    # print(f"right {right_diagonal}")
    total=abs(right_diagonal-left_diagonal)
    print(total)

diagonalDifference(arr)