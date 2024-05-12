def factorial(n,memo):
    if memo[n] != 0:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 1
        return memo[n]
    memo[n]=factorial(n-1,memo)*n
    return memo[n]

def solution(n):
    answer = 0
    memo=[0]*11
    factorial(10,memo)
    for i in range (1,11):
        if n>=memo[i]:
            answer=i
            
    return answer