def is_prime(num):
    if num < 2:
        return False # 2 보다 작은 수는 소수가 아니다.
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False # 나누어 떨어지면 소수가 아니다. -> 약수 판별도 가능
    return True # 나누어 떨어지지 않으니 소수

n = int(input())
nums = list(map(int,input().split()))

prime_cnt = sum(1 for num in nums if is_prime(num))

print(prime_cnt)