n=int(input())
t_size=list(map(int,input().split()))
t,p=map(int,input().split())
order_t=0

for i in t_size:
    if i>0 and i//t==0:
        order_t+=1
    elif i//t>0 and i%t==0:
        order_t+=i//t
    elif i//t>0 and i%t!=0:
        order_t+=i//t+1

print(order_t)
print(n//p,n%p)