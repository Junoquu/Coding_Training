a,b=map(int,input().split())
k,x=map(int,input().split())
cnt=0

for i in range(k-x,k+x+1):
    if i>=a and i<=b:
        cnt+=1
    
if cnt:
    print(cnt)
else:
    print('IMPOSSIBLE')