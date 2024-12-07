from collections import defaultdict
import heapq

def dijkstra(st,en):
    pq = []
    dists = [21e8 for _ in range(n+1)]
    dists[st] = 0
    
    heapq.heappush(pq,(0,st))
    
    while pq:
        cc, cn = heapq.heappop(pq)
        
        if dists[cn] < cc:
            continue
        
        for next_node, next_cost in bus_info[cn]:
            nc = cc + next_cost
            
            if dists[next_node] <= nc:
                continue
            
            dists[next_node] = nc
            
            heapq.heappush(pq,(nc, next_node))
            
    return dists[en]

n = int(input())
m = int(input())

bus_info = defaultdict(list)

for _ in range(m):
    froms, to, cost = map(int,input().split())
    bus_info[froms].append((to,cost))
    
st, en = map(int,input().split())

print(dijkstra(st,en))