n=int(input())
d=0
p=0
for i in range(n):
    score=input()
    if score=='D':
        d+=1
    elif score=='P':
        p+=1
    if d-p==2 or p-d==2:
        break
print(f"{d}:{p}")