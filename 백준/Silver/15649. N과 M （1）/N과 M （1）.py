def recur(num):
    if num==M:
        print(*ans)
        return
    for i in range(1, N+1):
        if i in ans:
            continue
        ans.append(i)
        recur(num+1)
        ans.pop()
    
N,M = map(int,input().split())
ans = []

recur(0)