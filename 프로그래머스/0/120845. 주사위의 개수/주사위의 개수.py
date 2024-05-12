def solution(box, n):
    answer = 1
    answer*=(box[0]//n)
    answer*=(box[1]//n)
    answer*=(box[2]//n)
    return answer