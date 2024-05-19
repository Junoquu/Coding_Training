codes=input().split('-')
code=codes[0][:5]

n=int(input())
cnt=0

for i in range(n):
    subjects=input().split('-')
    subject=subjects[0][:5]

    if code == subject:
        cnt+=1

print(cnt) 