def mod(a,b,c):
    cnt=0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for z in range(1,c+1):
                if i%j==j%z==z%i:
                    cnt+=1
    return cnt

t=int(input())

for i in range(t):
    a,b,c=map(int,input().split())
    print(mod(a,b,c))