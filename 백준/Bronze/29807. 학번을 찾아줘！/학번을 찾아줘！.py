t=int(input())
score=list(map(int,input().split()))

num=0

if t<5:
    for i in range(5-t):
        score.append(0)

if score[0]>=score[2]:
    num+=(score[0]-score[2])*508
else:
    num+=(max(score[0],score[2])-min(score[0],score[2]))*108

if score[1]>=score[3]:
    num+=(score[1]-score[3])*212
else:
    num+=(max(score[1],score[3])-min(score[1],score[3]))*305

if score[-1]:
    num+=score[-1]*707

print(num*4763)