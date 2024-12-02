from collections import deque

def find_circle(start, visited, matrix):
    dq = deque()
    dq.append(start)
    visited[start] = True
    
    while dq:
        cp = dq.popleft()
        
        for np in matrix[cp]:
            if not visited[np]:
                visited[np] = True
                dq.append(np)
    return 1

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    
    matrix = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    for _ in range(m):
        froms, to = map(int, input().split())
        matrix[froms].append(to)
        matrix[to].append(froms)
    
    cnt = 0
    for idx in range(1, n+1):
        if not visited[idx]:
            cnt += find_circle(idx, visited, matrix)
    
    print(f"#{tc} {cnt}")