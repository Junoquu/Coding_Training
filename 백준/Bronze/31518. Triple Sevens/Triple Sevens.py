n=int(input())
sevens=[]
for _ in range(3):
    m=list(map(int,input().split()))
    for _ in m:
        if _==7:
            sevens.append(7)
            break
if len(sevens)==3:
    print(777)
else:
    print(0)