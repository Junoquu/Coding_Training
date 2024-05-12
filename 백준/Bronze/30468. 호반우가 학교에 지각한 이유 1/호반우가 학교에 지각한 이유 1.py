s,d,i,l,n=map(int,input().split())

stats = s+d+i+l

if stats//4 < n:
    print(n*4-stats)
else:
    print(0)