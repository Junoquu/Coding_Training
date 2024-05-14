def triangles(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end='')
        print()

while True:
    n=int(input())
    if n==0:
        break
    else:
        triangles(n)