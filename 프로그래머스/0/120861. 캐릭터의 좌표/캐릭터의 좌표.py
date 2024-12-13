def solution(keyinput, board):
    answer = [0, 0]
    
    key = {
        "up" : [0, 1],
        "down" : [0, -1],
        "left" : [-1, 0],
        "right" : [1, 0]
    }
    
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    for key_input in keyinput:
        if key_input in key:
            dx, dy = key[key_input]
            nx = answer[0] + dx
            ny = answer[1] + dy
            
            if -y_limit <= ny <= y_limit and -x_limit <= nx <= x_limit:
                answer[0] = nx
                answer[1] = ny
                
    
    return answer