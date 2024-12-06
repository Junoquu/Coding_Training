import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def dijkstra(st):
    pq = []
    dists = [21e8 for _ in range(n+1)]
    dists[st] = 0
    
    heapq.heappush(pq,(0,st))
    
    while pq:
        cost, node = heapq.heappop(pq)
        
        if dists[node] < cost:
            continue
        
        for next_node in graph[node]:
            
            nc = dists[node] + 1
            
            if dists[next_node] <= nc:
                continue
            
            dists[next_node] = nc
            
            if dists[next_node] == k:
                aws.append(next_node)
                
            heapq.heappush(pq,(nc, next_node))
    return dists       

graph = defaultdict(list)
n,m,k,x = map(int,input().strip().split())
aws = []

for i in range(m):
    froms, to = map(int,input().strip().split())
    graph[froms].append(to)
    
dijkstra(x)
aws = sorted(aws)
if aws:
    for i in aws:
        print(i)
else:
    print(-1)