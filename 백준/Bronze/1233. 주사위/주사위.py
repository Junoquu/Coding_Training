a,b,c=map(int,input().split())
dice=[]
for i in range(1,a+1):
    for j in range(1,b+1):
        for z in range(1,c+1):
            dice.append(i+j+z)

cnt=[0]*(max(dice)+1)
for i in dice:
    cnt[i]+=1

print(cnt.index(max(cnt)))