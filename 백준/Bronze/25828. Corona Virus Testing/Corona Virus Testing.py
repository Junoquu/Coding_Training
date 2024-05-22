g,p,t=map(int,input().split())

all=g*p
kit=g+p*t

if all<kit:
    print(1)
elif all==kit:
    print(0)
else:
    print(2)