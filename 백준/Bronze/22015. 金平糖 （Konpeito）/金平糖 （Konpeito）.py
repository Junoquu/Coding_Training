abc=list(map(int,input().split()))
num=0

for i in abc:
    if i != max(abc):
        num+=(max(abc)-i)

print(num)