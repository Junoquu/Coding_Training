import sys
input = sys.stdin.readline

for i in range(3):
    n=int(input())
    sum=0
    for i in range(n):
        num=int(input())
        sum+=num

    if sum>0:
        print('+')
    elif sum==0:
        print(0)
    else:
        print('-')