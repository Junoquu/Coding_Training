k,w,m=map(int,input().split())

ans=w-k
if ans%m==0:
    print(ans//m)
else:
    print(ans//m +1)