def recur(lev,num):
    if lev==M:
        print(*ans)
        return
    for i in range(num, N+1):
        ans.append(i)
        recur(lev+1,i)
        ans.pop()
    
N,M = map(int,input().split())
ans = []

recur(0,1)