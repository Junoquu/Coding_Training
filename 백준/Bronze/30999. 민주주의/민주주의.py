n,m=map(int,input().split())
cnt=0

for i in range(n):
    voting=input()
    O=0
    for z in voting:
        if z=='O':
            O+=1
    if O>(m//2):
        cnt+=1

print(cnt)