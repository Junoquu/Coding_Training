D,H,M=map(int,input().split())
time=0
time+=(D-11)*1440+(H-11)*60+M-11
if time>=0:
    print(time)
else:
    print(-1)