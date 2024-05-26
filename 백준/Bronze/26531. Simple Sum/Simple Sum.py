string=input().split()
a=int(string[0])
b=int(string[2])
c=int(string[-1])

if a+b==c:
    print("YES")
else:
    print('NO')