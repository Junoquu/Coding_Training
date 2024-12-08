front =[]
reverse = []
k_list = []

n,m = map(int,input().split())

for _ in range(n):
    a,b = map(int,input().split())
    
    front.append(a)
    reverse.append(b)

for _ in range(m):
    k = int(input())
    
    for idx,value in enumerate(front):
        if k >= value:
            front[idx], reverse[idx] = reverse[idx], front[idx]

print(sum(front))