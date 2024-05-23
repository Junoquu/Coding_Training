n=int(input())

for _ in range(n):
    n_list=list(map(int,input().split()))
    find_mack=False
    find_zack=False
    print(*n_list)
    for i in n_list:
        if i==17:
            find_zack=True
        elif i==18:
            find_mack=True
    if find_mack and find_zack:
        print('both')
    elif find_mack:
        print('mack')
    elif find_zack:
        print('zack')
    else:
        print('none')
    print()