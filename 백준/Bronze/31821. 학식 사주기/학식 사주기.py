n=int(input())
prices=[]
for _ in range(n):
    price=int(input())
    prices.append(price)
m=int(input())
result=0
for _ in range(m):
    idx=int(input())
    result+=prices[idx-1]
print(result)