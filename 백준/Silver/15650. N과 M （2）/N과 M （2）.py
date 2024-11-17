def recur(num, idx):
    if num==M:
        print(*ans)
        return
    for i in range(idx, N+1):
        if i in ans:
            continue
        ans.append(i)
        recur(num+1,i+1)
        ans.pop()
    
N,M = map(int,input().split())
ans = []

recur(0,1)