n=input()

cnt=0
for i in n:
    if i=='0':
        cnt+=1
for i in range(len(n)-1,-1,-1):
    if n[i]=='0':
        cnt-=1
    else:
        break
print(cnt)