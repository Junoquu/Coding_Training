def solution(dots):
    answer = 0
    x=max(dots, key=lambda n:n[0])[0]-min(dots, key=lambda n:n[0])[0]
    y=max(dots, key=lambda n:n[1])[1]-min(dots, key=lambda n:n[1])[1]
    answer=x*y
    return answer