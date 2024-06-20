n_list=[]

n=int(input())

for _ in range(n):
    h,w=map(int,input().split())
    n_list.append(h*w)

print(max(n_list))