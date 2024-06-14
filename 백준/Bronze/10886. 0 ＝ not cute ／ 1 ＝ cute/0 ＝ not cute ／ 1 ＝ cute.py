n=int(input())
n_list=[0]*2

for _ in range(n):
    num=int(input())
    n_list[num]+=1

if n_list[0]>n_list[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')