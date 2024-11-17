def recur(lev,num):
    if lev==M:
        print(*ans)
        return
    for i in num_input:
        ans.append(i)
        recur(lev+1,i)
        ans.pop()
    
N,M = map(int,input().split())
num_input = list(map(int,input().split()))
num_input.sort()
ans = []

recur(0,0)