depth=0

for _ in range(4):
    string,height=input().split()
    if string=='Es':
        depth+=int(height)*21
    elif string=='Stair':
        depth+=int(height)*17
print(depth)