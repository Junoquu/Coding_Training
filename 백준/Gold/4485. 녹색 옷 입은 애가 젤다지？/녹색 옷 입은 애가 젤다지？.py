import heapq

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dijkstra(y, x):
    pq = []
    dists = [[21e8 for _ in range(n+1)] for _ in range(n+1)]
    dists[y][x] = matrix[y][x]
    
    heapq.heappush(pq, (matrix[y][x],y,x))
    
    while pq:
        cc, cy, cx = heapq.heappop(pq)
        
        if dists[cy][cx] < cc:
            continue
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            
            nc = cc + matrix[ny][nx]
            
            if dists[ny][nx] <= nc:
                continue
            
            dists[ny][nx] = nc
            
            heapq.heappush(pq,(nc,ny,nx))
            
    return dists[n-1][n-1]    

tc = 1

while True:    
    n = int(input())
    if n == 0:
        break
    matrix = [list(map(int,input().split())) for _ in range(n)]
    
    print(f"Problem {tc}: {dijkstra(0, 0)}")
    tc += 1