n,m=map(int,input().split())
a=100-n
b=100-m
c=100-(a+b)
print(a,b,c,a*b,(a*b)//100,(a*b)%100)
print(c+((a*b)//100),(a*b)%100)