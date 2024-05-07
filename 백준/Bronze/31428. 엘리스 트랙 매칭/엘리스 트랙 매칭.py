n=int(input())
n_list=list(input().split())
track=input()
cnt=0

for i in n_list:
    if i==track:
        cnt+=1

print(cnt)