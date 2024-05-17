a,b,c=map(int,input().split())

if a==b and b==c:
    print('*')
else:
    if a==b and b!=c:
        print('C')
    elif a==c and a!=b:
        print('B')
    elif b==c and b!=a:
        print('A')