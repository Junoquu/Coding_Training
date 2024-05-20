t=int(input())

for _ in range(t):
    g,c,e=map(int,input().split())
    result=0
    if g==1:
        result=e-c
    elif g==2:
        result=(e-c)*3
    elif g==3:
        result=(e-c)*5
    
    if result>0:
        print(result)
    else:
        print(0)