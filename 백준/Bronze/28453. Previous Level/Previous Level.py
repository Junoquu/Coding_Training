n=int(input())
levels=list(map(int,input().split()))
nums=[]
for level in levels:
    if level==300:
        nums.append(1)
    elif level>=275 and level<300:
        nums.append(2)
    elif level>=250 and level<275:
        nums.append(3)
    else:
        nums.append(4)

print(*nums)