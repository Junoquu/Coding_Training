a,b=map(int,input().split())
res=min(a,b)*2

if a-(res//2)>0 or b-(res//2)>0:
    res+=1

print(res)