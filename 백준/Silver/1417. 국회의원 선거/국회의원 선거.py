n=int(input())
pick_me=int(input())
n_list=[]
cnt=0

for i in range(n-1):
    n_list.append(int(input()))
n_list.sort(reverse=True)

if n==1:
    print(0)
else:
    while n_list[0] >= pick_me:
        pick_me+=1
        n_list[0]-=1
        cnt+=1
        n_list.sort(reverse=True)
    print(cnt)