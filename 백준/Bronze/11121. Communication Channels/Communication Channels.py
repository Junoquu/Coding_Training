n=int(input())

for i in range(n):
    a,b=map(str,input().split())
    if a == b:
        print('OK')
    else:
        print('ERROR')