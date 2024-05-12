def solution(my_string):
    answer = ''
    remove_string=['a','e','i','o','u']
    
    for i in my_string:
        if i not in remove_string:
            answer+=i
    
    return answer