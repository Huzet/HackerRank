import hashlib



if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    mylist = tuple(integer_list)
    answer = 0
    for x in range(0,n):
        answer = answer + mylist[x]
    answers= hash(mylist)
    print(answers)