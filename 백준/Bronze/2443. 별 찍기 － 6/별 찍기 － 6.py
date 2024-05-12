n=int(input())

for i in range(n,-1,-1):
    for z in range(n-i):
        print(' ',end='')
    for j in range((i*2)-1):
        print('*',end='')
    print()