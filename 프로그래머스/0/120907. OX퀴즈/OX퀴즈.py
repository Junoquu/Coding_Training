def solution(quiz):
    answer = []
    
    poly=[]
    
    for i in quiz:
        poly=i.split(' ')
        
        xy=0
        if poly[1]=='+':
            xy=int(poly[0])+int(poly[2])
        elif poly[1]=='-':
            xy=int(poly[0])-int(poly[2])
        
        if xy==int(poly[-1]):
            answer.append('O')
        else:
            answer.append('X')
    
    return answer