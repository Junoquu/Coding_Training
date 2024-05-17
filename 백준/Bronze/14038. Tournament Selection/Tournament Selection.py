cnt=0

for i in range(6):
    string=input()
    if string=='W':
        cnt+=1

if cnt<7 and cnt>=5:
    print(1)
elif cnt<5 and cnt>=3:
    print(2)
elif cnt<3 and cnt>=1:
    print(3)
else:
    print(-1)