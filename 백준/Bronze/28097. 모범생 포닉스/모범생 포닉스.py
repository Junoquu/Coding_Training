n=int(input())
study=map(int,input().split())
sum=0

for i in study:
    sum+=i

time = sum+(8*(n-1))

if time>=24:
    print(time//24, time%24)
else:
    print(0, time)