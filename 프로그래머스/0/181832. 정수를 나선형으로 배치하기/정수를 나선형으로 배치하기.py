def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    y, x, dir = 0, 0, 0
    
    num = 1
    answer[y][x] = num
    
    while num < n**2:
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if 0 <= ny < n and 0 <= nx < n and answer[ny][nx] == 0:
            num+=1
            answer[ny][nx] = num
            y,x = ny,nx
        else:
            dir = (dir + 1) % 4
            
    return answer