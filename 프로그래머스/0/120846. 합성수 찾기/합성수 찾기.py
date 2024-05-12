def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return len(divisors)

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if find_divisors(i)>=3:
            answer+=1
    return answer