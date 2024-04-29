n=int(input())

for i in range(n):
    a,b,x=map(int,input().split())
    print((x-1)*a+b)