def solution(my_string):
    new_str = my_string.split(" ")
    answer = int(new_str[0])
    
    for idx in range(1, len(new_str), 2):
        operator = new_str[idx]
        if operator == "+":
            answer += int(new_str[idx+1])
        elif operator == "-":
            answer -= int(new_str[idx+1])
            
    return answer