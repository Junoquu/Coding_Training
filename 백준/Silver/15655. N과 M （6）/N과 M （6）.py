def recur(lev,num):
    if lev==M:
        print(*ans)
        return
    for i in range(num,N):
        if num_input[i] in ans:
            continue
        ans.append(num_input[i])
        recur(lev+1,i)
        ans.pop()
    
N,M = map(int,input().split())
num_input = list(map(int,input().split()))
num_input.sort()
ans = []

recur(0,0)