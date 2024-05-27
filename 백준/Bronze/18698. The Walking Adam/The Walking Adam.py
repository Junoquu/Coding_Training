n=int(input())

for _ in range(n):
    string=input()
    cnt=0
    for i in string:
        if i != 'D':
            cnt+=1
        else:
            break
    print(cnt)