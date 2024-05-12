def solution(numbers, direction):
    answer = numbers
    
    if direction=='right':
        num=answer.pop()
        answer.insert(0,num)
    else:
        num=answer.pop(0)
        answer.append(num)
    return answer