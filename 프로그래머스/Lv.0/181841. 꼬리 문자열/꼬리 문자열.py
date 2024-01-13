def solution(str_list, ex):
    answer = ''
    filltered_str = [i for i in str_list if ex not in i]
    answer = "".join(filltered_str)
    return answer