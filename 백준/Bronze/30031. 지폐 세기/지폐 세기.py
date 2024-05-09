cash={136:1000,142:5000,148:10000,154:50000}

n=int(input())
money=0

for i in range(n):
    length,width=map(int,input().split())

    if length in cash:
        money+=cash[length]

print(money)