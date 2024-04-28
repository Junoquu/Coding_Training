n=int(input())
s=input()
cnt=0

for i in s:
    if i=='a' or i=='i' or i=='u' or i=='e' or i=='o':
        cnt+=1
print(cnt)