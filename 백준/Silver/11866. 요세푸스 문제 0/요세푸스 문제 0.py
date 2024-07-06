n,k = map(int,input().split())
n_list=[i for i in range(1,n+1)]
res=[]
idx=0

while n_list:
    idx = (idx + k-1) %len(n_list)
    res.append(n_list.pop(idx))

print("<"+", ".join(map(str,res))+">")