n=int(input())
cnt=0

for i in range(n):
    check=False
    string=input()

    if 'OI' in string or '01' in string:
        check=True
    if check:
        cnt+=1

print(cnt)