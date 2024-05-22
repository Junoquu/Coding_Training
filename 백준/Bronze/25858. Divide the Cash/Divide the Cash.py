n,d=map(int,input().split())
n_list=[]
for _ in range(n):
    n_list.append(int(input()))

divid_d=d//sum(n_list)

for i in n_list:
    print(divid_d*i)