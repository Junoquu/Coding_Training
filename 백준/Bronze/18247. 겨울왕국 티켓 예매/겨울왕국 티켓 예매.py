t = int(input())

for tc in range(t):
    n, m = map(int,input().split())

    if n < 12 or m < 4:
        print(-1)
        continue
    
    print(m*11+4)