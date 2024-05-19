time=int(input())
candy_cnt = int(input())
candies=list(map(int,input().split()))
time_cnt=0

for _ in candies:
    time_cnt+=_

if time<=time_cnt:
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')