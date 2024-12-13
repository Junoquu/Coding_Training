def solution(array, commands):
    answer = []
    
    for com in commands:
        new_arr = array[com[0]-1:com[1]]
        new_arr = sorted(new_arr)
        answer.append(new_arr[com[-1]-1])
    
    return answer