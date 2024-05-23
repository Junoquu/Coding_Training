n=int(input())

for _ in range(n):
    n_list=list(map(int,input().split()))
    ten=0
    print(*n_list)
    for i in n_list:
        if i>=10:
            ten+=1
    if ten==1:
        print('double')
    elif ten==2:
        print('double-double')
    elif ten==3:
        print('triple-double')
    elif ten==0:
        print('zilch')
    print()