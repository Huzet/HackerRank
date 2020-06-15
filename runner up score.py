# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    top_score = max(arr)
    for x in range(0, len(arr)):
        if arr[x] == top_score:
            arr[x] = -99999
    runner_up = max(arr)
    print(runner_up)
    
