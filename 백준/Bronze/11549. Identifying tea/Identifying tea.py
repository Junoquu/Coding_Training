correct=int(input())
participants=list(map(int,input().split()))
cnt=0

for i in participants:
    if i==correct:
        cnt+=1
print(cnt)