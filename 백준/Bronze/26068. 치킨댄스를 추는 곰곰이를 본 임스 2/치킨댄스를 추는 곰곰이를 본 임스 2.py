n=int(input())
cnt=0
for i in range(n):
    gifticon,day=input().split('-')
    if int(day)<=90:
        cnt+=1
print(cnt)