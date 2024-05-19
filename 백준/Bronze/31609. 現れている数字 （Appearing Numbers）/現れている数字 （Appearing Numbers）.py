n=int(input())
n_list=list(map(int,input().split()))
result=[]

for i in n_list:
    if i not in result:
        result.append(i)
result.sort()
for _ in result:
    print(_)