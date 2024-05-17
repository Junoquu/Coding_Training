string=input().split()

n=int(string[0])+int(string[2])

if n==int(string[-1]):
    print('YES')
else:
    print('NO')