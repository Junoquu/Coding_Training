n=int(input())

for _ in range(n):
    a,b,c=map(int,input().split())
    print(f'Data set: {a} {b} {c}')
    for i in range(c):
        if a>b:
            a//=2
        elif a<b:
            b//=2
        elif a==b:
            a//=2
    print(max(a,b),min(a,b))
    print()