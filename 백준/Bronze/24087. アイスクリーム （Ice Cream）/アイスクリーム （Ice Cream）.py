s=int(input())
a=int(input())
b=int(input())

if s-a>0:
    h=(s-a)//b
    if (s-a)%b!=0:
        h+=1
    print(250+(h*100))
else:
    print(250)