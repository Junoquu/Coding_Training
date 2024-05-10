n=int(input())
names=[]

for i in range(n):
    name=input()

    for j in name:
        if j=='S':
            names.append(name)

for i in names:
    print(i)