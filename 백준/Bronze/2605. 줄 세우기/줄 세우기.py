n=int(input())
n_list=list(map(int,input().split()))
stack_list=[]

for i in range(1,len(n_list)+1):
    if n_list[i-1]==0:
        stack_list.append(i)
    else:
        stack_list.insert(i-n_list[i-1]-1,i)

for i in stack_list:
    print(i,end=' ')