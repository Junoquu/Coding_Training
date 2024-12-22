n = int(input())

dp = [1] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] * i

ans = 0
for i in range(n+1):
    ans += (1/dp[i])
    
print(ans)