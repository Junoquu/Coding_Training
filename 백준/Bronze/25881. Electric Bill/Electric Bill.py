fee,extra=map(int,input().split())
n=int(input())

for _ in range(n):
    used=int(input())

    if used<=1000:
        print(used,used*fee)
    else:
        print(used,1000*fee + (used-1000)*extra)