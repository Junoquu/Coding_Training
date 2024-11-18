import sys
sys.setrecursionlimit(999999999)

def checker(idx, number):
    question_number = questions[idx][0]
    question_strike = questions[idx][1]
    question_ball = questions[idx][2]
    
    strike = 0
    ball = 0
    
    question_number_hundred = question_number // 100
    question_number_ten = (question_number - (question_number_hundred * 100)) // 10
    question_number_one = question_number % 10
    
    number_hundred = number // 100
    number_ten = (number - (number_hundred * 100)) // 10
    number_one = number % 10
    
    if number_hundred == 0 or number_ten == 0 or number_one == 0:
        return False
    
    if number_hundred == number_ten or number_hundred == number_one or number_ten == number_one:
        return False
    
    if number_hundred == question_number_hundred:
        strike += 1
    if number_ten == question_number_ten:
        strike += 1
    if number_one == question_number_one:
        strike += 1
    
    if number_hundred == question_number_ten or number_hundred == question_number_one:
        ball += 1
    if number_ten == question_number_hundred or number_ten == question_number_one:
        ball += 1
    if number_one == question_number_hundred or number_one == question_number_ten:
        ball += 1
        
    if strike == question_strike and ball == question_ball:
        return True
    return False

def recur(idx, num):
    global answer
    
    if idx == n:
        answer += 1
        recur(0, num+1)
        return
    
    if num == 1000:
        return
    
    if checker(idx, num):
        recur(idx + 1, num)
    else:
        recur(0, num + 1)
        
n = int(input())
questions = [list(map(int,input().split())) for _ in range(n)]
answer = 0
recur(0,100)
print(answer)