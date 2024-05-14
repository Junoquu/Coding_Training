def solution(numbers):
    answer = ''
    eng_num={'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
            'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    num=''
    for i in numbers:
        num+=i
        if num in eng_num:
            answer+=eng_num[num]
            num=''
        
    return int(answer)