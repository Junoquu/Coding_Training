m, n = map(int,input().split())

cnt = 0

while True:
    if cnt % 2 == 0:
        m -= 1
    else:
        n -= 1
    
    if m<=0 or n<=0:
        break
    
    cnt += 1
print(cnt)