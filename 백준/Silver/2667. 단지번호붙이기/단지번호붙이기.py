from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def BFS(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    cnt = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((ny, nx))
                cnt += 1
    return cnt

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(BFS(graph, i, j))

cnt.sort()

print(len(cnt))

for i in range(len(cnt)):
    print(cnt[i])