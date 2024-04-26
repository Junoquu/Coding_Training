n=int(input())
HalliGalli={}
for i in range(n):
    name,cnt=input().split()
    if name not in HalliGalli:
        HalliGalli[name]=0
    HalliGalli[name]+=int(cnt)

for i in HalliGalli.values():
    if i==5:
        print("YES")
        break
else:
    print("NO")