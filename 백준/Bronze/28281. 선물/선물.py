n,x=map(int,input().split())
n_list=list(map(int,input().split()))
result=(n_list[0]+n_list[1])*x

for i in range(2,n):
    gift=(n_list[i-1]+n_list[i])*x
    if result>gift:
        result=gift

print(result)