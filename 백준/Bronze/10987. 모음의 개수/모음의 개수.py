string=input()

cnt=0
for i in string:
    if i in 'aeiou':
        cnt+=1
print(cnt)