n=int(input())
n_list=list(map(int,input().split()))
belt=0

for i in n_list:
    if i==1:
        belt+=1
    elif i==-1:
        belt-=1
if belt>0:
    print('Right')
elif belt==0:
    print('Stay')
else:
    print('Left')