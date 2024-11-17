def recur(lev,num):
    check = 0
    if lev==M:
        print(*ans)
        return
    for i in range(N):
        if check != num_input[i] and visited[i] == 0:
            ans.append(num_input[i])
            visited[i] = 1
            check = num_input[i]
            recur(lev+1,0)
            ans.pop()
            visited[i]=0
    
N,M = map(int,input().split())
num_input = sorted(list(map(int,input().split())))
visited = [0]*N
ans = []

recur(0,0)