h,m=map(int,input().split())

if h==9 and m==0:
    print(0)
elif h==9:
    print(m)
elif h>9:
    print((h-9)*60+m)